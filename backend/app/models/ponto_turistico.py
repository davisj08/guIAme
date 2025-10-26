from sqlalchemy import Column, Integer, String, Float
from app.database.connection import Base


class PontoTuristico(Base):
    __tablename__ = "pontos_turisticos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    categoria = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
