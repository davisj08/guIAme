from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ---
## 🏆 Schema de Saída (Response Schema)
# ---

class ConquistaResponse(BaseModel):
    """Schema para representar uma conquista obtida por um usuário."""
    id: int
    usuario_id: int
    tipo: str
    titulo: str
    descricao: Optional[str]
    pontos: int
    icone: Optional[str]
    obtida_em: datetime

    class Config:
        # CORREÇÃO: Indentado para dentro da classe ConquistaResponse
        from_attributes = True