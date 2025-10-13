
import uvicorn   
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from src.migrations import print_migration_status, run_migrations
from sqlalchemy import create_engine, text
from Database.conexion import DATABASE_URL
from src.entities import __all__
from Database.conexion import *
from src.routers import auth, Autores, Bibliotecarios, Editoriales, Libros, Prestamos, Clientes
from usuarios_iniciales import create_initial_users


app = FastAPI(
    title="API Biblioteca",
    version="1.0.0",
    description="API REST básica para gestión de una biblioteca académica.",
    openapi_tags=[
        
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes (orígenes)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todas las cabeceras
)

app.include_router(auth.router)
app.include_router(Autores.router)
app.include_router(Bibliotecarios.router)
app.include_router(Editoriales.router)
app.include_router(Libros.router)
app.include_router(Prestamos.router)
app.include_router(Clientes.router)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Se crean las tablas al ejecutar el servidor
@app.on_event("startup")
def startup_event():
    create_tables()
    create_initial_users()

    
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


@app.get(
    "/",
    summary="Información de la API",
    description="Endpoint raíz que proporciona información básica sobre la API",
    tags=["General"]
)
def root():
    return {
        "message": "Bienvenido a la API de Biblioteca",
        "version": "1.0.0",
        "descripcion": "Sistema para gestión de libros, desarrollado por Emmanuel, Santiago y Juan Pablo",
    }