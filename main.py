from sqlalchemy import text
from database.conexion import engine

def verificar_conexion():
    try:
        # Probar la conexión y ejecutar consulta
        with engine.connect() as conn:
            result = conn.execute(text("SELECT name FROM sys.Databases"))
            for row in result:
                print("-", row[0])
        print("Conexión exitosa ✅")
    except Exception as e:
        print("Error de conexión ❌:", e)

if __name__ == "__main__":
    verificar_conexion()






