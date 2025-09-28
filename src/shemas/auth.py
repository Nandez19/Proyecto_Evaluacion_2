from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr



class UserBase(BaseModel):
    Nombre: str
    Telefono: str
    Correo: EmailStr
    Rol: str = "usuario"  # valores posibles: "usuario", "admin"

class UserCreate(UserBase):
    """Datos que envía el cliente para crear un usuario"""
    password: str  # Contraseña en texto plano, se hashéa antes de guardar

class UserResponse(UserBase):
    """Datos que devuelve la API al cliente"""
    id_usuario: UUID  # PK del usuario
    fecha_creacion: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None
    activo: bool = True

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    Correo: EmailStr  # o Nombre si quieres login por username
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

class TokenData(BaseModel):
    username: Optional[str] = None
    user_id: Optional[UUID] = None
    rol: Optional[str] = None
