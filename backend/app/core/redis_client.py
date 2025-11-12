import redis
import json
from typing import List, Dict, Optional
from app.core.config import settings

# Cliente Redis global
redis_client = redis.from_url(settings.redis_url, decode_responses=True)

class ChatHistoryManager:
    """Gerenciador de histórico de conversas no Redis"""

    @staticmethod
    def _get_key(user_id: int) -> str:
        """Gera chave do Redis para o usuário"""
        return f"chat_history:user:{user_id}"

    @staticmethod
    def add_message(user_id: int, role: str, content: str):
        """Adiciona uma mensagem ao histórico"""
        key = ChatHistoryManager._get_key(user_id)
        message = {"role": role, "content": content}
        
        # Adicionar à lista
        redis_client.rpush(key, json.dumps(message))
        
        # Definir expiração (24 horas)
        redis_client.expire(key, settings.redis_ttl)

    @staticmethod
    def get_history(user_id: int, limit: int = 10) -> List[Dict[str, str]]:
        """Recupera o histórico de conversas"""
        key = ChatHistoryManager._get_key(user_id)
        
        # Pegar últimas N mensagens
        messages = redis_client.lrange(key, -limit, -1)
        
        return [json.loads(msg) for msg in messages]

    @staticmethod
    def clear_history(user_id: int):
        """Limpa o histórico de conversas"""
        key = ChatHistoryManager._get_key(user_id)
        redis_client.delete(key)

    @staticmethod
    def get_history_size(user_id: int) -> int:
        """Retorna o tamanho do histórico"""
        key = ChatHistoryManager._get_key(user_id)
        return redis_client.llen(key)