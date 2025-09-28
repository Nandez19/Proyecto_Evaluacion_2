import uuid
from sqlalchemy import Column, Date, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from Database.conexion import Base
from sqlalchemy.sql import func

class Prestamo(Base):
    __tablename__ = "Prestamos"

    Id_Prestamo = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Fecha_Prestamo = Column(DateTime, nullable=False)
    Fecha_Devolucion = Column(DateTime,nullable=False, server_default=func.now(), onupdate=func.now())
    Estado = Column(String, nullable=False)

    #FK
    Cedula_Bibliotecario = Column(UUID(as_uuid=True), ForeignKey("Bibliotecario.Cedula_Bibliotecario"), nullable=False)
    Cedula_Usuario = Column(UUID(as_uuid=True), ForeignKey("Usuario.Cedula_Usuario"), nullable=False)

    #Relaciones
    bibliotecario = relationship("Bibliotecarios", back_populates="Prestamos")
    usuario = relationship("Usuarios", back_populates="Prestamos")
    libro = relationship("Libros", back_populates="Prestamos")