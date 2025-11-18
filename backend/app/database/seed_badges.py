from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.gamificacao import Badge
from typing import List, Dict, Any

def seed_badges():
    """Popula o banco com badges/conquistas do sistema."""
    
    # Inicializa a sessão com o banco de dados
    db: Session = SessionLocal()

    badges: List[Dict[str, Any]] = [
        # --- Badges de Visitas por Quantidade ---
        {
            "nome": "Explorador Iniciante",
            "descricao": "Visitou seu primeiro ponto turístico em Brasília",
            "icone": "🎒",
            "criterio": "visitar_1_ponto",
            "pontos_necessarios": 10
        },
        {
            "nome": "Turista Curioso",
            "descricao": "Visitou 5 pontos turísticos diferentes",
            "icone": "🗺️",
            "criterio": "visitar_5_pontos",
            "pontos_necessarios": 50
        },
        {
            "nome": "Conhecedor de Brasília",
            "descricao": "Visitou 10 pontos turísticos",
            "icone": "🏆",
            "criterio": "visitar_10_pontos",
            "pontos_necessarios": 100
        },
        {
            "nome": "Mestre Explorador",
            "descricao": "Visitou 25 pontos turísticos - você conhece Brasília!",
            "icone": "👑",
            "criterio": "visitar_25_pontos",
            "pontos_necessarios": 250
        },
        {
            "nome": "Lenda de Brasília",
            "descricao": "Visitou 50 pontos turísticos - você é uma lenda!",
            "icone": "⭐",
            "criterio": "visitar_50_pontos",
            "pontos_necessarios": 500
        },

        # --- Badges de Visitas por Categoria ---
        {
            "nome": "Crítico Gastronômico",
            "descricao": "Visitou 5 restaurantes diferentes",
            "icone": "🍽️",
            "criterio": "visitar_5_gastronomia",
            "pontos_necessarios": 50
        },
        {
            "nome": "Amante da Cultura",
            "descricao": "Visitou 5 pontos culturais (museus, teatros, etc)",
            "icone": "🎭",
            "criterio": "visitar_5_cultura",
            "pontos_necessarios": 50
        },
        {
            "nome": "Arquiteto Aprendiz",
            "descricao": "Visitou 5 obras de arquitetura de Niemeyer",
            "icone": "🏛️",
            "criterio": "visitar_5_arquitetura",
            "pontos_necessarios": 50
        },
        {
            "nome": "Amigo da Natureza",
            "descricao": "Visitou 5 parques e áreas naturais",
            "icone": "🌳",
            "criterio": "visitar_5_natureza",
            "pontos_necessarios": 50
        },
        {
            "nome": "Noiteiro de Brasília",
            "descricao": "Visitou 5 bares e casas noturnas",
            "icone": "🌃",
            "criterio": "visitar_5_vida_noturna",
            "pontos_necessarios": 50
        },
        {
            "nome": "Comprador Profissional",
            "descricao": "Visitou 5 shoppings e feiras",
            "icone": "🛍️",
            "criterio": "visitar_5_compras",
            "pontos_necessarios": 50
        },

        # --- Badges de Avaliação ---
        {
            "nome": "Avaliador Iniciante",
            "descricao": "Fez sua primeira avaliação",
            "icone": "⭐",
            "criterio": "avaliar_1_vez",
            "pontos_necessarios": 5
        },
        {
            "nome": "Avaliador Ativo",
            "descricao": "Fez 10 avaliações de pontos turísticos",
            "icone": "🌟",
            "criterio": "avaliar_10_vezes",
            "pontos_necessarios": 100
        },
        {
            "nome": "Crítico Especialista",
            "descricao": "Fez 25 avaliações detalhadas",
            "icone": "💎",
            "criterio": "avaliar_25_vezes",
            "pontos_necessarios": 250
        },

        # --- Badges de Temporalidade e Sequência ---
        {
            "nome": "Madrugador",
            "descricao": "Visitou um ponto turístico antes das 8h da manhã",
            "icone": "🌅",
            "criterio": "visitar_antes_8h",
            "pontos_necessarios": 20
        },
        {
            "nome": "Explorador Noturno",
            "descricao": "Visitou um ponto turístico após as 22h",
            "icone": "🌙",
            "criterio": "visitar_depois_22h",
            "pontos_necessarios": 20
        },
        {
            "nome": "Fim de Semana Ativo",
            "descricao": "Visitou 5 pontos turísticos em finais de semana",
            "icone": "🎉",
            "criterio": "visitar_5_fim_semana",
            "pontos_necessarios": 50
        },
        {
            "nome": "Turista Dedicado",
            "descricao": "Visitou pontos turísticos por 7 dias seguidos",
            "icone": "🔥",
            "criterio": "visitar_7_dias_seguidos",
            "pontos_necessarios": 100
        }
    ]

    try:
        # Itera sobre os dados das badges para criar ou pular se já existirem
        for badge_data in badges:
            # Verifica se uma badge com o mesmo nome já existe no banco
            existing = db.query(Badge).filter(
                Badge.nome == badge_data["nome"]
            ).first()

            if not existing:
                # Cria e adiciona a nova badge ao banco
                badge = Badge(**badge_data)
                db.add(badge)
                print(f"✓ Badge criado: {badge_data['nome']} {badge_data['icone']}")
            else:
                print(f"⊘ Já existe: {badge_data['nome']}")
        
        # Confirma todas as transações de criação
        db.commit()
        
        # Feedback final
        print(f"\n✅ Seed de badges executado com sucesso!")
        print(f"✅ {len(badges)} badges processados (criados ou ignorados).")

    except Exception as e:
        # Em caso de erro, desfaz as alterações e loga o erro
        db.rollback()
        print(f"\n❌ Erro ao executar seed de badges: {e}")
        # Re-lança a exceção para que o chamador saiba que houve um problema
        raise
    finally:
        # Garante que a sessão é sempre fechada
        db.close()

if __name__ == "__main__":
    seed_badges()


