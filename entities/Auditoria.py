from database.conexion import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Auditoria(Base):
    __tablename__ = "Auditoria"

    Id_Auditoria = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("NEWID()"), index=True)
    Fecha_Creacion = Column(DateTime, nullable=False, server_default=func.now())
    Fecha_Actualizacion = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    Accion = Column(String(50), nullable=False)  

    #FK
    Cedula_Bibliotecario = Column(UNIQUEIDENTIFIER, ForeignKey("Bibliotecario.Cedula_Bibliotecario"), nullable=False)

    #Relaciones
    bibliotecario = relationship("Bibliotecario", back_populates="Auditoria")