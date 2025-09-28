from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class prestamoBase(BaseModel):

    Fecha_Prestamo: datetime
    Fecha_Devolucion: datetime
    Estado: str


class prestamoCreate(prestamoBase):

    pass

class prestamoResponse(BaseModel):

    Id_Prestamo: UUID
    Fecha_Prestamo: datetime
    Fecha_Devolucion: datetime
    Estado: str

    class Config:
        from_attributes = True

