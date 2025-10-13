from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class ClienteBase(BaseModel):
    Cedula_Cliente: str
    Nombre: str
    Telefono: Optional[str] = None
    Correo: str

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    Id_Cliente: UUID
    Id_usuario_creacion: Optional[UUID] = None
    Id_usuario_actualizacion: Optional[UUID] = None
    Fecha_creacion: Optional[datetime] = None
    Fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True