import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String, Double
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from Database.conexion import Base

class Libro(Base):

    """
    Modelo de libro
    """
    
    __tablename__ = "Libros"

    Id_Libro = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Codigo_Libro= Column(String, index=True, unique=True)
    Titulo = Column(String, index=True)
    Año = Column(String,index=True)
    Precio = Column(Double,index=True)

    #Fk
    Id_Autor = Column(UUID(as_uuid=True), ForeignKey("Autores.Id_Autor"), index=True)
    Id_Editorial = Column(UUID(as_uuid=True), ForeignKey("Editoriales.Id_Editorial"), index=True)
    Id_Prestamo = Column(UUID(as_uuid=True), ForeignKey("Prestamos.Id_Prestamo"), index=True)

    # Campos de auditoría
    Id_usuario_creacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
    Id_usuario_actualizacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
    Fecha_creacion = Column(DateTime, index=True)
    Fecha_actualizacion = Column(DateTime, index=True)

    # Relaciones
    autor = relationship("Autor", back_populates="libros")
    editorial = relationship("Editorial", back_populates="libros")
    prestamos = relationship("Prestamo", back_populates="libro")
