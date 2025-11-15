from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class EditorialBase(BaseModel):

    # Id_Editorial:str
    Nombre: str
    Pais: Optional[str] = None
    Contacto: Optional[str] = None


class EditorialCreate(EditorialBase):

    pass


class EditorialResponse(EditorialBase):
    Id_Editorial: UUID  # ← AGREGAR ESTA LÍNEA
    Id_usuario_creacion: Optional[UUID] = None
    Id_usuario_actualizacion: Optional[UUID] = None
    Fecha_creacion: Optional[datetime] = None
    Fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True
