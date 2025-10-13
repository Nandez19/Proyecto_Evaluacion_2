from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class AutorBase(BaseModel):

    # Id_Autor:Optional[str] = None
    Cedula_Autor: str
    Nombre: str
    Telefono: Optional[str] = None
    Edad: Optional[str] = None


class AutorCreate(AutorBase):

    pass


class AutorResponse(AutorBase):

    Id_usuario_creacion: Optional[UUID] = None
    Id_usuario_actualizacion: Optional[UUID] = None
    Fecha_creacion: Optional[datetime] = None
    Fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True
