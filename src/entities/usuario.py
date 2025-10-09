import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.conexion import Base



class Usuario(Base):

    """
    Modelo de usuario
    """
    
    __tablename__ = "Usuarios"

    Id_Usuario = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Cedula_Usuario = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True)
    Nombre = Column(String, index=True, nullable=False)
    Telefono = Column(String)
    Correo = Column(String, unique=True, nullable=False)
    Password_Hash = Column(String, nullable=False)
    Rol = Column(String, default="usuario")

    # Campos de auditoría
    Id_usuario_creacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_usuario"), index=True)
    Id_usuario_actualizacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_usuario"), index=True)
    Fecha_creacion = Column(DateTime, index=True)
    Fecha_actualizacion = Column(DateTime, index=True)

    # Relaciones
    Prestamo = relationship("Prestamos", back_populates="Usuario")
