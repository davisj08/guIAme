from app.core.openai_client import get_openai_client
from app.core.redis_client import ChatHistoryManager
from app.core.config import settings
from sqlalchemy.orm import Session
from app.models.ponto_turistico import PontoTuristico
from typing import List, Dict
from datetime import datetime

class ChatService:
    @staticmethod
    def gerar_resposta(
        usuario_id: int,
        mensagem: str,
        contexto: str = None,
        db: Session = None
    ) -> Dict:
        """Gera resposta da IA com contexto"""
        
        # 1. Buscar histórico do Redis
        historico = ChatHistoryManager.get_history(usuario_id)
        
        # 2. Preparar mensagens
        mensagens = [
            {
                "role": "system",
                "content": """Você é um guia turístico especializado em Brasília. 
                Seja amigável, informativo e responda em português brasileiro.
                Forneça informações práticas como horários, preços e dicas de visitação.
                Se não souber algo, seja honesto e sugira onde o usuário pode obter mais informações."""
            }
        ]
        
        # 3. Adicionar contexto se houver
        if contexto and db:
            contexto_info = ChatService._buscar_contexto(contexto, db)
            if contexto_info:
                mensagens[0]["content"] += f"\n\nContexto adicional: {contexto_info}"
        
        # 4. Adicionar histórico (últimas 10 mensagens)
        mensagens.extend(historico[-10:])
        
        # 5. Adicionar mensagem atual
        mensagens.append({"role": "user", "content": mensagem})
        
        # 6. Chamar IA (Groq)
        try:
            client = get_openai_client()
            response = client.chat.completions.create(
                model=settings.openai_model,
                messages=mensagens,
                max_tokens=500,
                temperature=0.7
            )
            
            resposta = response.choices[0].message.content
            tokens = response.usage.total_tokens
            
            # 7. Salvar no histórico
            ChatHistoryManager.add_message(usuario_id, "user", mensagem)
            ChatHistoryManager.add_message(usuario_id, "assistant", resposta)
            
            return {
                "resposta": resposta,
                "tokens_usados": tokens
            }
        
        except Exception as e:
            raise Exception(f"Erro ao gerar resposta: {str(e)}")
    
    @staticmethod
    def _buscar_contexto(contexto: str, db: Session) -> str:
        """Busca informações de contexto no banco"""
        try:
            if contexto.startswith("ponto_turistico_id:"):
                ponto_id = int(contexto.split(":")[1])
                ponto = db.query(PontoTuristico).filter(
                    PontoTuristico.id == ponto_id
                ).first()
                
                if ponto:
                    return f"""Informações sobre {ponto.nome}:
                    - Descrição: {ponto.descricao}
                    - Categoria: {ponto.categoria}
                    - Endereço: {ponto.endereco}
                    - Horário: {ponto.horario_funcionamento}
                    - Telefone: {ponto.telefone}
                    """
        except:
            pass
        
        return ""
    
    @staticmethod
    def limpar_historico(usuario_id: int):
        """Limpa histórico de chat do usuário"""
        ChatHistoryManager.clear_history(usuario_id)
    
    @staticmethod
    def obter_historico(usuario_id: int) -> List[Dict]:
        """Retorna histórico de chat do usuário"""
        return ChatHistoryManager.get_history(usuario_id)