from database.conexion import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship


class Autor(Base):
    __tablename__ = "Autor"

    Cedula_Autor = Column(
    UNIQUEIDENTIFIER, primary_key=True, server_default=text("NEWID()"), index=True
)
    Nombre = Column(String, nullable=False)
    Telefono = Column(String,nullable=False)
    Edad = Column(String,nullable=False)

    #Relaciones
    libro = relationship("Libro", back_populates="Autor")
    