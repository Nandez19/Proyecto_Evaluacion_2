from sqlalchemy import create_engine, text
from Database.conexion import DATABASE_URL
from src.entities import *
from Database.conexion import *
from fastapi import FastAPI
import uvicorn   

app = FastAPI(
    title="API Biblioteca",
    version="1.0.0",
    description="API REST básica para gestión de una biblioteca académica.",
    openapi_tags=[
        {"name": "Usuarios",
            "description": "CRUD para gestionar los usuarios registrados en la biblioteca. Permite crear, consultar, actualizar y eliminar usuarios."},
        {"name": "Libros",
            "description": "CRUD para administrar los libros disponibles en la biblioteca. Permite agregar, consultar, modificar y eliminar información de libros."},
        {"name": "Prestamos",
            "description": "CRUD para gestionar los préstamos de libros. Permite registrar, consultar, actualizar y finalizar préstamos realizados por los usuarios."}
    ]
)

# Se crean las tablas al ejecutar el servidor
@app.on_event("startup")
def startup_event():
    create_tables()
    print("✅ Tablas creadas al iniciar FastAPI")

    
@app.on_event("shutdown")
def shutdown_event():
    drop_tables()
    print("✅ Tablas Eliminadas al cerrar FastAPI")


def main():     
    print("Iniciando servidor FastAPI...")
    uvicorn.run(
        "main:app",
        # host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )


if __name__ == "__main__":
    main()
