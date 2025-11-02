from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

## 📝 Schemas de Entrada (Input Schemas)

class PontoTuristicoCreate(BaseModel):
    """Schema para criar um novo ponto turístico."""
    nome: str = Field(..., min_length=3, max_length=200)
    descricao: str = Field(..., min_length=10)
    descricao_curta: Optional[str] = Field(None, max_length=500)
    categoria: str
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    endereco: Optional[str] = None
    horario_funcionamento: Optional[str] = None
    telefone: Optional[str] = None
    site: Optional[str] = None
    preco_entrada: Optional[str] = None
    imagem_principal: Optional[str] = None

class PontoTuristicoUpdate(BaseModel):
    """Schema para atualizar dados de um ponto turístico."""
    nome: Optional[str] = Field(None, min_length=3, max_length=200)
    descricao: Optional[str] = Field(None, min_length=10)
    descricao_curta: Optional[str] = Field(None, max_length=500)
    categoria: Optional[str] = None
    horario_funcionamento: Optional[str] = None
    telefone: Optional[str] = None
    site: Optional[str] = None
    preco_entrada: Optional[str] = None
    imagem_principal: Optional[str] = None

## 🌟 Schemas de Saída (Output/Response Schemas)

class PontoTuristicoResponse(BaseModel):
    """Schema de retorno completo do ponto turístico."""
    id: int
    nome: str
    descricao: str
    descricao_curta: Optional[str]
    categoria: str
    latitude: float
    longitude: float
    endereco: Optional[str]
    horario_funcionamento: Optional[str]
    telefone: Optional[str]
    site: Optional[str]
    preco_entrada: Optional[str]
    imagem_principal: Optional[str]
    total_visitas: int
    media_avaliacoes: float
    total_avaliacoes: int
    criado_em: datetime

    class Config:
        # CORREÇÃO: Indentado para dentro da classe PontoTuristicoResponse
        from_attributes = True

class PontoTuristicoLista(BaseModel):
    """Versão simplificada para listagens."""
    id: int
    nome: str
    descricao_curta: Optional[str]
    categoria: str
    latitude: float
    longitude: float
    imagem_principal: Optional[str]
    media_avaliacoes: float
    total_avaliacoes: int

    class Config:
        # CORREÇÃO: Indentado para dentro da classe PontoTuristicoLista
        from_attributes = True