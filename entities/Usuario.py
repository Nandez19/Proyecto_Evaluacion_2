from database.conexion import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = "Usuario"

    Cedula_Usuario = Column(
    UNIQUEIDENTIFIER, primary_key=True, server_default=text("NEWID()"), index=True
)
    Nombre = Column(String, nullable=False)
    Telefono = Column(String,nullable=False)
    Correo = Column(String,nullable=False)

    #Relaciones
    prestamo = relationship("Prestamo", back_populates="Usuario")