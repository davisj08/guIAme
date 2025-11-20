from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class FavoritoCreate(BaseModel):
    """Schema para criar um favorito"""
    ponto_turistico_id: int


class FavoritoResponse(BaseModel):
    """Schema para resposta de favorito"""
    id: int
    usuario_id: int
    ponto_turistico_id: int
    created_at: datetime
    
    # Campos adicionais (preenchidos manualmente no router)
    ponto_nome: Optional[str] = None
    ponto_categoria: Optional[str] = None
    ponto_cidade: Optional[str] = None

    class Config:
        from_attributes = True  # Permite criar a partir de modelos ORM


class FavoritoCheck(BaseModel):
    """Schema para verificar se um ponto é favorito"""
    ponto_turistico_id: int
    is_favorito: bool
