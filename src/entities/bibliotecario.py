import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from Database.conexion import Base


class Bibliotecario(Base):

    """
    Modelo de bibliotecario
    """

    __tablename__ = "Bibliotecarios"

    Id_Bibliotecario = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Cedula_Bibliotecario = Column(String, unique=True, index=True)
    Nombre = Column(String, index=True)
    Telefono = Column(String,index=True)
    Edad = Column(String,index=True)

    # Campos de auditoría
    Id_usuario_creacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
    Id_usuario_actualizacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
    Fecha_creacion = Column(DateTime, index=True)
    Fecha_actualizacion = Column(DateTime, index=True)

    #Relaciones

    Prestamo = relationship("Prestamos", back_populates="Bibliotecario")
 