import uuid
from database.conexion import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Autor(Base):
    __tablename__ = "Autores"

    Id_Auditoria = Column(
    UNIQUEIDENTIFIER, primary_key=True, server_default=text("NEWID()"), index=True
)
    Fecha_Creacion = Column(DateTime, nullable=False)
    Fecha_Actualizacion = Column(DateTime,nullable=True, onupdate=func.now())
    Accion = Column(DateTime, server_default=func.now())
    