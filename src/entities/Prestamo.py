import uuid
from sqlalchemy import Column, Date, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from Database.conexion import Base

class Prestamo(Base):
    __tablename__ = "Prestamos"

    Id_Prestamo = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Fecha_Prestamo = Column(DateTime, nullable=False)
    Fecha_Devolucion = Column(DateTime,nullable=False, server_default=func.now(), onupdate=func.now())
    Estado = Column(String, nullable=False)

    #FK
    Cedula_Bibliotecario = Column(UNIQUEIDENTIFIER, ForeignKey("Bibliotecario.Cedula_Bibliotecario"), nullable=False)
    Cedula_Usuario = Column(UNIQUEIDENTIFIER, ForeignKey("Usuario.Cedula_Usuario"), nullable=False)

    #Relaciones
    bibliotecario = relationship("Bibliotecario", back_populates="Prestamo")
    usuario = relationship("Usuario", back_populates="Prestamo")
    libro = relationship("Libro", back_populates="Prestamo")