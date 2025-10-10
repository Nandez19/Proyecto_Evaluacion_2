from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class bibliotecarioBase(BaseModel):

    Nombre: str
    Telefono: str
    Edad: str


class bibliotecarioCreate(bibliotecarioBase):

    pass

class bibliotecarioResponse(BaseModel):

    Cedula_bibliotecario: UUID
    Nombre: str
    Telefono: str
    Edad: str

    class Config:
        from_attributes = True