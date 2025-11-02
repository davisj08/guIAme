from pydantic import BaseModel
from typing import Optional

# ---
## 🔑 Schemas de Token (Autenticação)
# ---

class Token(BaseModel):
    """Schema para o token JWT retornado após o login."""
    access_token: str
    token_type: str = "bearer" # Padrão para autenticação JWT

class TokenData(BaseModel):
    """Schema para os dados (payload) contidos dentro do token JWT."""
    email: Optional[str] = None
    user_id: Optional[int] = None

    # Se você estivesse lendo o TokenData diretamente de um objeto ORM
    # (o que é incomum, mas possível), você adicionaria a Config:
    # class Config:
    #     from_attributes = True