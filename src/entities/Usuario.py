import uuid
from sqlalchemy import Column, Date, DateTime, ForeignKey, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from Database.conexion import Base
from datetime import datetime


class Usuario(Base):
    __tablename__ = "Usuarios"

    Cedula_Usuario = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Nombre = Column(String, index=True, nullable=False)
    Telefono = Column(String)
    Correo = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    Rol = Column(String, default="usuario")

    # Auditoría
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

