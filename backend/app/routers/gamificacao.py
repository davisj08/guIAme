from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Dict, Any, Optional

from app.database.connection import get_db
from app.core.security import get_current_active_user
from app.models.usuario import Usuario
from app.models.gamificacao import PontuacaoUsuario, Badge, UsuarioBadge
from app.schemas.gamificacao import (
    PontuacaoResponse,
    BadgeResponse,
    UsuarioBadgeResponse,
    RankingItemResponse, # Corrigido conforme a sugestão de formatação anterior
    MinhaPosicaoResponse
)

# --- Configuração do Roteador ---
router = APIRouter(
    prefix="/api/gamificacao", 
    tags=["Gamificação"]
)

# --- Funções Auxiliares (Lógica de Negócio) ---

def atualizar_nivel(pontuacao: PontuacaoUsuario) -> str:
    """
    Atualiza e retorna o nível do usuário baseado nos pontos totais.

    Níveis:
    - Bronze: 0-99 pontos
    - Prata: 100-499 pontos
    - Ouro: 500-999 pontos
    - Platina: 1000+ pontos
    """
    pontos = pontuacao.pontos_totais

    if pontos >= 1000:
        novo_nivel = "Platina"
    elif pontos >= 500:
        novo_nivel = "Ouro"
    elif pontos >= 100:
        novo_nivel = "Prata"
    else:
        novo_nivel = "Bronze"
    
    # Atualiza o objeto de pontuação (se houver mudança)
    if pontuacao.nivel != novo_nivel:
        pontuacao.nivel = novo_nivel
    
    return novo_nivel

# --- Endpoints de Usuário ---

@router.get("/minha-pontuacao", response_model=PontuacaoResponse)
async def get_minha_pontuacao(
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    🎯 **Retorna a pontuação e progresso do usuário atual.**

    - **pontos_totais**: Total de pontos acumulados
    - **nivel**: Nível atual (Bronze, Prata, Ouro, Platina)
    - **visitas_realizadas**: Quantidade de visitas a pontos turísticos
    - **avaliacoes_feitas**: Quantidade de avaliações realizadas
    """
    pontuacao = db.query(PontuacaoUsuario).filter(
        PontuacaoUsuario.usuario_id == current_user.id
    ).first()

    if not pontuacao:
        # Criar pontuação inicial para o usuário se não existir
        pontuacao = PontuacaoUsuario(usuario_id=current_user.id)
        db.add(pontuacao)
        db.commit()
        db.refresh(pontuacao)
    
    # Garantir que o nível está atualizado
    atualizar_nivel(pontuacao)
    
    return pontuacao


@router.get("/minhas-badges", response_model=List[UsuarioBadgeResponse])
async def get_minhas_badges(
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    🏅 **Retorna todas as badges conquistadas pelo usuário atual.**

    Cada badge contém:
    - **nome**: Nome da conquista
    - **descricao**: Descrição de como conquistar
    - **icone**: Emoji ou ícone da badge
    - **conquistado_em**: Data e hora da conquista
    """
    badges_conquistadas = db.query(UsuarioBadge).filter(
        UsuarioBadge.usuario_id == current_user.id
    ).all()

    return badges_conquistadas

# --- Endpoints de Badges Gerais ---

@router.get("/badges-disponiveis", response_model=List[BadgeResponse])
async def get_badges_disponiveis(
    db: Session = Depends(get_db)
):
    """
    ✨ **Lista todas as badges disponíveis no sistema.**

    Mostra todas as conquistas que podem ser desbloqueadas,
    ordenadas pelo ponto necessário.
    """
    badges = db.query(Badge).order_by(Badge.pontos_necessarios).all()
    return badges

# --- Endpoints de Ranking ---

@router.get("/ranking", response_model=List[RankingItemResponse])
async def get_ranking(
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """
    👑 **Retorna o ranking dos usuários com mais pontos.**

    - **limit**: Quantidade de usuários no ranking (padrão: 10, máximo: 100).

    Retorna lista ordenada por pontuação decrescente.
    """
    # Limita o máximo de usuários retornados
    if limit > 100:
        limit = 100

    # Consulta que faz JOIN com a tabela Usuario e ordena
    ranking_data = db.query(
        PontuacaoUsuario,
        Usuario.nome
    ).join(
        Usuario, PontuacaoUsuario.usuario_id == Usuario.id
    ).order_by(
        PontuacaoUsuario.pontos_totais.desc()
    ).limit(limit).all()

    # Mapeia o resultado para o formato de resposta Pydantic
    resultado: List[Dict[str, Any]] = []
    for idx, (pontuacao, nome) in enumerate(ranking_data, 1):
        # Garante que o nível está atualizado antes de retornar
        nivel_atualizado = atualizar_nivel(pontuacao) 
        
        resultado.append({
            "posicao": idx,
            "usuario_nome": nome,
            "pontos_totais": pontuacao.pontos_totais,
            "nivel": nivel_atualizado,
            "visitas_realizadas": pontuacao.visitas_realizadas
        })
        
    return resultado


@router.get("/minha-posicao", response_model=MinhaPosicaoResponse)
async def get_minha_posicao(
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    📍 **Retorna a posição do usuário atual no ranking geral.**

    Mostra:
    - **posicao**: Posição no ranking (1 = primeiro lugar)
    - **total_usuarios**: Total de usuários com pontuação
    - **pontos**: Pontos do usuário atual
    - **nivel**: Nível do usuário atual
    """
    pontuacao_atual = db.query(PontuacaoUsuario).filter(
        PontuacaoUsuario.usuario_id == current_user.id
    ).first()

    if not pontuacao_atual:
        # Cria pontuação inicial se não existir
        pontuacao_atual = PontuacaoUsuario(usuario_id=current_user.id)
        db.add(pontuacao_atual)
        db.commit()
        db.refresh(pontuacao_atual)
    
    # Atualiza o nível
    nivel_atual = atualizar_nivel(pontuacao_atual)

    # 1. Contar quantos usuários têm mais pontos que o usuário atual
    usuarios_acima = db.query(func.count(PontuacaoUsuario.id)).filter(
        PontuacaoUsuario.pontos_totais > pontuacao_atual.pontos_totais
    ).scalar()

    # 2. Contar o total de usuários com pontuação
    total_usuarios = db.query(func.count(PontuacaoUsuario.id)).scalar()

    # A posição é o número de usuários acima + 1
    posicao = usuarios_acima + 1

    return {
        "posicao": posicao,
        "total_usuarios": total_usuarios,
        "pontos": pontuacao_atual.pontos_totais,
        "nivel": nivel_atual
    }