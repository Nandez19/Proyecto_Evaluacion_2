from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime

from Database.conexion import get_db
from src.schemas.prestamo import PrestamoCreate, PrestamoResponse
import src.controller.prestamo as prestamo_controller
from src.auth.middleware import get_current_user

router = APIRouter(
    prefix="/prestamos", tags=["Préstamos"], dependencies=[Depends(get_current_user)]
)

""" ✅ Crear un nuevo préstamo"""


@router.post("/prestamos/", response_model=PrestamoResponse)
def create_prestamo(prestamo: PrestamoCreate, db: Session = Depends(get_db)):
    nuevo_prestamo = prestamo_controller.create_prestamo(db=db, prestamo=prestamo)

    if not nuevo_prestamo:
        raise HTTPException(status_code=400, detail="Error al crear el préstamo")

    return JSONResponse(
        status_code=201,
        content={
            "detail": "Préstamo creado correctamente",
            "data": {
                "Id_Prestamo": str(nuevo_prestamo.Id_Prestamo),
                "Fecha_Prestamo": nuevo_prestamo.Fecha_Prestamo.isoformat() if hasattr(nuevo_prestamo.Fecha_Prestamo, 'isoformat') else str(nuevo_prestamo.Fecha_Prestamo),
                "Fecha_Devolucion": nuevo_prestamo.Fecha_Devolucion.isoformat() if nuevo_prestamo.Fecha_Devolucion and hasattr(nuevo_prestamo.Fecha_Devolucion, 'isoformat') else str(nuevo_prestamo.Fecha_Devolucion) if nuevo_prestamo.Fecha_Devolucion else None,
                "Estado": nuevo_prestamo.Estado,
                "Id_Libro": str(nuevo_prestamo.Id_Libro) if hasattr(nuevo_prestamo, 'Id_Libro') else None,
                "Id_Cliente": str(nuevo_prestamo.Id_Cliente) if hasattr(nuevo_prestamo, 'Id_Cliente') else None,
                "Id_Bibliotecario": str(nuevo_prestamo.Id_Bibliotecario) if hasattr(nuevo_prestamo, 'Id_Bibliotecario') else None,
            },
        },
    )


""" ✅ Obtener todos los préstamos - DEVUELVE ARRAY DIRECTO"""


@router.get("/prestamos/", response_model=list[PrestamoResponse])
def get_all_prestamos(db: Session = Depends(get_db)):
    prestamos = prestamo_controller.get_prestamos(db)

    # Si no hay préstamos, devolver array vacío en lugar de error
    if not prestamos:
        return []

    # ✅ DEVOLVER ARRAY DIRECTAMENTE (sin JSONResponse)
    return [
        {
            "Id_Prestamo": str(p.Id_Prestamo),
            "Fecha_Prestamo": p.Fecha_Prestamo.isoformat() if hasattr(p.Fecha_Prestamo, 'isoformat') else str(p.Fecha_Prestamo),
            "Fecha_Devolucion": p.Fecha_Devolucion.isoformat() if p.Fecha_Devolucion and hasattr(p.Fecha_Devolucion, 'isoformat') else str(p.Fecha_Devolucion) if p.Fecha_Devolucion else None,
            "Estado": p.Estado,
            "Id_Libro": str(p.Id_Libro) if hasattr(p, 'Id_Libro') and p.Id_Libro else None,
            "Id_Cliente": str(p.Id_Cliente) if hasattr(p, 'Id_Cliente') and p.Id_Cliente else None,
            "Id_Bibliotecario": str(p.Id_Bibliotecario) if hasattr(p, 'Id_Bibliotecario') and p.Id_Bibliotecario else None,
        }
        for p in prestamos
    ]


""" ✅ Obtener un préstamo por ID"""


