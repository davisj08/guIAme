from app.core.openai_client import get_openai_client
from app.core.config import settings

def chat(mensagem: str):
    """Envia uma mensagem para a IA e retorna a resposta"""
    print(f"\n��� Você: {mensagem}")
    
    try:
        client = get_openai_client()
        response = client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {
                    "role": "system", 
                    "content": "Você é um guia turístico especializado em Brasília. Seja amigável e informativo."
                },
                {
                    "role": "user", 
                    "content": mensagem
                }
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        resposta = response.choices[0].message.content
        print(f"��� IA: {resposta}")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

# Exemplos de uso
if __name__ == "__main__":
    print("=" * 60)
    print("��� TESTE DE CONVERSA COM IA - GUIA TURÍSTICO DE BRASÍLIA")
    print("=" * 60)
    
    # Teste 1: Saudação
    chat("Olá! Quem é você?")
    
    # Teste 2: Pergunta sobre Brasília
    chat("O que você pode me dizer sobre a Catedral de Brasília?")
    
    # Teste 3: Recomendação
    chat("Quais são os 3 melhores pontos turísticos para visitar em Brasília?")
    
    # Teste 4: Informação prática
    chat("Qual é o melhor horário para visitar a Torre de TV?")
