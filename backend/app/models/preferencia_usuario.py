from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.connection import Base


class PreferenciaUsuario(Base):
    """
    Define o modelo de persistência para as preferências de um usuário,
    utilizado para personalizar a experiência.
    """
    __tablename__ = "preferencias_usuarios"

    # Identificadores
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    # Preferências de Conteúdo
    # Armazenado como JSON string (ex: ["Arquitetura", "Natureza"])
    categorias_favoritas = Column(String(500))
    # Armazenado como JSON string (ex: ["Cultural", "Aventura"])
    tipos_atividade = Column(String(500))

    # Níveis de Interesse (Escala 1-10)
    nivel_interesse_historia = Column(Integer, default=5)
    nivel_interesse_natureza = Column(Integer, default=5)
    nivel_interesse_gastronomia = Column(Integer, default=5)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())