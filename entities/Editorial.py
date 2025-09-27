from database.conexion import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship


class Editorial(Base):
    __tablename__ = "Editorial"

    Id_Editorial = Column(
    UNIQUEIDENTIFIER, primary_key=True, server_default=text("NEWID()"), index=True
)
    Nombre = Column(String, nullable=False)
    Pais = Column(String, nullable=False)
    Contacto = Column(String, nullable=False) 

    #Relaciones
    libro = relationship("Libro", back_populates="Editorial")

    