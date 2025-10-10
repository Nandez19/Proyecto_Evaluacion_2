from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class editorialBase(BaseModel):

    Nombre: str
    Pais: str
    Contacto: str


class editorialCreate(editorialBase):

    pass

class editorialResponse(BaseModel):

    Id_Editorial: UUID
    Nombre: str
    Pais: str
    Contacto: str

    class Config:
        from_attributes = True