@router.get("/prestamos/{prestamo_id}", response_model=PrestamoResponse)
def get_prestamo(prestamo_id: UUID, db: Session = Depends(get_db)):
    prestamo = prestamo_controller.get_prestamo(db, prestamo_id)

    if not prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")

    return JSONResponse(
        status_code=200,
        content={
            "detail": "Préstamo encontrado",
            "data": {
                "Id_Prestamo": str(prestamo.Id_Prestamo),
                "Fecha_Prestamo": prestamo.Fecha_Prestamo.isoformat() if hasattr(prestamo.Fecha_Prestamo, 'isoformat') else str(prestamo.Fecha_Prestamo),
                "Fecha_Devolucion": prestamo.Fecha_Devolucion.isoformat() if prestamo.Fecha_Devolucion and hasattr(prestamo.Fecha_Devolucion, 'isoformat') else str(prestamo.Fecha_Devolucion) if prestamo.Fecha_Devolucion else None,
                "Estado": prestamo.Estado,
                "Id_Libro": str(prestamo.Id_Libro) if hasattr(prestamo, 'Id_Libro') else None,
                "Id_Cliente": str(prestamo.Id_Cliente) if hasattr(prestamo, 'Id_Cliente') else None,
                "Id_Bibliotecario": str(prestamo.Id_Bibliotecario) if hasattr(prestamo, 'Id_Bibliotecario') else None,
            },
        },
    )


""" ✅ Actualizar un préstamo"""


@router.put("/prestamos/{prestamo_id}", response_model=PrestamoResponse)
def update_prestamo(
    prestamo_id: UUID, datos: PrestamoCreate, db: Session = Depends(get_db)
):
    prestamo = prestamo_controller.get_prestamo(db, prestamo_id)

    if not prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")

    # Actualizar campos
    prestamo.Fecha_Prestamo = datos.Fecha_Prestamo
    prestamo.Fecha_Devolucion = datos.Fecha_Devolucion
    prestamo.Estado = datos.Estado
    
    # Actualizar las relaciones si existen en el modelo
    if hasattr(datos, 'Id_Libro') and datos.Id_Libro:
        prestamo.Id_Libro = datos.Id_Libro
    if hasattr(datos, 'Id_Cliente') and datos.Id_Cliente:
        prestamo.Id_Cliente = datos.Id_Cliente
    if hasattr(datos, 'Id_Bibliotecario') and datos.Id_Bibliotecario:
        prestamo.Id_Bibliotecario = datos.Id_Bibliotecario
    
    prestamo.Fecha_actualizacion = datetime.now()

    db.commit()
    db.refresh(prestamo)

    return JSONResponse(
        status_code=200,
        content={
            "detail": "Préstamo actualizado correctamente",
            "data": {
                "Id_Prestamo": str(prestamo.Id_Prestamo),
                "Fecha_Prestamo": prestamo.Fecha_Prestamo.isoformat() if hasattr(prestamo.Fecha_Prestamo, 'isoformat') else str(prestamo.Fecha_Prestamo),
                "Fecha_Devolucion": prestamo.Fecha_Devolucion.isoformat() if prestamo.Fecha_Devolucion and hasattr(prestamo.Fecha_Devolucion, 'isoformat') else str(prestamo.Fecha_Devolucion) if prestamo.Fecha_Devolucion else None,
                "Estado": prestamo.Estado,
                "Id_Libro": str(prestamo.Id_Libro) if hasattr(prestamo, 'Id_Libro') else None,
                "Id_Cliente": str(prestamo.Id_Cliente) if hasattr(prestamo, 'Id_Cliente') else None,
                "Id_Bibliotecario": str(prestamo.Id_Bibliotecario) if hasattr(prestamo, 'Id_Bibliotecario') else None,
            },
        },
    )


""" ✅ Eliminar un préstamo"""


@router.delete("/prestamos/{prestamo_id}", response_model=PrestamoResponse)
def delete_prestamo(prestamo_id: UUID, db: Session = Depends(get_db)):
    prestamo = prestamo_controller.delete_prestamo(db, prestamo_id)

    if not prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")

    return JSONResponse(
        status_code=200,
        content={
            "detail": "Préstamo eliminado correctamente",
            "data": {
                "Id_Prestamo": str(prestamo.Id_Prestamo),
                "Estado": prestamo.Estado,
            },
        },
    )