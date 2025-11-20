from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database.connection import Base
import json
from typing import List, Optional
from sqlalchemy.orm import relationship


class Usuario(Base):
    __tablename__ = "usuarios"
    
    # Identificação
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200), nullable=False)
    email = Column(String(200), unique=True, nullable=False, index=True)
    senha_hash = Column(String(200), nullable=False)
    
    # Contato
    telefone = Column(String(20))
    foto_perfil = Column(String(500))
    
    # Preferências (armazenadas como JSON string no banco)
    _preferencias_categorias = Column("preferencias_categorias", String(500))
    
    # Gamificação
    pontos_totais = Column(Integer, default=0)
    nivel = Column(Integer, default=1)
    
    # Status
    ativo = Column(Boolean, default=True)
    
    # Timestamps
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Property para converter string JSON ↔ lista
    @property
    def preferencias_categorias(self) -> Optional[List[str]]:
        """Retorna preferências como lista Python"""
        if not self._preferencias_categorias:
            return []
        
        try:
            # Tentar fazer parse do JSON
            return json.loads(self._preferencias_categorias)
        except (json.JSONDecodeError, TypeError):
            # Se não for JSON válido, tentar split por vírgula
            if isinstance(self._preferencias_categorias, str):
                return [cat.strip() for cat in self._preferencias_categorias.split(",") if cat.strip()]
            return []
    
    @preferencias_categorias.setter
    def preferencias_categorias(self, value: Optional[List[str]]):
        """Salva preferências como JSON string no banco"""
        if value:
            self._preferencias_categorias = json.dumps(value, ensure_ascii=False)
        else:
            self._preferencias_categorias = None

    # Adicionar esta linha:
    pontuacao = relationship("PontuacaoUsuario", back_populates="usuario", uselist=False)
    favoritos = relationship("Favorito", back_populates="usuario")