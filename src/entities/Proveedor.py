from database.conexion import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship


class Proveedor(Base):
    __tablename__ = "Proveedor"

    Nit_Proveedor = Column(
    UNIQUEIDENTIFIER, primary_key=True, server_default=text("NEWID()"), index=True
)
    Nombre = Column(String, nullable=False)
    Direccion = Column(String,nullable=False)
    Telefono = Column(String,nullable=False)

    #Relaciones
    libro = relationship("Libro", back_populates="Proveedor")