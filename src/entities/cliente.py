import uuid

from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from Database.conexion import Base
 
class Cliente(Base):
    """
    Modelo de cliente (quien realiza el prestamo)
    """
    __tablename__ = "Clientes"
    Id_Cliente = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Cedula_Cliente = Column(String, unique=True)
    Nombre = Column(String, index=True)
    Telefono = Column(String, index=True)
    Correo = Column(String, index=True, unique=True)


    # Campos de auditoría
    Id_usuario_creacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
    Id_usuario_actualizacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
    Fecha_creacion = Column(DateTime, index=True)
    Fecha_actualizacion = Column(DateTime, index=True)

     # Relaciones
    prestamos = relationship("Prestamo", back_populates="cliente")
