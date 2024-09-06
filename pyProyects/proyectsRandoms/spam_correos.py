import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor y credenciales
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Credenciales y destinatario
EMAIL = 'carmelojonathan664@gmail.com'
PASSWORD = 'gcfj qifu zyur pkas'  # Usa la contraseña específica para la aplicación aquí
RECEPTOR = 'elpepecrack53@gmail.com'

# Crear el mensaje
msg = MIMEMultipart()
msg['From'] = EMAIL
msg['To'] = RECEPTOR
msg['Subject'] = 'Hola amiguito'

# Cuerpo del correo
cuerpo = 'No te voy a invitar a mi fiesta'
msg.attach(MIMEText(cuerpo, 'plain'))

# Conectar al servidor SMTP y enviar el correo
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Inicia la conexión TLS
    server.login(EMAIL, PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL, RECEPTOR, text)
    print('Correo enviado exitosamente')
except smtplib.SMTPAuthenticationError:
    print('Error de autenticación. Verifica tu correo y contraseña.')
except smtplib.SMTPConnectError:
    print('Error de conexión al servidor SMTP. Verifica tu conexión a Internet y la configuración del servidor.')
except smtplib.SMTPRecipientsRefused:
    print('Error: El destinatario fue rechazado.')
except Exception as e:
    print(f'Error al enviar el correo: {e}')
finally:
    try:
        server.quit()
    except Exception as e:
        print(f'Error al cerrar la conexión con el servidor: {e}')