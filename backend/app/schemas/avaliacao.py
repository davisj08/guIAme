from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict

# --- Schemas de Avaliação (Review) ---

class AvaliacaoCreate(BaseModel):
    """Schema para criar uma avaliação."""
    ponto_turistico_id: int = Field(..., description="ID do ponto turístico")
    nota: int = Field(..., ge=1, le=5, description="Nota de 1 a 5 estrelas")
    comentario: Optional[str] = Field(None, description="Comentário sobre o ponto")

class AvaliacaoUpdate(BaseModel):
    """Schema para atualizar uma avaliação."""
    nota: Optional[int] = Field(None, ge=1, le=5, description="Nova nota (1 a 5)")
    comentario: Optional[str] = Field(None, description="Novo comentário")

class AvaliacaoResponse(BaseModel):
    """Schema de resposta de avaliação completa."""
    id: int
    usuario_id: int
    ponto_turistico_id: int
    nota: int
    comentario: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    
    # Informações adicionais injetadas do ORM
    usuario_nome: Optional[str] = None

    class Config:
        from_attributes = True



# --- Schemas de Visita (Check-in) ---

class VisitaCreate(BaseModel):
    """Schema para registrar uma visita (check-in)."""
    ponto_turistico_id: int = Field(..., description="ID do ponto turístico")
    comentario: Optional[str] = Field(None, description="Comentário opcional sobre a visita")
    latitude: Optional[float] = Field(None, description="Latitude do check-in")
    longitude: Optional[float] = Field(None, description="Longitude do check-in")

class VisitaResponse(BaseModel):
    """Schema de resposta de visita (check-in) completa."""
    id: int
    usuario_id: int
    ponto_turistico_id: int
    data_visita: datetime
    comentario: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    created_at: datetime
    
    # Informações adicionais injetadas do ORM
    usuario_nome: Optional[str] = None
    ponto_nome: Optional[str] = None

    class Config:
        from_attributes = True


# --- Schema de Estatísticas ---

class EstatisticasPonto(BaseModel):
    """Schema para exibir estatísticas agregadas de um ponto turístico."""
    ponto_id: int
    ponto_nome: str
    total_avaliacoes: int
    media_avaliacoes: float
    total_visitas: int
    distribuicao_notas: Dict[int, int] = Field(
        ...,
        description="Distribuição de notas por contagem. Ex: {1: 5, 2: 10, ...}"
    )