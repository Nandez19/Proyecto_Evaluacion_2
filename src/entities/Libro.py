import uuid
from sqlalchemy import Column, Date, DateTime, ForeignKey, String, Double
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from Database.conexion import Base


class Libro(Base):
    __tablename__ = "Libro"

    Codigo_Libro= Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Titulo = Column(String, nullable=False)
    Año = Column(String,nullable=False)
    Precio = Column(Double,nullable=False)

    #Fk
    Cedula_Autor = Column(UUID(as_uuid=True), ForeignKey("Autor.Cedula_Autor"), nullable=False)

    # Relaciones
    Autor = relationship("Autor", back_populates="Libro")



