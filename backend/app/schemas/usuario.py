from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

## Schemas de Entrada (Input Schemas)

class UsuarioCreate(BaseModel):
    """Schema para criação de um novo usuário."""
    nome: str = Field(..., min_length=3, max_length=200)
    email: EmailStr
    senha: str = Field(..., min_length=6, max_length=100)
    telefone: Optional[str] = None
    preferencias_categorias: Optional[List[str]] = []

class UsuarioLogin(BaseModel):
    """Schema para login de usuário."""
    email: EmailStr
    senha: str

class UsuarioUpdate(BaseModel):
    """Schema para atualização de dados do usuário."""
    nome: Optional[str] = Field(None, min_length=3, max_length=200)
    telefone: Optional[str] = None
    foto_perfil: Optional[str] = None
    preferencias_categorias: Optional[List[str]] = None

##  Schemas de Saída (Output/Response Schemas)

class UsuarioResponse(BaseModel):
    """Schema de retorno completo do usuário."""
    id: int
    nome: str
    email: str
    telefone: Optional[str]
    foto_perfil: Optional[str]
    # O Pydantic irá serializar a lista de strings. Se no DB for uma string,
    # pode ser necessário ajustar a forma como você a carrega.
    preferencias_categorias: Optional[List[str]] 
    pontos_totais: int
    nivel: int
    criado_em: datetime

    class Config:
        # Permite mapear de um objeto ORM (como SQLAlchemy) para este schema.
        from_attributes = True

class UsuarioPublico(BaseModel):
    """Informações públicas do usuário (para rankings, etc)."""
    id: int
    nome: str
    foto_perfil: Optional[str]
    pontos_totais: int
    nivel: int

    class Config:
        # Permite mapear de um objeto ORM (como SQLAlchemy) para este schema.
        from_attributes = True