import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from Database.conexion import Base

class Prestamo(Base):

    """
    Modelo de prestamo
    """
    
    __tablename__ = "Prestamos"

    Id_Prestamo = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Fecha_Prestamo = Column(DateTime, index=True, nullable=False)
    Fecha_Devolucion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, index=True)
    Estado = Column(String, index=True)

    #FK
    Id_Bibliotecario = Column(UUID(as_uuid=True), ForeignKey("Bibliotecarios.Id_Bibliotecario"), index=True)
    Id_Usuario = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
   
   # Campos de auditoría
    Id_usuario_creacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
    Id_usuario_actualizacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), index=True)
    Fecha_creacion = Column(DateTime, index=True)
    Fecha_actualizacion = Column(DateTime, index=True)

    #Relaciones
    Bibliotecario = relationship("Bibliotecario", back_populates="Prestamo")
    Usuario = relationship("Usuario", back_populates="Prestamo")
    Libro = relationship("Libro", back_populates="Prestamo")