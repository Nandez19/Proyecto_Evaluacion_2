import sys
import os

# Agregar carpeta raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.conexion import Base, engine
from entities import init_entities

Base.metadata.create_all(bind=engine)
print("✅ Tablas creadas en la base de datos")
