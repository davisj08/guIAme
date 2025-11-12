from openai import OpenAI
from app.core.config import settings

# Cliente OpenAI (compatível com DeepSeek)
client = OpenAI(
    api_key=settings.openai_api_key,
    base_url=settings.openai_base_url  # ← ADICIONAR!
)

def get_openai_client():
    """Retorna o cliente OpenAI configurado"""
    return client
