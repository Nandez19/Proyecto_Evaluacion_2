from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from Database.conexion import get_db
from src.schemas.cliente import ClienteCreate, ClienteResponse
from src.controller import cliente as cliente_controller

router = APIRouter(prefix="/clientes", tags=["Clientes"])

# ==========================================================
# Crear un cliente
# ==========================================================
@router.post("/", response_model=ClienteResponse)
def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)) -> JSONResponse:
    db_cliente = cliente_controller.create_cliente(db, cliente)
    if db_cliente is None:
        raise HTTPException(status_code=400, detail="Error al crear cliente")
    return JSONResponse(
        status_code=201,
        content={
            "detail": "Cliente creado correctamente",
            "data": {
                "Cedula_Cliente": cliente.Cedula_Cliente,
                "Nombre": cliente.Nombre,
                "Telefono": cliente.Telefono,
                "Correo": cliente.Correo,
            },
        },
    )

# ==========================================================
# Obtener todos los clientes
# ==========================================================
@router.get("/", response_model=list[ClienteResponse])
def read_all_clientes(db: Session = Depends(get_db)):
    db_clientes = cliente_controller.get_clientes(db)
    if not db_clientes:
        raise HTTPException(status_code=404, detail="No hay clientes registrados")
    return db_clientes

# ==========================================================
# Obtener un cliente por ID
# ==========================================================
@router.get("/{cliente_id}", response_model=ClienteResponse)
def read_one_cliente(cliente_id: str, db: Session = Depends(get_db)):
    db_cliente = cliente_controller.get_cliente(db, cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return JSONResponse(
        status_code=200,
        content={
            "detail": "Cliente encontrado",
            "data": {
                "Cedula_Cliente": db_cliente.Cedula_Cliente,
                "Nombre": db_cliente.Nombre,
                "Telefono": db_cliente.Telefono,
                "Correo": db_cliente.Correo,
            },
        },
    )

# ==========================================================
# Actualizar un cliente
# ==========================================================
@router.put("/{cliente_id}", response_model=ClienteResponse)
def update_cliente(cliente_id: str, cliente: ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = cliente_controller.update_cliente(db, cliente_id, cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return JSONResponse(
        status_code=200,
        content={
            "detail": "Cliente actualizado correctamente",
            "data": {
                "Cedula_Cliente": cliente.Cedula_Cliente,
                "Nombre": cliente.Nombre,
                "Telefono": cliente.Telefono,
                "Correo": cliente.Correo,
            },
        },
    )

# ==========================================================
# Eliminar un cliente
# ==========================================================
@router.delete("/{cliente_id}", response_model=ClienteResponse)
def delete_cliente(cliente_id: str, db: Session = Depends(get_db)):
    db_cliente = cliente_controller.delete_cliente(db, cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return JSONResponse(
        status_code=200,
        content={
            "detail": "Cliente eliminado correctamente",
            "data": {
                "Cedula_Cliente": db_cliente.Cedula_Cliente,
                "Nombre": db_cliente.Nombre,
                "Telefono": db_cliente.Telefono,
                "Correo": db_cliente.Correo,
            },
        },
    )