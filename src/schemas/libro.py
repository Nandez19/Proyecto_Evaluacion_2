from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class libroBase(BaseModel):
    Titulo: str
    Año: str
    Precio: float

class libroCreate(libroBase):
    pass

class libroResponse(BaseModel):
    Codigo_Libro: UUID
    Titulo: str
    Año: str
    Precio: float

    class Config:
        from_attributes = True