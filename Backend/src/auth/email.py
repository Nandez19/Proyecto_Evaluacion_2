import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURACIÓN DEL SERVIDOR SMTP ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "correo.prueba160205@gmail.com"
EMAIL_PASSWORD = "zjmgaypqcznpemzu"  # Usa una contraseña de aplicación, no la real: 
#Contraseña: zjmg aypq cznp emzu


def enviar_correo_reset(destinatario: str, reset_link: str):
    
    asunto = "Restablecimiento de contraseña"
    cuerpo = f"""
    Hola,

    Recibimos una solicitud para restablecer tu contraseña.

    Puedes hacerlo haciendo clic en el siguiente enlace (válido por 15 minutos):

    {reset_link}

    Si no solicitaste este cambio, ignora este correo.

    Atentamente,
    El equipo de soporte.
    BibliotecaITM
    """

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = destinatario
    msg["Subject"] = asunto

    msg.attach(MIMEText(cuerpo, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"✅ Correo enviado a {destinatario}")
    except Exception as e:
        print(f"❌ Error al enviar correo: {e}")
