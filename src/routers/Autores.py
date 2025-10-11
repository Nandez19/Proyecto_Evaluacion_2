from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from uuid import UUID

import src.controller.Autor as autor_controller
from Database.conexion import get_db
from src.schemas.autor import AutorCreate, AutorResponse
from src.auth.middleware import get_current_user   
router = APIRouter(prefix="/autores", tags=["Autores"], dependencies=[Depends(get_current_user)])

# ============================================================
# RUTAS PARA AUTORES
# ============================================================

@router.post("/autores/", response_model=AutorResponse, tags=["Autores"])
def create_autor(autor: AutorCreate, db: Session = Depends(get_db)) -> JSONResponse:
    autor_creado = autor_controller.create_autor(db=db, autor=autor)
    if autor_creado is None:
        raise HTTPException(status_code=400, detail="Error al crear el autor")
    else:
        return JSONResponse(
            status_code=201,
            content={
                "detail": "Autor creado correctamente",
                "Cuerpo de la respuesta": {
                    #"ID del Autor": str(autor.Id_Autor),
                    "Cédula": autor.Cedula_Autor,
                    "Nombre": autor.Nombre,
                    "Teléfono": autor.Telefono,
                    "Edad": autor.Edad,
                },
            },
        )


@router.get("/autores/", response_model=list[AutorResponse], tags=["Autores"])
def read_all_autores(db: Session = Depends(get_db)):
    autores = autor_controller.get_autores(db)
    if not autores:
        raise HTTPException(status_code=404, detail="No hay autores registrados")
    return autores


@router.get("/autores/{autor_id}", response_model=AutorResponse, tags=["Autores"])
def read_one_autor(autor_id: UUID, db: Session = Depends(get_db)):
    autor = autor_controller.get_autor(db, autor_id=autor_id)
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    else:
        return JSONResponse(
            status_code=200,
            content={
                "detail": "Autor encontrado",
                "data": {
                    "ID del Autor": str(autor.Id_Autor),
                    "Cédula": autor.Cedula_Autor,
                    "Nombre": autor.Nombre,
                    "Teléfono": autor.Telefono,
                    "Edad": autor.Edad,
                },
            },
        )


@router.put("/autores/{autor_id}", response_model=AutorResponse, tags=["Autores"])
def update_autor(autor_id: UUID, autor: AutorCreate, db: Session = Depends(get_db)):
    autor_actualizado = autor_controller.update_autor(db, autor_id=autor_id, autor=autor)
    if autor_actualizado is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    else:
        return JSONResponse(
            status_code=201,
            content={
                "detail": "Autor actualizado correctamente",
                "data": {
                    #"ID del Autor": str(autor.Id_Autor),
                    "Cédula": autor.Cedula_Autor,
                    "Nombre": autor.Nombre,
                    "Teléfono": autor.Telefono,
                    "Edad": autor.Edad,
                },
            },
        )


@router.delete("/autores/{autor_id}", response_model=AutorResponse, tags=["Autores"])
def delete_autor(autor_id: UUID, db: Session = Depends(get_db)):
    autor_eliminado = autor_controller.delete_autor(db, autor_id=autor_id)
    if autor_eliminado is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    else:
        return JSONResponse(
            status_code=200,
            content={
                "detail": "Autor eliminado correctamente",
                "data": {
                    "ID del Autor": str(autor_eliminado.Id_Autor),
                    "Cédula": autor_eliminado.Cedula_Autor,
                    "Nombre": autor_eliminado.Nombre,
                    "Teléfono": autor_eliminado.Telefono,
                    "Edad": autor_eliminado.Edad,
                },
            },
        )
