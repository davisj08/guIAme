from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.core.security import get_current_active_user
from app.models.usuario import Usuario
from app.schemas.chat import ChatRequest, ChatResponse, ChatHistoryResponse, ChatMessage
from app.services.chat_service import ChatService
from datetime import datetime

router = APIRouter()

@router.post("/chat", response_model=ChatResponse, summary="Enviar Mensagem para IA")
def enviar_mensagem(
    request: ChatRequest,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Envia uma mensagem para a IA e retorna a resposta.
    
    - **mensagem**: Texto da mensagem do usuário
    - **contexto**: (Opcional) Contexto adicional como "ponto_turistico_id:1"
    """
    try:
        resultado = ChatService.gerar_resposta(  # ✅ MÉTODO CORRETO!
            usuario_id=current_user.id,
            mensagem=request.mensagem,
            contexto=request.contexto,
            db=db
        )
        
        return ChatResponse(
            resposta=resultado["resposta"],
            timestamp=datetime.now(),
            tokens_usados=resultado.get("tokens_usados")
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao processar mensagem: {str(e)}"
        )

@router.get("/chat/historico", response_model=ChatHistoryResponse, summary="Obter Histórico de Chat")
def obter_historico(
    current_user: Usuario = Depends(get_current_active_user)
):
    """
    Retorna o histórico de conversas do usuário autenticado.
    """
    try:
        historico = ChatService.obter_historico(current_user.id)
        
        mensagens = [
            ChatMessage(
                role=msg["role"],
                content=msg["content"],
                timestamp=datetime.now()
            )
            for msg in historico
        ]
        
        return ChatHistoryResponse(
            mensagens=mensagens,
            total=len(mensagens)
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao obter histórico: {str(e)}"
        )

@router.delete("/chat/historico", summary="Limpar Histórico de Chat")
def limpar_historico(
    current_user: Usuario = Depends(get_current_active_user)
):
    """
    Limpa todo o histórico de conversas do usuário autenticado.
    """
    try:
        ChatService.limpar_historico(current_user.id)
        return {"message": "Histórico limpo com sucesso"}
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao limpar histórico: {str(e)}"
        )
