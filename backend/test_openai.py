from app.core.openai_client import get_openai_client
from app.core.redis_client import ChatHistoryManager
from app.core.config import settings

def test_openai():
    """Testa conexão com OpenAI"""
    print("Testando OpenAI...")
    try:
        client = get_openai_client()
        response = client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": "Diga olá!"}
            ],
            max_tokens=50
        )
        print(f"✓ OpenAI funcionando: {response.choices[0].message.content}")
    except Exception as e:
        print(f"✗ Erro no OpenAI: {e}")

def test_redis():
    """Testa conexão com Redis"""
    print("\nTestando Redis...")
    try:
        # Adiciona uma mensagem de teste
        ChatHistoryManager.add_message(999, "user", "Teste")
        
        # Recupera o histórico e verifica o tamanho
        history = ChatHistoryManager.get_history(999)
        print(f"✓ Redis funcionando: {len(history)} mensagens")
        
        # Limpa o histórico de teste
        ChatHistoryManager.clear_history(999)
    except Exception as e:
        print(f"✗ Erro no Redis: {e}")

if __name__ == "__main__":
    test_openai()
    test_redis()