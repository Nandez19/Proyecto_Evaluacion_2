from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from Database.conexion import get_db
from src.schemas.editorial import editorialCreate, editorialResponse
import src.controller.editorial as editorial_controller

router = APIRouter(prefix="/editoriales", tags=["Editoriales"])


# ✅ Crear una nueva editorial
@router.post("/editoriales/", response_model=editorialResponse)
def create_editorial(editorial: editorialCreate, db: Session = Depends(get_db)):
    nueva_editorial = editorial_controller.create_editorial(db=db, editorial=editorial)
    if not nueva_editorial:
        raise HTTPException(status_code=400, detail="Error al crear la editorial")
    return JSONResponse(
        status_code=201,
        content={
            "detail": "Editorial creada correctamente",
            "data": {
                "Nombre": editorial.Nombre,
                "Pais": editorial.Pais,
                "Contacto": editorial.Contacto,
            },
        },
    )


# ✅ Obtener todas las editoriales
@router.get("/editoriales/", response_model=list[editorialResponse])
def get_all_editoriales(db: Session = Depends(get_db)):
    editoriales = editorial_controller.get_all_editoriales(db)
    if not editoriales:
        raise HTTPException(status_code=404, detail="No hay editoriales registradas")
    return editoriales


# ✅ Obtener una editorial por ID
@router.get("/editoriales/{editorial_id}", response_model=editorialResponse)
def get_editorial(editorial_id: str, db: Session = Depends(get_db)):
    editorial = editorial_controller.get_editorial(db, editorial_id)
    if not editorial:
        raise HTTPException(status_code=404, detail="Editorial no encontrada")
    return JSONResponse(
        status_code=200,
        content={
            "detail": "Editorial encontrada",
            "data": {
                "Id_Editorial": str(editorial.Id_Editorial),
                "Nombre": editorial.Nombre,
                "Pais": editorial.Pais,
                "Contacto": editorial.Contacto,
            },
        },
    )


# ✅ Actualizar una editorial
@router.put("/editoriales/{editorial_id}", response_model=editorialResponse)
def update_editorial(editorial_id: str, editorial: editorialCreate, db: Session = Depends(get_db)):
    editorial_actualizada = editorial_controller.update_editorial(db, editorial_id, editorial)
    if not editorial_actualizada:
        raise HTTPException(status_code=404, detail="Editorial no encontrada")
    return JSONResponse(
        status_code=200,
        content={
            "detail": "Editorial actualizada correctamente",
            "data": {
                "Nombre": editorial.Nombre,
                "Pais": editorial.Pais,
                "Contacto": editorial.Contacto,
            },
        },
    )


# ✅ Eliminar una editorial
@router.delete("/editoriales/{editorial_id}", response_model=editorialResponse)
def delete_editorial(editorial_id: str, db: Session = Depends(get_db)):
    editorial_eliminada = editorial_controller.delete_editorial(db, editorial_id)
    if not editorial_eliminada:
        raise HTTPException(status_code=404, detail="Editorial no encontrada")
    return JSONResponse(
        status_code=200,
        content={
            "detail": "Editorial eliminada correctamente",
            "data": {
                "Id_Editorial": str(editorial_eliminada.Id_Editorial),
                "Nombre": editorial_eliminada.Nombre,
            },
        },
    )