from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, List

# Define um TypeVar para que os modelos genéricos possam aceitar qualquer tipo de dado (T)
T = TypeVar('T')

# ---
## 📤 Schemas de Resposta Padrão da API
# ---

class ResponseModel(BaseModel, Generic[T]):
    """Modelo de resposta padrão da API (sucesso)."""
    success: bool = True
    message: Optional[str] = None
    data: Optional[T] = None # Onde o dado específico (usuário, ponto, etc.) vai

class PaginatedResponse(BaseModel, Generic[T]):
    """Modelo de resposta para listas de dados paginadas."""
    items: List[T] # A lista de itens no tipo T
    total: int     # O número total de itens disponíveis
    page: int      # A página atual
    page_size: int # O tamanho da página
    total_pages: int # O número total de páginas

class ErrorResponse(BaseModel):
    """Modelo de resposta de erro padrão da API."""
    success: bool = False
    message: str
    error_code: Optional[str] = None
    details: Optional[dict] = None