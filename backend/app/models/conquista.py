from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database.connection import Base


class Conquista(Base):
    __tablename__ = "conquistas"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200), nullable=False)
    descricao = Column(Text)
    icone = Column(String(500))
    pontos_necessarios = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
