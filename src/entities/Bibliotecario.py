import uuid
from sqlalchemy import Column, Date, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from Database.conexion import Base


class Bibliotecarios(Base):
    __tablename__ = "Bibliotecarios"

    Cedula_Bibliotecario = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Nombre = Column(String, nullable=False)
    Telefono = Column(String,nullable=False)
    Edad = Column(String,nullable=False)

    #Relaciones
    auditoria = relationship("Auditoria", back_populates="Bibliotecario")
    prestamo = relationship("Prestamo", back_populates="Bibliotecario")
    