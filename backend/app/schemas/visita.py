from pydantic import BaseModel
from datetime import datetime
from typing import Optional # Importação não usada, mas mantida por convenção

# ---
## 📝 Schema de Entrada (Input Schema)
# ---

class VisitaCreate(BaseModel):
    """Schema para registrar uma nova visita a um ponto turístico."""
    ponto_turistico_id: int
    # Você pode querer adicionar um campo para a data/hora se ela for enviada pelo cliente,
    # mas o usual é que o backend registre o momento da criação.

# ---
## 📦 Schema de Saída (Response Schema)
# ---

class VisitaResponse(BaseModel):
    """Schema de retorno da visita registrada."""
    id: int
    usuario_id: int
    ponto_turistico_id: int
    visitado_em: datetime

    class Config:
        # CORREÇÃO: Indentado para dentro da classe VisitaResponse
        from_attributes = True