from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from Database.conexion import get_db
from src.auth.middleware import get_current_user
from src.controller.auth_controller import authentic_user, create_user, create_user_token

from src.schemas.auth import LoginRequest, LoginResponse, UserCreate, UserResponse

# OAuth2 scheme para extraer el token del header Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

router = APIRouter(prefix="/auth", tags=["Autenticación"])

# ---------------------------
# REGISTRO DE USUARIO
# ---------------------------
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = create_user(db, user)
        return UserResponse(
            Id_Usuario=db_user.Id_Usuario,
            Username=db_user.Username,
            Correo=db_user.Correo,
            Nombre=db_user.Nombre,
            Rol=db_user.Rol,
            Activo=db_user.Activo,
            Fecha_creacion=db_user.Fecha_creacion,
            Fecha_actualizacion = db_user.Fecha_actualizacion
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# ---------------------------
# LOGIN
# ---------------------------
@router.post("/login", response_model=LoginResponse)
def login_user(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = authentic_user(db, login_data.Username, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_user_token(user)
    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            Id_Usuario=user.Id_Usuario,
            Username=user.Username,
            Correo=user.Correo,
            Nombre=user.Nombre,
            Rol=user.Rol,
            Activo=user.Activo,
            Fecha_creacion=user.Fecha_creacion,
            Fecha_actualizacion = user.Fecha_actualizacion
        ),
    )

# ---------------------------
# INFO DEL USUARIO ACTUAL
# ---------------------------
@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: UserResponse = Depends(get_current_user)):
    return current_user
