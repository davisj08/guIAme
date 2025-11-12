from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ===========================
# 📝 Schemas de Entrada (Create/Update)
# ===========================

class PontoTuristicoCreate(BaseModel):
    """Schema para criar um novo ponto turístico."""
    nome: str = Field(..., min_length=3, max_length=200, description="Nome do ponto turístico")
    descricao: Optional[str] = Field(None, description="Descrição completa do ponto turístico")
    categoria: Optional[str] = Field(None, max_length=100, description="Categoria do ponto turístico")
    latitude: Optional[float] = Field(None, ge=-90, le=90, description="Latitude da localização")
    longitude: Optional[float] = Field(None, ge=-180, le=180, description="Longitude da localização")
    endereco: Optional[str] = Field(None, max_length=300, description="Endereço completo")
    horario_funcionamento: Optional[str] = Field(None, max_length=200, description="Horário de funcionamento")
    telefone: Optional[str] = Field(None, max_length=20, description="Telefone de contato")
    site: Optional[str] = Field(None, max_length=200, description="Site oficial")
    imagem_url: Optional[str] = Field(None, max_length=500, description="URL da imagem principal")


class PontoTuristicoUpdate(BaseModel):
    """Schema para atualizar dados de um ponto turístico."""
    nome: Optional[str] = Field(None, min_length=3, max_length=200)
    descricao: Optional[str] = None
    categoria: Optional[str] = Field(None, max_length=100)
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)
    endereco: Optional[str] = Field(None, max_length=300)
    horario_funcionamento: Optional[str] = Field(None, max_length=200)
    telefone: Optional[str] = Field(None, max_length=20)
    site: Optional[str] = Field(None, max_length=200)
    imagem_url: Optional[str] = Field(None, max_length=500)


# ===========================
# 🌟 Schemas de Saída (Response)
# ===========================

class PontoTuristicoResponse(BaseModel):
    """Schema de retorno completo do ponto turístico."""
    id: int
    nome: str
    descricao: Optional[str] = None
    categoria: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    endereco: Optional[str] = None
    horario_funcionamento: Optional[str] = None
    telefone: Optional[str] = None
    site: Optional[str] = None
    imagem_url: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class PontoTuristicoLista(BaseModel):
    """Versão simplificada para listagens."""
    id: int
    nome: str
    categoria: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    imagem_url: Optional[str] = None

    class Config:
        from_attributes = True


# ===========================
# 📄 Schema de Paginação
# ===========================

class PontoTuristicoPaginado(BaseModel):
    """Schema para resposta paginada de pontos turísticos."""
    items: list[PontoTuristicoResponse]
    total: int
    page: int
    page_size: int
    total_pages: int