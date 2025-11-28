"""
Authentication middleware for protecting endpoints.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from uuid import UUID

from Database.conexion import get_db
from src.auth.jwt_handler import verify_token
from src.controller.auth_controller import get_user_by_id
from src.schemas.auth import UserResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> UserResponse:
    token_data = verify_token(token)
    user_id_str = token_data.get("user_id")  # Es una string del JWT
    if not user_id_str:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o sin ID de usuario",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        user_id = UUID(user_id_str)  # Convierte string a UUID aquí
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="ID de usuario inválido en el token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = get_user_by_id(db, user_id)  # Ahora pasa el UUID al controller
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.Activo:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario inactivo",
        )

    return UserResponse(
        Id_Usuario=user.Id_Usuario,
        Username=user.Username,
        Correo=user.Correo,
        Telefono=user.Telefono,
        Nombre=user.Nombre,
        Rol=user.Rol,
        Fecha_creacion=user.Fecha_creacion,
        Fecha_actualizacion=user.Fecha_actualizacion,
        Activo=user.Activo,
    )


def get_current_active_user(
    current_user: UserResponse = Depends(get_current_user),
) -> UserResponse:
    """Verifica si el usuario actual está activo"""
    if not current_user.Activo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo"
        )
    return current_user


def require_role(required_role: str):
    """Dependency para validar roles"""

    def role_checker(
        current_user: UserResponse = Depends(get_current_active_user),
    ) -> UserResponse:
        if current_user.Rol != required_role and current_user.Rol != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Se requiere rol '{required_role}' o 'admin'",
            )
        return current_user

    return role_checker


"""Roles predefinidos"""

require_admin = require_role("admin")
require_bibliotecario = require_role("bibliotecario")
require_cliente = require_role("cliente")
