from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class PrestamoBase(BaseModel):

    Fecha_Prestamo: datetime
    Fecha_Devolucion: Optional[datetime] = None
    Estado: str
    Id_Bibliotecario: UUID
    Id_Cliente: UUID
    Id_Libro: UUID

class PrestamoCreate(PrestamoBase):

    pass

class PrestamoResponse(PrestamoBase):

    Id_Prestamo: UUID
    Id_usuario_creacion: Optional[UUID] = None
    Id_usuario_actualizacion: Optional[UUID] = None
    Fecha_creacion: Optional[datetime] = None
    Fecha_actualizacion: Optional[datetime] = None
    class Config:
        from_attributes = True