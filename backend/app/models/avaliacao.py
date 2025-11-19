from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
# Assumindo que 'Base' e o caminho de importação estão corretos
from app.database.connection import Base


# --- Modelo de Avaliação (Review) ---
class Avaliacao(Base):
    """Modelo para avaliações de pontos turísticos (1-5 estrelas)."""

    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    ponto_turistico_id = Column(Integer, ForeignKey("pontos_turisticos.id"), nullable=False)
    nota = Column(Integer, nullable=False)
    comentario = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Constraint para garantir nota entre 1 e 5
    __table_args__ = (
        CheckConstraint('nota >= 1 AND nota <= 5', name='check_nota_range'),
    )

    # Relacionamentos (configurados para as classes 'Usuario' e 'PontoTuristico')
    usuario = relationship("Usuario")
    ponto_turistico = relationship("PontoTuristico")

# --- Modelo de Visita (Check-in) ---
class Visita(Base):
    """Modelo para registrar visitas (check-in) em pontos turísticos."""

    __tablename__ = "visitas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    ponto_turistico_id = Column(Integer, ForeignKey("pontos_turisticos.id"), nullable=False)
    data_visita = Column(DateTime, default=datetime.utcnow)
    comentario = Column(Text)  # Comentário opcional sobre a visita
    latitude = Column(Float)  # Localização do check-in (opcional)
    longitude = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relacionamentos (configurados para as classes 'Usuario' e 'PontoTuristico')
    usuario = relationship("Usuario")
    ponto_turistico = relationship("PontoTuristico")