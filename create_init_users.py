
import sys

from sqlalchemy.orm import Session

from Database.conexion import SessionLocal, create_tables
from src.controller.auth_controller import create_user
from src.shemas.auth import UserCreate


def create_initial_users():
    """
    Crea usuarios iniciales para el sistema.
    """
    # Crear tablas si no existen
    create_tables()

    db = SessionLocal()
    try:
        # Usuario administrador
        admin_user = UserCreate(
            username="Admin",
            email="elchurches@admin.com",
            nombre_completo="Administrador del Sistema",
            password="admin123",
            rol="admin",
        )

        # Usuario Cliente
        cliente_user = UserCreate(
            username="dr_garcia",
            email="dr.garcia@hospital.com",
            nombre_completo="Dr. Carlos García",
            password="medico123",
            rol="medico",
        )

        users_to_create = [admin_user, cliente_user]

        for user_data in users_to_create:
            try:
                create_user(db, user_data)
                print(f"Usuario creado: {user_data.username} ({user_data.rol})")
            except ValueError as e:
                print(f"Usuario {user_data.username} ya existe: {e}")

        print("\nUsuarios iniciales creados exitosamente!")
        print("\nCredenciales de acceso:")
        print("\nAdmin: admin / admin123")
        print("\nMédico: dr_garcia / medico123")
        print("\nfermera: enfermera_lopez / enfermera123")
        print("\nUsuario: usuario_test / usuario123")

    except Exception as e:
        print(f"Error creando usuarios: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    create_initial_users()