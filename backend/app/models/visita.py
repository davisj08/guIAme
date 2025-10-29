from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.connection import Base


class Visita(Base):
    __tablename__ = "visitas"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    ponto_turistico_id = Column(Integer, ForeignKey("pontos_turisticos.id"), nullable=False)
    data_visita = Column(DateTime(timezone=True), server_default=func.now())
    confirmada = Column(Boolean, default=False)
    
    # Relacionamentos
    # usuario = relationship("Usuario", back_populates="visitas")
    # ponto_turistico = relationship("PontoTuristico", back_populates="visitas")
