from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from Database.conexion import get_db
from src.auth.middleware import get_current_user
from src.controller.auth_controller import authenticate_user, create_user, create_user_token

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
            id_usuario=db_user.Cedula_Usuario,
            Nombre=db_user.Nombre,
            Telefono=db_user.Telefono,
            Correo=db_user.Correo,
            Rol=db_user.Rol,
            fecha_creacion=db_user.fecha_creacion,
            fecha_actualizacion=db_user.fecha_actualizacion,
            activo=db_user.activo,
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# ---------------------------
# LOGIN
# ---------------------------
@router.post("/login", response_model=LoginResponse)
def login_user(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, login_data.Correo, login_data.password)
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
            id_usuario=user.Cedula_Usuario,
            Nombre=user.Nombre,
            Telefono=user.Telefono,
            Correo=user.Correo,
            Rol=user.Rol,
            fecha_creacion=user.fecha_creacion,
            fecha_actualizacion=user.fecha_actualizacion,
            activo=user.activo,
        ),
    )

# ---------------------------
# INFO DEL USUARIO ACTUAL
# ---------------------------
@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: UserResponse = Depends(get_current_user)):
    return current_user
