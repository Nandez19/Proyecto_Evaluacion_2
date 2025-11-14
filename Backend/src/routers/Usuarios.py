from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Database.conexion import get_db
from src.entities.usuario import Usuario  # tu modelo SQLAlchemy
from src.schemas.auth import UserResponse  # si tienes un esquema para devolver datos

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/usuarios", response_model=list[UserResponse], tags=["Usuarios"])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()
