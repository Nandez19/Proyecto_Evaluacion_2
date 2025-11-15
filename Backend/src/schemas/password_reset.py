from pydantic import BaseModel, EmailStr

class ForgotPasswordRequest(BaseModel):
    correo: EmailStr

class ResetPasswordRequest(BaseModel):
    token: str
    nueva_contraseña: str
