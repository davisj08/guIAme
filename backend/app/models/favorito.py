from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.connection import Base


class Favorito(Base):
    """
    Modelo para armazenar pontos turísticos favoritos dos usuários.
    Relacionamento muitos-para-muitos entre Usuario e PontoTuristico.
    """
    __tablename__ = "favoritos"

    # Colunas principais
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    ponto_turistico_id = Column(Integer, ForeignKey("pontos_turisticos.id"), nullable=False)
    
    # Data de criação
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relacionamentos
    usuario = relationship("Usuario", back_populates="favoritos")
    ponto_turistico = relationship("PontoTuristico", back_populates="favoritos")

    # Constraint: Um usuário não pode favoritar o mesmo ponto duas vezes
    __table_args__ = (
        UniqueConstraint('usuario_id', 'ponto_turistico_id', name='uq_usuario_ponto'),
    )
