from datetime import datetime, timedelta
from fastapi import HTTPException, status
from src.auth.jwt_handler import SECRET_KEY, ALGORITHM, pwd_context  
from src.auth.email import enviar_correo_reset
from src.entities.usuario import Usuario
import jwt


def solicitar_reset_password(db, correo: str):
    """
    Genera token y envía correo de restablecimiento.
    """
    user = db.query(Usuario).filter(Usuario.Correo == correo).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    expire = datetime.utcnow() + timedelta(minutes=15)
    token = jwt.encode({"sub": correo, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)

    reset_link = f"http://localhost:4200/auth/new-password?token={token}"
    enviar_correo_reset(correo, reset_link)

    return {"message": "Correo de recuperación enviado", "token": token}


def resetear_password(db, token: str, nueva_contraseña: str):
    """
    Valida token y actualiza la contraseña del usuario.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        correo = payload.get("sub")
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El enlace ha expirado."
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido."
        )

    user = db.query(Usuario).filter(Usuario.Correo == correo).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado."
        )

    user.Password_Hash = pwd_context.hash(nueva_contraseña)
    db.commit()

    return {"message": "Contraseña actualizada exitosamente."}
