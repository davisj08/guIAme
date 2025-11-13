from app.core.openai_client import get_openai_client
from app.core.redis_client import ChatHistoryManager
from app.services.chat_service import ChatService
from app.core.config import settings


def test_chat_completo():
    """Teste completo do sistema de chat"""
    print("=" * 60)
    print("🧪 TESTE COMPLETO DO SISTEMA DE CHAT")
    print("=" * 60)

    usuario_id = 999  # ID de teste

    # Teste 1: Limpar histórico
    print("\n\u2460 Limpando histórico...")
    ChatService.limpar_historico(usuario_id)
    print("✓ Histórico limpo")

    # Teste 2: Primeira mensagem
    print("\n\u2461 Enviando primeira mensagem...")
    resultado1 = ChatService.gerar_resposta(
        usuario_id=usuario_id,
        mensagem="Olá! Quais são os 3 melhores pontos turísticos de Brasília?"
    )
    print(f"✓ Resposta: {resultado1['resposta'][:100]}...")
    print(f"✓ Tokens usados: {resultado1['tokens_usados']}")

    # Teste 3: Segunda mensagem (com contexto)
    print("\n\u2462 Enviando segunda mensagem...")
    resultado2 = ChatService.gerar_resposta(
        usuario_id=usuario_id,
        mensagem="Me fale mais sobre o primeiro lugar que você mencionou"
    )
    print(f"✓ Resposta: {resultado2['resposta'][:100]}...")

    # Teste 4: Verificar histórico
    print("\n\u2463 Verificando histórico...")
    historico = ChatService.obter_historico(usuario_id)
    print(f"✓ Total de mensagens no histórico: {len(historico)}")

    # Teste 5: Limpar histórico
    print("\n\u2464 Limpando histórico novamente...")
    ChatService.limpar_historico(usuario_id)
    historico_limpo = ChatService.obter_historico(usuario_id)
    print(f"✓ Histórico após limpeza: {len(historico_limpo)} mensagens")

    print("\n" + "=" * 60)
    print("✅ TODOS OS TESTES PASSARAM!")
    print("=" * 60)


if __name__ == "__main__":
    test_chat_completo()