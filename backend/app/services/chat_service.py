from typing import List, Dict
from app.core.openai_client import get_openai_client
from app.core.redis_client import ChatHistoryManager
from app.core.config import settings

class ChatService:
    """Serviço para gerenciar o chatbot com IA"""

    # Prompt do sistema para contextualizar o chatbot
    SYSTEM_PROMPT = """Você é um guia turístico virtual especializado em
Brasília, a capital do Brasil.
Seu papel é:
- Fornecer informações precisas e interessantes sobre pontos turísticos de Brasília
- Sugerir roteiros personalizados baseados nos interesses do turista
- Explicar a história e arquitetura da cidade
- Recomendar restaurantes, hotéis e atividades
- Ser amigável, prestativo e entusiasta
Características de Brasília que você deve conhecer:
- Capital federal do Brasil, inaugurada em 1960
- Projetada por Lúcio Costa e Oscar Niemeyer
- Patrimônio Mundial da UNESCO
- Arquitetura modernista única
- Principais pontos: Catedral, Congresso Nacional, Palácio da Alvorada, Ponte JK
- Localizada no Planalto Central
Sempre responda em português brasileiro de forma clara e objetiva."""

    @staticmethod
    def _build_messages(user_id: int, user_message: str, include_context: bool = True) -> List[Dict[str, str]]:
        """Constrói a lista de mensagens para enviar ao GPT"""
        messages = []

        # Adicionar prompt do sistema
        if include_context:
            messages.append({
                "role": "system",
                "content": ChatService.SYSTEM_PROMPT
            })

        # Recuperar histórico do Redis
        history = ChatHistoryManager.get_history(user_id, limit=10)
        messages.extend(history)

        # Adicionar mensagem atual do usuário
        messages.append({
            "role": "user",
            "content": user_message
        })
        
        return messages

    @staticmethod
    def get_chat_response(user_id: int, user_message: str, include_context: bool = True) -> str:
        """Obtém resposta do chatbot usando GPT"""
        try:
            client = get_openai_client()
            
            # Construir mensagens
            messages = ChatService._build_messages(user_id, user_message, include_context)
            
            # Chamar API da OpenAI
            response = client.chat.completions.create(
                model=settings.openai_model,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            # Extrair resposta
            assistant_message = response.choices[0].message.content.strip()
            
            # Salvar no histórico
            ChatHistoryManager.add_message(user_id, "user", user_message)
            ChatHistoryManager.add_message(user_id, "assistant", assistant_message)
            
            return assistant_message
        
        except Exception as e:
            print(f"Erro ao chamar OpenAI: {e}")
            return "Desculpe, estou com dificuldades técnicas no momento. Por favor, tente novamente em instantes."

    @staticmethod
    def get_history(user_id: int) -> List[Dict[str, str]]:
        """Recupera histórico de conversas"""
        return ChatHistoryManager.get_history(user_id, limit=50)

    @staticmethod
    def clear_history(user_id: int):
        """Limpa histórico de conversas"""
        ChatHistoryManager.clear_history(user_id)