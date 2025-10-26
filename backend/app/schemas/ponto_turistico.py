from pydantic import BaseModel
from typing import Optional


class PontoTuristicoBase(BaseModel):
    nome: str
    descricao: str
    categoria: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class PontoTuristicoCreate(PontoTuristicoBase):
    pass


class PontoTuristicoResponse(PontoTuristicoBase):
    id: int
    
    class Config:
        from_attributes = True
