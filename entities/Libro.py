from database.conexion import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, Double, text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship


class Libro(Base):
    __tablename__ = "Libro"

    Codigo_Libro = Column(
    UNIQUEIDENTIFIER, primary_key=True, server_default=text("NEWID()"), index=True
)
    Titulo = Column(String, nullable=False)
    Año = Column(String,nullable=False)
    Precio = Column(Double,nullable=False)

    #FK
    Nit_Proveedor = Column(UNIQUEIDENTIFIER, ForeignKey("Proveedor.Nit_Proveedor"), nullable=False)
    Cedula_Autor = Column(UNIQUEIDENTIFIER, ForeignKey("Autor.Cedula_Autor"), nullable=False)
    Id_Editorial = Column(UNIQUEIDENTIFIER, ForeignKey("Editorial.Id_Editorial"), nullable=False)
    Id_Prestamo = Column(UNIQUEIDENTIFIER, ForeignKey("Prestamo.Id_Prestamo"), nullable=False)

    #Relaciones
    prestamo = relationship("Prestamo", back_populates="Libro")
    autor = relationship("Autor", back_populates="Libro")
    proveedor = relationship("Proveedor", back_populates="Libro")
    editorial = relationship("Editorial", back_populates="Libro")
