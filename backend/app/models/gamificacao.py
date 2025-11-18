from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database.connection import Base
from datetime import datetime

# ---

class PontuacaoUsuario(Base):
    """
    Modelo para armazenar a pontuação e progresso do usuário.
    Possui relacionamento 'um-para-um' com a tabela 'usuarios'.
    """
    __tablename__ = "pontuacoes_usuarios"

    # Colunas principais
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), unique=True)
    pontos_totais = Column(Integer, default=0)
    nivel = Column(String(50), default="Bronze")  # Bronze, Prata, Ouro, Platina

    # Progresso/Atividades
    visitas_realizadas = Column(Integer, default=0)
    avaliacoes_feitas = Column(Integer, default=0)

    # Datas de registro/atualização
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relacionamento
    usuario = relationship("Usuario", back_populates="pontuacao")

# ---

class Badge(Base):
    """
    Modelo para badges/conquistas do sistema.
    Define as características de cada conquista disponível.
    """
    __tablename__ = "badges"

    # Colunas principais
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False, unique=True)
    descricao = Column(String(300))
    icone = Column(String(100))  # emoji ou URL de ícone
    criterio = Column(String(200))  # ex: "visitar_5_pontos", "avaliar_10_vezes"
    pontos_necessarios = Column(Integer, default=0)

    # Data de criação
    created_at = Column(DateTime, default=datetime.utcnow)

# ---

class UsuarioBadge(Base):
    """Modelo para relacionar usuários com badges conquistadas"""
    __tablename__ = "usuarios_badges"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    badge_id = Column(Integer, ForeignKey("badges.id"))
    conquistado_em = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    usuario = relationship("Usuario")
    badge = relationship("Badge")
