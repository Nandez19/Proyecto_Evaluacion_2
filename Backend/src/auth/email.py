import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURACIÓN DEL SERVIDOR SMTP ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "correo.prueba160205@gmail.com"
EMAIL_PASSWORD = "zjmgaypqcznpemzu"  # Contraseña de aplicación

image_url_1 = "https://instagram.feoh5-1.fna.fbcdn.net/v/t51.2885-19/470348068_588601943817534_2137280264568037441_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.feoh5-1.fna.fbcdn.net&_nc_cat=106&_nc_oc=Q6cZ2QHyd_N5SOVLsxr3drC0XNQA5KnnAcZgVpAF-Bk5-JUyz7gXSnysMjIB0oUdH7qDecfzaLKpOYdnOfMt2gw302pW&_nc_ohc=E6HK2mQe6XsQ7kNvwHWkZKs&_nc_gid=eB848EbGk-w_Jyl2gDHL-A&edm=AP4sbd4BAAAA&ccb=7-5&oh=00_AfjoFX36RRQOURRRU1zRSsyJXgHkluYDXnxmafncAWS_4Q&oe=691DE48E&_nc_sid=7a9f4b"
image_url_= "https://instagram.feoh5-1.fna.fbcdn.net/v/t51.2885-19/573326142_18098486959802216_8115530074740069421_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.feoh5-1.fna.fbcdn.net&_nc_cat=108&_nc_oc=Q6cZ2QFzpleHqZlg_36bxwMIY2Lm4ABl_x_iIAlLCDGqDMCFq88ZMZs1fG0_mb9wK1zTaCnrz4g8YnZg02uvP729bh4B&_nc_ohc=rMpTAf6UA1QQ7kNvwEDZNv5&_nc_gid=J8dZHOz6nIg2r8ThhCloHg&edm=ALGbJPMBAAAA&ccb=7-5&oh=00_AfhtpzNGFuE5iTiKHi2bFUgXrC0b3IXlvt6UUPpn-Zeobg&oe=691DC60A&_nc_sid=7d3ac5"

def enviar_correo_reset(destinatario: str, reset_link: str, image_url_1: str = image_url_1, image_url_2: str = image_url_):
    
    asunto = "Restablecimiento de contraseña"

    # --- HTML DEL CORREO ---
    html_content = f"""
    <html>
        <body>
            <div style="text-align: center; font-family: Arial;">
                <h2>Restablecer contraseña</h2>
                <p>Hemos recibido una solicitud para restablecer tu contraseña.</p>

                <p>
                    <a href="{reset_link}" 
                       style="padding: 10px 20px; background-color: #007bff; color: white;
                              text-decoration: none; border-radius: 5px;">
                        Restablecer contraseña
                    </a>
                </p>

                <br/>

                <!-- Mostrar imagen -->
                <img src="{image_url_1}" alt="Imagen" style="width:180px; border-radius:10px;">
                <img src="{image_url_}" alt="Imagen" style="width:180px; border-radius:10px;">

                
                <br/><br/>
                <p>Si no solicitaste este cambio, ignora este mensaje.</p>
                <p><b>Biblioteca ITM</b></p>
            </div>
        </body>
    </html>
    """

    msg = MIMEMultipart("alternative")
    msg["From"] = EMAIL_SENDER
    msg["To"] = destinatario
    msg["Subject"] = asunto

    # Adjuntar HTML
    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"✅ Correo enviado a {destinatario}")
    except Exception as e:
        print(f"❌ Error al enviar correo: {e}")
