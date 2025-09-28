"""
Pydantic schemas for Factura entity.
"""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Usuario(BaseModel):
    """Base schema for Usuario with common fields."""

    idUsuario: UUID
    idCita: UUID
    monto: float
    descripcion: str
    fechaEmision: datetime
    estado: str = "pendiente"


class FacturaCreate(FacturaBase):
    """Schema for creating a new Factura."""

    pass


class FacturaResponse(FacturaBase):
    """Schema for Factura response."""

    idFactura: UUID
    id_usuario_creacion: Optional[UUID] = None
    id_usuario_actualizacion: Optional[UUID] = None
    fecha_creacion: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True