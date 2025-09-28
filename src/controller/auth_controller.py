from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy.orm import Session

from src.auth.jwt_handler import create_access_token, get_password_hash, verify_password
from src.entities.Usuario import Usuario
from src.shemas.auth import LoginRequest, UserCreate, UserResponse


# ---------------------------
# CREAR USUARIO
# ---------------------------
def create_user(db: Session, user: UserCreate) -> Usuario:
    """
    Crea un nuevo usuario en la base de datos.
    """
    # Verificar si el nombre ya existe
    existing_user = get_user_by_nombre(db, user.Nombre)
    if existing_user:
        raise ValueError("El nombre de usuario ya existe")

    # Verificar si el correo ya existe
    existing_email = get_user_by_email(db, user.Correo)
    if existing_email:
        raise ValueError("El correo electrónico ya está registrado")

    # Crear nuevo usuario
    hashed_password = get_password_hash(user.password)
    db_user = Usuario(
        Cedula_Usuario=uuid4(),
        Nombre=user.Nombre,
        Telefono=user.Telefono,
        Correo=user.Correo,
        password_hash=hashed_password,
        Rol=user.Rol,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ---------------------------
# FUNCIONES AUXILIARES
# ---------------------------
def get_user_by_nombre(db: Session, nombre: str) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.Nombre == nombre).first()


def get_user_by_email(db: Session, correo: str) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.Correo == correo).first()


def get_user_by_id(db: Session, user_id: UUID) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.Cedula_Usuario == user_id).first()

