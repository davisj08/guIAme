from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ChatMessage(BaseModel):
    """Mensagem individual do chat"""
    role: str = Field(..., description="user ou assistant")
    content: str = Field(..., description="Conteúdo da mensagem")
    timestamp: Optional[datetime] = None

class ChatRequest(BaseModel):
    """Requisição para o chatbot"""
    message: str = Field(..., min_length=1, max_length=1000,
                         description="Mensagem do usuário")
    include_context: bool = Field(True, description="Incluir contexto de Brasília")

class ChatResponse(BaseModel):
    """Resposta do chatbot"""
    message: str = Field(..., description="Resposta do assistente")
    conversation_id: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class ChatHistoryResponse(BaseModel):
    """Histórico de conversas"""
    messages: List[ChatMessage]
    total_messages: int