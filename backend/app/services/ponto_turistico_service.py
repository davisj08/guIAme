from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from app.models.ponto_turistico import PontoTuristico
from app.schemas.ponto_turistico import (
    PontoTuristicoCreate,
    PontoTuristicoUpdate
)


class PontoTuristicoService:
    @staticmethod
    def get_all(
        db: Session,
        skip: int = 0,
        limit: int = 20,
        categoria: Optional[str] = None,
        busca: Optional[str] = None
    ) -> tuple[List[PontoTuristico], int]:
        """Retorna lista de pontos turísticos com filtros"""
        query = db.query(PontoTuristico)

        # Filtro por categoria
        if categoria:
            query = query.filter(PontoTuristico.categoria == categoria)

        # Busca por nome ou descrição
        if busca:
            search_filter = f"%{busca}%"
            query = query.filter(
                (PontoTuristico.nome.ilike(search_filter)) |
                (PontoTuristico.descricao.ilike(search_filter))
            )

        # Contar total
        total = query.count()

        # Aplicar paginação
        pontos = query.offset(skip).limit(limit).all()

        return pontos, total

    @staticmethod
    def get_by_id(db: Session, ponto_id: int) -> Optional[PontoTuristico]:
        """Retorna um ponto turístico por ID"""
        return db.query(PontoTuristico).filter(
            PontoTuristico.id == ponto_id
        ).first()

    @staticmethod
    def create(
        db: Session,
        ponto_data: PontoTuristicoCreate
    ) -> PontoTuristico:
        """Cria um novo ponto turístico"""
        novo_ponto = PontoTuristico(**ponto_data.model_dump())
        db.add(novo_ponto)
        db.commit()
        db.refresh(novo_ponto)
        return novo_ponto

    @staticmethod
    def update(
        db: Session,
        ponto_id: int,
        ponto_data: PontoTuristicoUpdate
    ) -> Optional[PontoTuristico]:
        """Atualiza um ponto turístico"""
        ponto = PontoTuristicoService.get_by_id(db, ponto_id)
        if not ponto:
            return None

        # Atualizar apenas campos fornecidos
        update_data = ponto_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(ponto, field, value)

        db.commit()
        db.refresh(ponto)
        return ponto

    @staticmethod
    def delete(db: Session, ponto_id: int) -> bool:
        """Deleta um ponto turístico do banco de dados"""
        ponto = PontoTuristicoService.get_by_id(db, ponto_id)
        if not ponto:
            return False

        db.delete(ponto)
        db.commit()
        return True

    @staticmethod
    def get_categorias(db: Session) -> List[str]:
        """Retorna lista de categorias únicas"""
        categorias = db.query(PontoTuristico.categoria).distinct().all()
        return [cat[0] for cat in categorias if cat[0] is not None]