from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.connection import Base


class Avaliacao(Base):
    __tablename__ = "avaliacoes"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    ponto_turistico_id = Column(Integer, ForeignKey("pontos_turisticos.id"), nullable=False)
    nota = Column(Integer, nullable=False)  # 1 a 5
    comentario = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relacionamentos
    # usuario = relationship("Usuario", back_populates="avaliacoes")
    # ponto_turistico = relationship("PontoTuristico", back_populates="avaliacoes")
