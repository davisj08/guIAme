from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship  # ← NOVO
from app.database.connection import Base


class PontoTuristico(Base):
    __tablename__ = "pontos_turisticos"
    
    # Chave primária (OBRIGATÓRIA!)
    id = Column(Integer, primary_key=True, index=True)
    
    # Informações básicas
    nome = Column(String(200), nullable=False)
    descricao = Column(Text)
    categoria = Column(String(100))
    
    # Localização
    latitude = Column(Float)
    longitude = Column(Float)
    endereco = Column(String(300))
    
    # Contato e informações
    horario_funcionamento = Column(String(200))
    telefone = Column(String(20))
    site = Column(String(200))
    imagem_url = Column(String(500))
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos  ← NOVO
    favoritos = relationship("Favorito", back_populates="ponto_turistico")
