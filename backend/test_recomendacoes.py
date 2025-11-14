from app.services.recomendacao_service import RecomendacaoService
from app.database.connection import SessionLocal


def test_recomendacoes():
    """Teste do sistema de recomendações"""
    print("=" * 60)
    print("🧪 TESTE DO SISTEMA DE RECOMENDAÇÕES")
    print("=" * 60)

    # Inicializa a sessão do banco de dados
    db = SessionLocal()

    try:
        # Teste com usuário ID 1
        print("\n🔍 Gerando recomendações para usuário ID 1...")
        recomendacoes = RecomendacaoService.gerar_recomendacoes_ia(
            usuario_id=1,
            db=db,
            quantidade=5
        )

        print(f"\n✓ {len(recomendacoes)} recomendações geradas:\n")

        # Exibe os resultados
        for i, rec in enumerate(recomendacoes, 1):
            print(f"{i}. {rec['ponto']['nome']}")
            print(f"   Categoria: {rec['ponto']['categoria']}")
            print(f"   Motivo: {rec['motivo']}")
            print(f"   Relevância: {rec['relevancia']}%")
            print()

        print("=" * 60)
        print("✅ TESTE CONCLUÍDO!")
        print("=" * 60)

    finally:
        # Garante o fechamento da conexão com o banco de dados
        db.close()


if __name__ == "__main__":
    test_recomendacoes()