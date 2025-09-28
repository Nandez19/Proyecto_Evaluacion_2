import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from Database.conexion import Base


class Autor(Base):

    """
    Modelo de autor
    """

    __tablename__ = "Autores"

    Id_Autor = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Cedula_Autor= Column(String, index=True, nullable=False)
    Nombre = Column(String, index=True)
    Telefono = Column(String)
    Edad = Column(String)

    # Campos de auditoría
    Id_usuario_creacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
    Id_usuario_actualizacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
    Fecha_creacion = Column(DateTime, index=True)
    Fecha_actualizacion = Column(DateTime, index=True)

    # Relaciones
    libros = relationship("Libros", back_populates="Autores")  

