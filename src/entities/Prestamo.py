import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
<<<<<<< HEAD

from database.conexion import Base
=======
from Database.conexion import Base
from sqlalchemy.sql import func
>>>>>>> 26578a216dc9364a19d4f8e80fe1dbef1138837a

class Prestamo(Base):

    """
    Modelo de prestamo
    """
    
    __tablename__ = "Prestamos"

    Id_Prestamo = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Fecha_Prestamo = Column(DateTime, nullable=False)
    Fecha_Devolucion = Column(DateTime,nullable=False, server_default=func.now(), onupdate=func.now())
    Estado = Column(String, nullable=False)

    #FK
<<<<<<< HEAD
    Id_Bibliotecario = Column(UUID(as_uuid=True), ForeignKey("Bibliotecarios.Id_Bibliotecario"), nullable=False)
    Id_Usuario = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_Usuario"), nullable=False)
   
   # Campos de auditoría
    Id_usuario_creacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_usuario"), index=True)
    Id_usuario_actualizacion = Column(UUID(as_uuid=True), ForeignKey("Usuarios.Id_usuario"), index=True)
    Fecha_creacion = Column(DateTime, index=True)
    Fecha_actualizacion = Column(DateTime, index=True)

    #Relaciones
    Bibliotecario = relationship("Bibliotecario", back_populates="Prestamo")
    Usuario = relationship("Usuario", back_populates="Prestamo")
    Libro = relationship("Libro", back_populates="Prestamo")
=======
    Cedula_Bibliotecario = Column(UUID(as_uuid=True), ForeignKey("Bibliotecario.Cedula_Bibliotecario"), nullable=False)
    Cedula_Usuario = Column(UUID(as_uuid=True), ForeignKey("Usuario.Cedula_Usuario"), nullable=False)

    #Relaciones
    bibliotecario = relationship("Bibliotecarios", back_populates="Prestamos")
    usuario = relationship("Usuarios", back_populates="Prestamos")
    libro = relationship("Libros", back_populates="Prestamos")
>>>>>>> 26578a216dc9364a19d4f8e80fe1dbef1138837a
