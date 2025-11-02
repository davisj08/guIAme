from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# ---
## 📝 Schemas de Entrada (Input Schemas)
# ---

class AvaliacaoCreate(BaseModel):
    """Schema para criar uma nova avaliação."""
    ponto_turistico_id: int
    nota: float = Field(..., ge=0.0, le=5.0) # Nota deve estar entre 0.0 e 5.0
    comentario: Optional[str] = Field(None, max_length=1000)

class AvaliacaoUpdate(BaseModel):
    """Schema para atualizar uma avaliação existente."""
    nota: Optional[float] = Field(None, ge=0.0, le=5.0)
    comentario: Optional[str] = Field(None, max_length=1000)

# ---
## 📦 Schema de Saída (Output/Response Schema)
# ---

class AvaliacaoResponse(BaseModel):
    """Schema de retorno da avaliação."""
    id: int
    usuario_id: int
    ponto_turistico_id: int
    nota: float
    comentario: Optional[str]
    criado_em: datetime

    class Config:
        # CORREÇÃO: Indentado para dentro da classe AvaliacaoResponse
        from_attributes = True