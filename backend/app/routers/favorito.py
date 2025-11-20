from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List

from app.database.connection import get_db
from app.models.usuario import Usuario
from app.models.ponto_turistico import PontoTuristico
from app.models.favorito import Favorito
from app.schemas import favorito as schemas
from app.core.security import get_current_active_user


# Definição do Roteador
router = APIRouter(prefix="/api/favoritos", tags=["Favoritos"])


## ⭐ Endpoints de Favoritos

### 📌 `POST /api/favoritos`
@router.post("", response_model=schemas.FavoritoResponse, status_code=status.HTTP_201_CREATED)
def adicionar_favorito(
    favorito_data: schemas.FavoritoCreate,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    ⭐ **Adicionar um ponto turístico aos favoritos.**
    
    - Valida se o ponto turístico existe
    - Impede duplicatas (mesmo ponto favoritado duas vezes)
    - Retorna o favorito criado com informações do ponto
    """
    
    # 1. Validar se o ponto turístico existe
    ponto = db.query(PontoTuristico).filter(
        PontoTuristico.id == favorito_data.ponto_turistico_id
    ).first()
    
    if not ponto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ponto turístico não encontrado"
        )
    
    # 2. Verificar se já é favorito
    favorito_existente = db.query(Favorito).filter(
        Favorito.usuario_id == current_user.id,
        Favorito.ponto_turistico_id == favorito_data.ponto_turistico_id
    ).first()
    
    if favorito_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este ponto turístico já está nos seus favoritos"
        )
    
    # 3. Criar favorito
    novo_favorito = Favorito(
        usuario_id=current_user.id,
        ponto_turistico_id=favorito_data.ponto_turistico_id
    )
    
    try:
        db.add(novo_favorito)
        db.commit()
        db.refresh(novo_favorito)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Erro ao adicionar favorito. Pode já existir."
        )
    
    # 4. Preparar resposta com informações do ponto
    response = schemas.FavoritoResponse.from_orm(novo_favorito)
    response.ponto_nome = ponto.nome
    response.ponto_categoria = ponto.categoria
    response.ponto_cidade = None
    
    return response


### 📌 `DELETE /api/favoritos/{ponto_id}`
@router.delete("/{ponto_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_favorito(
    ponto_id: int,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    ❌ **Remover um ponto turístico dos favoritos.**
    
    - Remove o favorito se existir
    - Retorna 404 se não estiver nos favoritos
    """
    
    # Buscar favorito
    favorito = db.query(Favorito).filter(
        Favorito.usuario_id == current_user.id,
        Favorito.ponto_turistico_id == ponto_id
    ).first()
    
    if not favorito:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Este ponto não está nos seus favoritos"
        )
    
    # Remover favorito
    db.delete(favorito)
    db.commit()
    
    return {"message": "Favorito removido com sucesso"}


### 📌 `GET /api/favoritos/meus`
@router.get("/meus", response_model=List[schemas.FavoritoResponse])
def listar_meus_favoritos(
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    📋 **Listar todos os pontos turísticos favoritos do usuário.**
    
    - Retorna lista ordenada por data de adição (mais recentes primeiro)
    - Inclui informações básicas de cada ponto turístico
    """
    
    # Buscar favoritos do usuário
    favoritos = db.query(Favorito).filter(
        Favorito.usuario_id == current_user.id
    ).order_by(Favorito.created_at.desc()).all()
    
    # Preparar resposta com informações dos pontos
    result = []
    for favorito in favoritos:
        fav_dict = schemas.FavoritoResponse.from_orm(favorito)
        fav_dict.ponto_nome = favorito.ponto_turistico.nome
        fav_dict.ponto_categoria = favorito.ponto_turistico.categoria
        fav_dict.ponto_cidade = None
        result.append(fav_dict)
    
    return result


### 📌 `GET /api/favoritos/check/{ponto_id}`
@router.get("/check/{ponto_id}", response_model=schemas.FavoritoCheck)
def verificar_favorito(
    ponto_id: int,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    ✅ **Verificar se um ponto turístico está nos favoritos.**
    
    - Retorna `true` se o ponto está favoritado
    - Retorna `false` caso contrário
    - Útil para UI (mostrar ícone de coração preenchido ou vazio)
    """
    
    # Verificar se existe favorito
    favorito = db.query(Favorito).filter(
        Favorito.usuario_id == current_user.id,
        Favorito.ponto_turistico_id == ponto_id
    ).first()
    
    return schemas.FavoritoCheck(
        ponto_turistico_id=ponto_id,
        is_favorito=favorito is not None
    )
