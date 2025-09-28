from database.conexion import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Prestamo(Base):
    __tablename__ = "Prestamo"

    Id_Prestamo = Column(
    UNIQUEIDENTIFIER, primary_key=True, server_default=text("NEWID()"), index=True
)
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