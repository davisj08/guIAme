from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ChatMessage(BaseModel):
    """Mensagem individual do chat"""
    role: str = Field(..., description="user ou assistant")
    content: str = Field(..., description="Conteúdo da mensagem")
    timestamp: Optional[datetime] = None

    class Config:
        from_attributes = True

class ChatRequest(BaseModel):
    """Requisição de chat"""
    mensagem: str = Field(..., min_length=1, max_length=1000, description="Mensagem do usuário")
    contexto: Optional[str] = Field(None, description="Contexto adicional (ex: ponto_turistico_id:1)")

class ChatResponse(BaseModel):
    """Resposta do chat"""
    resposta: str
    timestamp: datetime
    tokens_usados: Optional[int] = None

class ChatHistoryResponse(BaseModel):
    """Histórico de conversas"""
    mensagens: List[ChatMessage]
    total: int