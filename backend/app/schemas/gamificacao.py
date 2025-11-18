from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# ---

class PontuacaoResponse(BaseModel):
    """Schema de resposta para a pontuação e progresso do usuário."""
    pontos_totais: int
    nivel: str
    visitas_realizadas: int
    avaliacoes_feitas: int

    class Config:
        # Permite que o Pydantic seja construído a partir de objetos SQLAlchemy
        from_attributes = True

# ---

class BadgeResponse(BaseModel):
    """Schema de resposta para uma badge (conquista) específica."""
    id: int
    nome: str
    descricao: Optional[str] = None
    icone: Optional[str] = None
    pontos_necessarios: int

    class Config:
        from_attributes = True

# ---

class UsuarioBadgeResponse(BaseModel):
    """
    Schema de resposta para uma badge conquistada por um usuário.
    Inclui o detalhe da badge (BadgeResponse) e a data da conquista.
    """
    badge: BadgeResponse
    conquistado_em: datetime

    class Config:
        from_attributes = True

# ---

class RankingItemResponse(BaseModel):
    """
    Schema de resposta para um item individual dentro da lista de ranking.
    Representa a posição e detalhes de um único usuário.
    """
    posicao: int
    usuario_nome: str
    pontos_totais: int
    nivel: str
    visitas_realizadas: int
    
    class Config:
        from_attributes = True

# ---

class RankingResponse(BaseModel):
    """
    Schema de resposta para a lista completa de ranking.
    (Sugestão: É mais comum usar uma lista de RankingItemResponse para o ranking completo).
    """
    # Se você for usar este nome (RankingResponse) para a lista de itens,
    # pode ser útil reestruturar para: ranking: List[RankingItemResponse]
    ranking: List[RankingItemResponse]

    class Config:
        from_attributes = True

# ---

class MinhaPosicaoResponse(BaseModel):
    """
    Schema de resposta para a posição, pontuação e nível do usuário
    atual dentro do ranking.
    """
    posicao: Optional[int] = None  # Pode ser None se o usuário não estiver no top N
    total_usuarios: int
    pontos: int
    nivel: str

    class Config:
        from_attributes = True