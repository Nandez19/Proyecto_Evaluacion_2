from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from sqlalchemy import Double


class libroBase(BaseModel):

    Titulo: str
    Año: str
    Precio: Double


class libroCreate(libroBase):

    pass

class libroResponse(BaseModel):

    Codigo_Libro: UUID
    Titulo: str
    Año: str
    Precio: Double

    class Config:
        from_attributes = True

