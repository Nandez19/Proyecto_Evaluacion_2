from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.password_reset import ForgotPasswordRequest, ResetPasswordRequest
from src.auth.password_reset import solicitar_reset_password, resetear_password
from Database.conexion import get_db

router = APIRouter(prefix="/Password", tags=["Password Reset"])


@router.post("/forgot-password")
def forgot_password(data: ForgotPasswordRequest, db: Session = Depends(get_db)):
    """
    Endpoint para solicitar un correo de restablecimiento de contraseña.
    """
    try:
        resultado = solicitar_reset_password(db, data.correo)
        return resultado
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reset-password")
def reset_password(data: ResetPasswordRequest, db: Session = Depends(get_db)):
    """
    Endpoint para restablecer la contraseña usando el token recibido por correo.
    """
    try:
        resultado = resetear_password(db, data.token, data.nueva_contraseña)
        return resultado
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
