import uuid
from sqlalchemy import Column, Date, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from Database.conexion import Base


class Editorial(Base):
    __tablename__ = "Editoriales"

    Id_Editorial = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Nombre = Column(String, nullable=False)
    Pais = Column(String, nullable=False)
    Contacto = Column(String, nullable=False) 

    #Relaciones
    Libro = relationship("Libro", back_populates="Editorial")

    