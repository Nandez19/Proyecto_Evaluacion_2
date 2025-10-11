from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class LibroBase(BaseModel):

    Codigo_Libro: str
    Titulo: str
    Año:Optional[str] = None
    Precio: Optional[float] = None
    Id_Autor: UUID
    Id_Editorial: UUID
    Id_Prestamo: UUID

class LibroCreate(LibroBase):
    pass

class LibroResponse(LibroBase):

    Id_Libro: UUID
    Id_usuario_creacion: Optional[UUID] = None
    Id_usuario_actualizacion: Optional[UUID] = None
    Fecha_creacion: Optional[datetime] = None
    Fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True