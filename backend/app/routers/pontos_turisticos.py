from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import Optional
import math

from app.database.connection import get_db
from app.models.usuario import Usuario
from app.schemas.ponto_turistico import (
    PontoTuristicoCreate,
    PontoTuristicoUpdate,
    PontoTuristicoResponse,
    PontoTuristicoLista
)
from app.schemas.response import ResponseModel, PaginatedResponse
from app.services.ponto_turistico_service import PontoTuristicoService
from app.core.dependencies import get_current_active_user


router = APIRouter(prefix="/pontos-turisticos", tags=["Pontos Turísticos"])


@router.get("", response_model=PaginatedResponse[PontoTuristicoLista])
def listar_pontos(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    categoria: Optional[str] = None,
    busca: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Lista todos os pontos turísticos com paginação e filtros"""
    skip = (page - 1) * page_size

    pontos, total = PontoTuristicoService.get_all(
        db=db,
        skip=skip,
        limit=page_size,
        categoria=categoria,
        busca=busca
    )

    total_pages = math.ceil(total / page_size)

    return PaginatedResponse(
        items=pontos,
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages
    )


@router.get("/categorias", response_model=ResponseModel[list[str]])
def listar_categorias(db: Session = Depends(get_db)):
    """Lista todas as categorias disponíveis"""
    categorias = PontoTuristicoService.get_categorias(db)

    return ResponseModel(
        success=True,
        data=categorias
    )


@router.get(
    "/{ponto_id}",
    response_model=ResponseModel[PontoTuristicoResponse]
)
def obter_ponto(ponto_id: int, db: Session = Depends(get_db)):
    """Obtém detalhes de um ponto turístico específico"""
    ponto = PontoTuristicoService.get_by_id(db, ponto_id)

    if not ponto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ponto turístico não encontrado"
        )

    return ResponseModel(
        success=True,
        data=ponto
    )


@router.post(
    "",
    response_model=ResponseModel[PontoTuristicoResponse],
    status_code=status.HTTP_201_CREATED
)
def criar_ponto(
    ponto_data: PontoTuristicoCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Cria um novo ponto turístico (requer autenticação)"""
    novo_ponto = PontoTuristicoService.create(db, ponto_data)

    return ResponseModel(
        success=True,
        message="Ponto turístico criado com sucesso",
        data=novo_ponto
    )


@router.put(
    "/{ponto_id}",
    response_model=ResponseModel[PontoTuristicoResponse]
)
def atualizar_ponto(
    ponto_id: int,
    ponto_data: PontoTuristicoUpdate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Atualiza um ponto turístico (requer autenticação)"""
    ponto_atualizado = PontoTuristicoService.update(db, ponto_id, ponto_data)

    if not ponto_atualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ponto turístico não encontrado"
        )

    return ResponseModel(
        success=True,
        message="Ponto turístico atualizado com sucesso",
        data=ponto_atualizado
    )


@router.delete("/{ponto_id}", response_model=ResponseModel[None])
def deletar_ponto(
    ponto_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Deleta um ponto turístico (requer autenticação)"""
    sucesso = PontoTuristicoService.delete(db, ponto_id)

    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ponto turístico não encontrado"
        )

    return ResponseModel(
        success=True,
        message="Ponto turístico deletado com sucesso"
    )