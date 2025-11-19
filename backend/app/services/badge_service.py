
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.gamificacao import Badge, UsuarioBadge, PontuacaoUsuario
from app.models.avaliacao import Avaliacao, Visita


def verificar_e_conceder_badges(usuario_id: int, db: Session) -> list:
    """
    Verifica critérios e concede badges automaticamente ao usuário.
    
    Args:
        usuario_id: ID do usuário
        db: Sessão do banco de dados
        
    Returns:
        Lista de badges recém-conquistadas
    """
    badges_conquistadas = []
    
    # Buscar pontuação do usuário
    pontuacao = db.query(PontuacaoUsuario).filter(
        PontuacaoUsuario.usuario_id == usuario_id
    ).first()
    
    if not pontuacao:
        return badges_conquistadas
    
    # Buscar todas as badges disponíveis
    todas_badges = db.query(Badge).all()
    
    # Buscar badges já conquistadas pelo usuário
    badges_ja_conquistadas = db.query(UsuarioBadge.badge_id).filter(
        UsuarioBadge.usuario_id == usuario_id
    ).all()
    badges_ja_conquistadas_ids = [b[0] for b in badges_ja_conquistadas]
    
    # Contar visitas e avaliações
    total_visitas = pontuacao.visitas_realizadas
    total_avaliacoes = pontuacao.avaliacoes_feitas
    total_pontos = pontuacao.pontos_totais
    
    # Contar avaliações 5 estrelas
    avaliacoes_5_estrelas = db.query(func.count(Avaliacao.id)).filter(
        Avaliacao.usuario_id == usuario_id,
        Avaliacao.nota == 5
    ).scalar()
    
    # Contar pontos turísticos únicos visitados
    pontos_unicos_visitados = db.query(
        func.count(func.distinct(Visita.ponto_turistico_id))
    ).filter(
        Visita.usuario_id == usuario_id
    ).scalar()
    
    # Verificar cada badge
    for badge in todas_badges:
        # Pular se já conquistou
        if badge.id in badges_ja_conquistadas_ids:
            continue
        
        conceder = False
        
        # Critérios baseados no nome da badge (AJUSTADO PARA BADGES DO BANCO)
        nome_lower = badge.nome.lower()
        
        # === BADGES DE VISITAS ===
        if "explorador iniciante" in nome_lower:
            conceder = total_visitas >= 1
        elif "turista curioso" in nome_lower:
            conceder = total_visitas >= 5
        elif "conhecedor de brasília" in nome_lower or "conhecedor de brasilia" in nome_lower:
            conceder = total_visitas >= 10
        elif "mestre explorador" in nome_lower:
            conceder = total_visitas >= 25
        elif "lenda de brasília" in nome_lower or "lenda de brasilia" in nome_lower:
            conceder = total_visitas >= 50
        
        # === BADGES DE AVALIAÇÕES ===
        elif "avaliador iniciante" in nome_lower:
            conceder = total_avaliacoes >= 1
        elif "avaliador ativo" in nome_lower:
            conceder = total_avaliacoes >= 10
        elif "crítico especialista" in nome_lower or "critico especialista" in nome_lower:
            conceder = total_avaliacoes >= 25
        
        # === BADGES POR CATEGORIA (requer contagem específica) ===
        elif "arquiteto aprendiz" in nome_lower:
            # Contar visitas em pontos de categoria "Arquitetura"
            visitas_arquitetura = db.query(func.count(Visita.id)).join(
                Visita.ponto_turistico
            ).filter(
                Visita.usuario_id == usuario_id,
                # Assumindo que existe um campo 'categoria' no modelo PontoTuristico
                # Se não existir, essa badge não será concedida
            ).scalar() or 0
            conceder = visitas_arquitetura >= 5
        
        elif "amigo da natureza" in nome_lower:
            # Contar visitas em parques
            conceder = False  # Implementar lógica de categoria quando disponível
        
        elif "crítico gastronômico" in nome_lower or "critico gastronomico" in nome_lower:
            # Contar visitas em restaurantes
            conceder = False  # Implementar lógica de categoria quando disponível
        
        elif "amante da cultura" in nome_lower:
            # Contar visitas em pontos culturais
            conceder = False  # Implementar lógica de categoria quando disponível
        
        elif "noiteiro de brasília" in nome_lower or "noiteiro de brasilia" in nome_lower:
            # Contar visitas em bares/casas noturnas
            conceder = False  # Implementar lógica de categoria quando disponível
        
        elif "comprador profissional" in nome_lower:
            # Contar visitas em shoppings/feiras
            conceder = False  # Implementar lógica de categoria quando disponível
        
        # === BADGES ESPECIAIS (baseadas em horário/sequência) ===
        elif "madrugador" in nome_lower:
            # Verificar se tem visita antes das 8h
            conceder = False  # Implementar lógica de horário quando necessário
        
        elif "explorador noturno" in nome_lower:
            # Verificar se tem visita após 22h
            conceder = False  # Implementar lógica de horário quando necessário
        
        elif "fim de semana ativo" in nome_lower:
            # Verificar visitas em finais de semana
            conceder = False  # Implementar lógica de dia da semana quando necessário
        
        elif "turista dedicado" in nome_lower:
            # Verificar visitas em 7 dias seguidos
            conceder = False  # Implementar lógica de sequência quando necessário
        
        # Conceder badge se critério foi atendido
        if conceder:
            nova_badge = UsuarioBadge(
                usuario_id=usuario_id,
                badge_id=badge.id,
                conquistado_em=datetime.utcnow()
            )
            db.add(nova_badge)
            badges_conquistadas.append(badge)
    
    # Salvar no banco
    if badges_conquistadas:
        db.commit()
    
    return badges_conquistadas