from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class AutorBase(BaseModel):

    Nombre: str
    Telefono: str
    Edad: str


class AutorCreate(AutorBase):

    pass

class AutorResponse(BaseModel):

    Cedula_Autor: UUID
    Nombre: str
    Telefono: str
    Edad: str

    class Config:
        from_attributes = True

   