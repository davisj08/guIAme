from pydantic import BaseModel, Field
from typing import List, Optional

from app.schemas.ponto_turistico import PontoTuristicoResponse


class RecomendacaoItem(BaseModel):
    """Item de recomendação"""
    ponto: PontoTuristicoResponse
    motivo: str = Field(..., description="Razão da recomendação")
    relevancia: int = Field(
        ...,
        ge=0,
        le=100,
        description="Relevância da recomendação (0-100)"
    )


class RecomendacoesResponse(BaseModel):
    """Resposta com lista de recomendações"""
    recomendacoes: List[RecomendacaoItem]
    total: int


class PreferenciaCreate(BaseModel):
    """Criar/atualizar preferências do usuário"""
    categorias_favoritas: Optional[List[str]] = None
    tipos_atividade: Optional[List[str]] = None
    nivel_interesse_historia: Optional[int] = Field(None, ge=1, le=10)
    nivel_interesse_natureza: Optional[int] = Field(None, ge=1, le=10)
    nivel_interesse_gastronomia: Optional[int] = Field(None, ge=1, le=10)