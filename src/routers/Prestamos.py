from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime

from Database.conexion import get_db
from src.schemas.prestamo import PrestamoCreate, PrestamoResponse
import src.controller.prestamo as prestamo_controller

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])


# ✅ Crear un nuevo préstamo
@router.post("/prestamos/", response_model=PrestamoResponse)
def create_prestamo(prestamo: PrestamoCreate, db: Session = Depends(get_db)):
    nuevo_prestamo = prestamo_controller.create_prestamo(db=db, prestamo_data=prestamo)

    if not nuevo_prestamo:
        raise HTTPException(status_code=400, detail="Error al crear el préstamo")

    return JSONResponse(
        status_code=201,
        content={
            "detail": "Préstamo creado correctamente",
            "data": {
                "Id_Prestamo": str(nuevo_prestamo.Id_Prestamo),
                "Fecha_Prestamo": str(nuevo_prestamo.Fecha_Prestamo),
                "Fecha_Devolucion": str(nuevo_prestamo.Fecha_Devolucion),
                "Estado": nuevo_prestamo.Estado,
            },
        },
    )


# ✅ Obtener todos los préstamos
@router.get("/prestamos/", response_model=list[PrestamoResponse])
def get_all_prestamos(db: Session = Depends(get_db)):
    prestamos = prestamo_controller.get_prestamos(db)

    if not prestamos:
        raise HTTPException(status_code=404, detail="No hay préstamos registrados")

    return JSONResponse(
        status_code=200,
        content={
            "detail": "Lista de préstamos obtenida correctamente",
            "data": [
                {
                    "Id_Prestamo": str(p.Id_Prestamo),
                    "Fecha_Prestamo": str(p.Fecha_Prestamo),
                    "Fecha_Devolucion": str(p.Fecha_Devolucion),
                    "Estado": p.Estado,
                }
                for p in prestamos
            ],
        },
    )


# ✅ Obtener un préstamo por ID
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
                "Fecha_Prestamo": str(prestamo.Fecha_Prestamo),
                "Fecha_Devolucion": str(prestamo.Fecha_Devolucion),
                "Estado": prestamo.Estado,
            },
        },
    )


# ✅ Actualizar un préstamo
@router.put("/prestamos/{prestamo_id}", response_model=PrestamoResponse)
def update_prestamo(prestamo_id: UUID, datos: PrestamoCreate, db: Session = Depends(get_db)):
    prestamo = prestamo_controller.get_prestamo(db, prestamo_id)

    if not prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")

    prestamo.Fecha_Prestamo = datos.Fecha_Prestamo
    prestamo.Fecha_Devolucion = datos.Fecha_Devolucion
    prestamo.Estado = datos.Estado
    prestamo.Fecha_actualizacion = datetime.now()

    db.commit()
    db.refresh(prestamo)

    return JSONResponse(
        status_code=200,
        content={
            "detail": "Préstamo actualizado correctamente",
            "data": {
                "Id_Prestamo": str(prestamo.Id_Prestamo),
                "Fecha_Prestamo": str(prestamo.Fecha_Prestamo),
                "Fecha_Devolucion": str(prestamo.Fecha_Devolucion),
                "Estado": prestamo.Estado,
            },
        },
    )


# ✅ Eliminar un préstamo
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
