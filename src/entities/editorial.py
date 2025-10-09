import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.conexion import Base


class Editorial(Base):

    """
    Modelo de editorial
    """

    __tablename__ = "Editoriales"

    Id_Editorial = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Nombre = Column(String, index=True, unique=True)
    Pais = Column(String, index=True)
    Contacto = Column(String, index=True) 

    # Campos de auditoría
    Id_usuario_creacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
    Id_usuario_actualizacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
    Fecha_creacion = Column(DateTime, index=True)
    Fecha_actualizacion = Column(DateTime, index=True)

    #Relaciones
    libro = relationship("Libros", back_populates="Editoriales")
