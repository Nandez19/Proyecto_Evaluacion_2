from database.conexion import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship


class Bibliotecarios(Base):
    __tablename__ = "Bibliotecario"

    Cedula_Bibliotecario = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("NEWID()"), index=True)
    Nombre = Column(String, nullable=False)
    Telefono = Column(String,nullable=False)
    Edad = Column(String,nullable=False)

    #Relaciones
    auditoria = relationship("Auditoria", back_populates="Bibliotecario")
    prestamo = relationship("Prestamo", back_populates="Bibliotecario")
    