from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from datetime import datetime

# Importações de dependências e modelos (assumindo que os caminhos estão corretos)
from app.database.connection import get_db
from app.models.usuario import Usuario
from app.models.ponto_turistico import PontoTuristico
from app.models.avaliacao import Avaliacao, Visita
from app.models.gamificacao import PontuacaoUsuario
from app.schemas import avaliacao as schemas
from app.core.security import get_current_active_user
from app.services.badge_service import verificar_e_conceder_badges  # ← NOVO IMPORT

# Definição do Roteador
router = APIRouter(prefix="/api/avaliacoes", tags=["Avaliações e Visitas"])

# --- Funções Auxiliares ---
def _atualizar_nivel_usuario(pontuacao: PontuacaoUsuario):
    """Lógica para atualizar o nível do usuário com base nos pontos totais."""
    if pontuacao.pontos_totais >= 1000:
        pontuacao.nivel = "Platina"
    elif pontuacao.pontos_totais >= 500:
        pontuacao.nivel = "Ouro"
    elif pontuacao.pontos_totais >= 100:
        pontuacao.nivel = "Prata"
    else:
        pontuacao.nivel = "Bronze"


## ⭐️ Endpoints de Avaliações

### 📌 `POST /api/avaliacoes`
@router.post("", response_model=schemas.AvaliacaoResponse, status_code=status.HTTP_201_CREATED)
def criar_avaliacao(
    avaliacao_data: schemas.AvaliacaoCreate,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Criar uma nova avaliação para um ponto turístico."""

    # 1. Validação de Ponto e Avaliação Existente
    ponto = db.query(PontoTuristico).filter(PontoTuristico.id == avaliacao_data.ponto_turistico_id).first()
    if not ponto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ponto turístico não encontrado")

    avaliacao_existente = db.query(Avaliacao).filter(
        Avaliacao.usuario_id == current_user.id,
        Avaliacao.ponto_turistico_id == avaliacao_data.ponto_turistico_id
    ).first()

    if avaliacao_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Você já avaliou este ponto turístico. Use PUT para atualizar."
        )

    # 2. Criação da Avaliação
    nova_avaliacao = Avaliacao(
        usuario_id=current_user.id,
        ponto_turistico_id=avaliacao_data.ponto_turistico_id,
        nota=avaliacao_data.nota,
        comentario=avaliacao_data.comentario
    )
    db.add(nova_avaliacao)

    # 3. Gamificação (+5 pontos)
    pontuacao = db.query(PontuacaoUsuario).filter(PontuacaoUsuario.usuario_id == current_user.id).first()
    if not pontuacao:
        pontuacao = PontuacaoUsuario(
            usuario_id=current_user.id,
            pontos_totais=0,
            visitas_realizadas=0,
            avaliacoes_feitas=0,
            nivel="Bronze"
        )
        db.add(pontuacao)
        db.flush()  # Garante que o objeto está no banco antes de usar

    pontuacao.pontos_totais += 5
    pontuacao.avaliacoes_feitas += 1
    pontuacao.updated_at = datetime.utcnow()
    
    _atualizar_nivel_usuario(pontuacao)

    db.commit()
    db.refresh(nova_avaliacao)

    # 4. ✨ VERIFICAR E CONCEDER BADGES ✨
    verificar_e_conceder_badges(current_user.id, db)

    # 5. Preparar Resposta
    response = schemas.AvaliacaoResponse.from_orm(nova_avaliacao)
    response.usuario_nome = current_user.nome
    
    return response

### 📌 `GET /api/avaliacoes/ponto/{ponto_id}`
@router.get("/ponto/{ponto_id}", response_model=List[schemas.AvaliacaoResponse])
def listar_avaliacoes_ponto(
    ponto_id: int,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Listar todas as avaliações de um ponto turístico."""
    ponto = db.query(PontoTuristico).filter(PontoTuristico.id == ponto_id).first()
    if not ponto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ponto turístico não encontrado")

    avaliacoes = db.query(Avaliacao).filter(
        Avaliacao.ponto_turistico_id == ponto_id
    ).order_by(Avaliacao.created_at.desc()).offset(skip).limit(limit).all()

    result = []
    for avaliacao in avaliacoes:
        av_dict = schemas.AvaliacaoResponse.from_orm(avaliacao)
        # O relacionamento 'usuario' deve estar configurado para buscar o nome
        av_dict.usuario_nome = avaliacao.usuario.nome 
        result.append(av_dict)

    return result

### 📌 `GET /api/avaliacoes/minhas`
@router.get("/minhas", response_model=List[schemas.AvaliacaoResponse])
def listar_minhas_avaliacoes(
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Listar todas as avaliações do usuário logado."""
    avaliacoes = db.query(Avaliacao).filter(
        Avaliacao.usuario_id == current_user.id
    ).order_by(Avaliacao.created_at.desc()).all()

    result = []
    for avaliacao in avaliacoes:
        av_dict = schemas.AvaliacaoResponse.from_orm(avaliacao)
        av_dict.usuario_nome = current_user.nome
        result.append(av_dict)

    return result

### 📌 `PUT /api/avaliacoes/{avaliacao_id}`
@router.put("/{avaliacao_id}", response_model=schemas.AvaliacaoResponse)
def atualizar_avaliacao(
    avaliacao_id: int,
    avaliacao_data: schemas.AvaliacaoUpdate,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Atualizar uma avaliação existente."""
    avaliacao = db.query(Avaliacao).filter(Avaliacao.id == avaliacao_id).first()

    if not avaliacao:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Avaliação não encontrada")

    # 1. Autorização
    if avaliacao.usuario_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para editar esta avaliação"
        )

    # 2. Atualizar Campos
    if avaliacao_data.nota is not None:
        avaliacao.nota = avaliacao_data.nota
    if avaliacao_data.comentario is not None:
        avaliacao.comentario = avaliacao_data.comentario

    avaliacao.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(avaliacao)

    # 3. ✨ VERIFICAR E CONCEDER BADGES ✨
    verificar_e_conceder_badges(current_user.id, db)

    response = schemas.AvaliacaoResponse.from_orm(avaliacao)
    response.usuario_nome = current_user.nome

    return response

### 📌 `DELETE /api/avaliacoes/{avaliacao_id}`
@router.delete("/{avaliacao_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_avaliacao(
    avaliacao_id: int,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Deletar uma avaliação."""
    avaliacao = db.query(Avaliacao).filter(Avaliacao.id == avaliacao_id).first()

    if not avaliacao:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Avaliação não encontrada")

    # 1. Autorização
    if avaliacao.usuario_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para deletar esta avaliação"
        )

    # 2. Remover pontos e atualizar o registro
    pontuacao = db.query(PontuacaoUsuario).filter(PontuacaoUsuario.usuario_id == current_user.id).first()
    if pontuacao:
        pontuacao.pontos_totais = max(0, pontuacao.pontos_totais - 5)
        pontuacao.avaliacoes_feitas = max(0, pontuacao.avaliacoes_feitas - 1)
        _atualizar_nivel_usuario(pontuacao)

    db.delete(avaliacao)
    db.commit()
    
    return {"message": "Avaliação deletada com sucesso"} # Retorna um corpo vazio, mas documenta a ação


## 🗺️ Endpoints de Visitas (Check-in)

### 📌 `POST /api/avaliacoes/visitas`
@router.post("/visitas", response_model=schemas.VisitaResponse, status_code=status.HTTP_201_CREATED)
def registrar_visita(
    visita_data: schemas.VisitaCreate,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Registrar uma visita (check-in) em um ponto turístico."""

    # 1. Validação de Ponto
    ponto = db.query(PontoTuristico).filter(PontoTuristico.id == visita_data.ponto_turistico_id).first()
    if not ponto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ponto turístico não encontrado")

    # 2. Criação da Visita
    nova_visita = Visita(
        usuario_id=current_user.id,
        ponto_turistico_id=visita_data.ponto_turistico_id,
        comentario=visita_data.comentario,
        latitude=visita_data.latitude,
        longitude=visita_data.longitude
    )
    db.add(nova_visita)

    # 3. Gamificação (+10 pontos)
    pontuacao = db.query(PontuacaoUsuario).filter(PontuacaoUsuario.usuario_id == current_user.id).first()
    if not pontuacao:
        pontuacao = PontuacaoUsuario(
            usuario_id=current_user.id,
            pontos_totais=0,
            visitas_realizadas=0,
            avaliacoes_feitas=0,
            nivel="Bronze"
        )
        db.add(pontuacao)
        db.flush()  # Garante que o objeto está no banco antes de usar

    pontuacao.pontos_totais += 10
    pontuacao.visitas_realizadas += 1
    pontuacao.updated_at = datetime.utcnow()
    
    _atualizar_nivel_usuario(pontuacao)

    db.commit()
    db.refresh(nova_visita)

    # 4. ✨ VERIFICAR E CONCEDER BADGES ✨
    verificar_e_conceder_badges(current_user.id, db)

    # 5. Preparar Resposta
    response = schemas.VisitaResponse.from_orm(nova_visita)
    response.usuario_nome = current_user.nome
    response.ponto_nome = ponto.nome # Adiciona o nome do ponto
    
    return response

### 📌 `GET /api/avaliacoes/visitas/minhas`
@router.get("/visitas/minhas", response_model=List[schemas.VisitaResponse])
def listar_minhas_visitas(
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Listar todas as visitas do usuário logado."""
    visitas = db.query(Visita).filter(
        Visita.usuario_id == current_user.id
    ).order_by(Visita.data_visita.desc()).all()

    result = []
    for visita in visitas:
        vis_dict = schemas.VisitaResponse.from_orm(visita)
        vis_dict.usuario_nome = current_user.nome
        # O relacionamento 'ponto_turistico' deve estar configurado
        vis_dict.ponto_nome = visita.ponto_turistico.nome 
        result.append(vis_dict)

    return result

### 📌 `GET /api/avaliacoes/visitas/ponto/{ponto_id}`
@router.get("/visitas/ponto/{ponto_id}", response_model=List[schemas.VisitaResponse])
def listar_visitas_ponto(
    ponto_id: int,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Listar todas as visitas de um ponto turístico."""

    ponto = db.query(PontoTuristico).filter(PontoTuristico.id == ponto_id).first()
    if not ponto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ponto turístico não encontrado")

    visitas = db.query(Visita).filter(
        Visita.ponto_turistico_id == ponto_id
    ).order_by(Visita.data_visita.desc()).offset(skip).limit(limit).all()

    result = []
    for visita in visitas:
        vis_dict = schemas.VisitaResponse.from_orm(visita)
        vis_dict.usuario_nome = visita.usuario.nome
        vis_dict.ponto_nome = ponto.nome
        result.append(vis_dict)

    return result



## 📊 Endpoint de Estatísticas

### 📌 `GET /api/avaliacoes/estatisticas/ponto/{ponto_id}`
@router.get("/estatisticas/ponto/{ponto_id}", response_model=schemas.EstatisticasPonto)
def obter_estatisticas_ponto(
    ponto_id: int,
    db: Session = Depends(get_db)
):
    """Obter estatísticas de um ponto turístico (avaliações e visitas)."""

    ponto = db.query(PontoTuristico).filter(PontoTuristico.id == ponto_id).first()
    if not ponto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ponto turístico não encontrado")

    # 1. Agregações Simples
    total_avaliacoes = db.query(func.count(Avaliacao.id)).filter(
        Avaliacao.ponto_turistico_id == ponto_id
    ).scalar()

    media_avaliacoes = db.query(func.avg(Avaliacao.nota)).filter(
        Avaliacao.ponto_turistico_id == ponto_id
    ).scalar() or 0.0

    total_visitas = db.query(func.count(Visita.id)).filter(
        Visita.ponto_turistico_id == ponto_id
    ).scalar()

    # 2. Distribuição de Notas
    distribuicao = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    notas = db.query(Avaliacao.nota, func.count(Avaliacao.id)).filter(
        Avaliacao.ponto_turistico_id == ponto_id
    ).group_by(Avaliacao.nota).all()

    for nota, count in notas:
        distribuicao[nota] = count

    # 3. Preparar Resposta
    return schemas.EstatisticasPonto(
        ponto_id=ponto_id,
        ponto_nome=ponto.nome,
        total_avaliacoes=total_avaliacoes,
        media_avaliacoes=round(media_avaliacoes, 2), # Arredonda a média para 2 casas decimais
        total_visitas=total_visitas,
        distribuicao_notas=distribuicao
    )