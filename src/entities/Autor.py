import uuid
from sqlalchemy import Column, Date, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from Database.conexion import Base


class Autor(Base):

    __tablename__ = "Autores"

    Cedula_Autor= Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Nombre = Column(String, index=True)
    Telefono = Column(String)
    Edad = Column(String)

    # Relaciones
    libros = relationship("Libros", back_populates="Autores")  

