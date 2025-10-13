from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from Database.conexion import get_db
from src.schemas.bibliotecario import BibliotecarioCreate, BibliotecarioResponse
from src.controller import bibliotecario as bibliotecario_controller

router = APIRouter(prefix="/bibliotecarios", tags=["Bibliotecarios"])

# ==========================================================
# Crear un bibliotecario
# ==========================================================
@router.post("/bibliotecarios/", response_model=BibliotecarioResponse)
def create_bibliotecario(biblio: BibliotecarioCreate, db: Session = Depends(get_db)) -> JSONResponse:
    db_biblio = bibliotecario_controller.create_bibliotecario(db, biblio)

    if db_biblio is None:
        raise HTTPException(status_code=400, detail="Error al crear bibliotecario")
    
    return JSONResponse(
        status_code=201,
        content={
            "detail": "Bibliotecario creado correctamente",
            "data": {
                "Cedula del Bibliotecario": biblio.Cedula_Bibliotecario,
                "Nombre": biblio.Nombre,
                "Teléfono": biblio.Telefono,
                "Edad": biblio.Edad,
            },
        },
    )


# ==========================================================
# Obtener todos los bibliotecarios
# ==========================================================
@router.get("/bibliotecarios/", response_model=list[BibliotecarioResponse])
def read_all_bibliotecarios(db: Session = Depends(get_db)):
    db_biblios = bibliotecario_controller.get_bibliotecarios(db)

    if not db_biblios:
        raise HTTPException(status_code=404, detail="No hay bibliotecarios registrados")

    return db_biblios


# ==========================================================
# Obtener un bibliotecario por ID
# ==========================================================
@router.get("/bibliotecarios/{biblio_id}", response_model=BibliotecarioResponse)
def read_one_bibliotecario(biblio_id: str, db: Session = Depends(get_db)):
    db_biblio = bibliotecario_controller.get_bibliotecario(db, biblio_id)

    if db_biblio is None:
        raise HTTPException(status_code=404, detail="Bibliotecario no encontrado")

    return JSONResponse(
        status_code=200,
        content={
            "detail": "Bibliotecario encontrado",
            "data": {
                "Cedula del Bibliotecario": db_biblio.Cedula_Bibliotecario,
                "Nombre": db_biblio.Nombre,
                "Teléfono": db_biblio.Telefono,
                "Edad": db_biblio.Edad,
            },
        },
    )


# ==========================================================
# Actualizar un bibliotecario
# ==========================================================
@router.put("/bibliotecarios/{biblio_id}", response_model=BibliotecarioResponse)
def update_bibliotecario(biblio_id: str, biblio: BibliotecarioCreate, db: Session = Depends(get_db)):
    db_biblio = bibliotecario_controller.update_bibliotecario(db, biblio_id, biblio)

    if db_biblio is None:
        raise HTTPException(status_code=404, detail="Bibliotecario no encontrado")

    return JSONResponse(
        status_code=200,
        content={
            "detail": "Bibliotecario actualizado correctamente",
            "data": {
                "Cedula del Bibliotecario": biblio.Cedula_Bibliotecario,
                "Nombre": biblio.Nombre,
                "Teléfono": biblio.Telefono,
                "Edad": biblio.Edad,
            },
        },
    )


# ==========================================================
# Eliminar un bibliotecario
# ==========================================================
@router.delete("/bibliotecarios/{biblio_id}", response_model=BibliotecarioResponse)
def delete_bibliotecario(biblio_id: str, db: Session = Depends(get_db)):
    db_biblio = bibliotecario_controller.delete_bibliotecario(db, biblio_id)

    if db_biblio is None:
        raise HTTPException(status_code=404, detail="Bibliotecario no encontrado")

    return JSONResponse(
        status_code=200,
        content={
            "detail": "Bibliotecario eliminado correctamente",
            "data": {
                "Cedula del Bibliotecario": db_biblio.Cedula_Bibliotecario,
                "Nombre": db_biblio.Nombre,
                "Teléfono": db_biblio.Telefono,
                "Edad": db_biblio.Edad,
            },
        },
    )