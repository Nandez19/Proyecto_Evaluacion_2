from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from Database.conexion import get_db
from src.schemas.libro import libroCreate, libroResponse
import src.controller.libro as libro_controller

router = APIRouter(prefix="/libros", tags=["Libros"])


# ✅ Crear un nuevo libro
@router.post("/libros/", response_model=libroResponse)
def create_libro(libro: libroCreate, db: Session = Depends(get_db)):
    nuevo_libro = libro_controller.create_libro(db=db, libro=libro)
    if not nuevo_libro:
        raise HTTPException(status_code=400, detail="Error al crear el libro")

    return JSONResponse(
        status_code=201,
        content={
            "detail": "Libro creado correctamente",
            "data": {
                "Titulo": libro.Titulo,
                "Año": libro.Año,
                "Precio": libro.Precio,
            },
        },
    )


# ✅ Obtener todos los libros
@router.get("/libros/", response_model=list[libroResponse])
def get_all_libros(db: Session = Depends(get_db)):
    libros = libro_controller.get_all_libros(db)
    if not libros:
        raise HTTPException(status_code=404, detail="No hay libros registrados")
    return libros


# ✅ Obtener un libro por ID
@router.get("/libros/{libro_id}", response_model=libroResponse)
def get_libro(libro_id: str, db: Session = Depends(get_db)):
    libro = libro_controller.get_libro(db, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return JSONResponse(
        status_code=200,
        content={
            "detail": "Libro encontrado",
            "data": {
                "Id_Libro": str(libro.Id_Libro),
                "Codigo_Libro": libro.Codigo_Libro,
                "Titulo": libro.Titulo,
                "Año": libro.Año,
                "Precio": libro.Precio,
            },
        },
    )


# ✅ Actualizar un libro
@router.put("/libros/{libro_id}", response_model=libroResponse)
def update_libro(libro_id: str, libro: libroCreate, db: Session = Depends(get_db)):
    libro_actualizado = libro_controller.update_libro(db, libro_id, libro)
    if not libro_actualizado:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return JSONResponse(
        status_code=200,
        content={
            "detail": "Libro actualizado correctamente",
            "data": {
                "Titulo": libro.Titulo,
                "Año": libro.Año,
                "Precio": libro.Precio,
            },
        },
    )


# ✅ Eliminar un libro
@router.delete("/libros/{libro_id}", response_model=libroResponse)
def delete_libro(libro_id: str, db: Session = Depends(get_db)):
    libro_eliminado = libro_controller.delete_libro(db, libro_id)
    if not libro_eliminado:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return JSONResponse(
        status_code=200,
        content={
            "detail": "Libro eliminado correctamente",
            "data": {
                "Codigo_Libro": libro_eliminado.Codigo_Libro,
                "Titulo": libro_eliminado.Titulo,
            },
        },
    )