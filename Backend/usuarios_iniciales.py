"""
Script para crear usuarios iniciales del sistema.
"""

from sqlalchemy.orm import Session
from Database.conexion import SessionLocal
from src.controller.auth_controller import create_user
from src.schemas.auth import UserCreate


def create_initial_users():
    db: Session = SessionLocal()

    try:
        users_to_create = [
            UserCreate(
                Username="Pablo",
                Correo="Nande@hospital.com",
                Telefono="3258796345",
                Nombre="Administrador",
                password="nande123",
                Rol="admin",
            ),
            UserCreate(
                Username="Emmanuel",
                Correo="Emmanuel@example.com",
                Telefono="3008964725",
                Nombre="Bibliotecario",
                password="goblin123",
                Rol="bibliotecario",
            ),
            UserCreate(
                Username="Santiago",
                Correo="Santiago@example.com",
                Telefono="3008964725",
                Nombre="Bibliotecario",
                password="santi123",
                Rol="bibliotecario",
            ),
            UserCreate(
                Username="Mosca",
                Correo="Laosca@example.com",
                Telefono="3115489637",
                Nombre="Admin",
                password="lamosca123",
                Rol="admin",
            ),
        ]

        for user in users_to_create:
            try:
                created_user = create_user(db, user)
                print(
                    f"✅ Usuario creado: {created_user.Username} - Rol: {created_user.Rol}"
                )
            except Exception as e:
                db.rollback()
                print(f"❌ No se pudo crear el usuario {user.Username}: {e}")

    except Exception as e:
        print(f"❌ Error general al crear usuarios iniciales: {e}")

    finally:
        db.close()
