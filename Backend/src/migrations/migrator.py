"""
Sistema de migración automática para la base de datos PostgreSQL.
"""

import logging
from typing import List

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from Database.conexion import Base, engine

from src.entities.autor import Autor
from src.entities.bibliotecario import Bibliotecario
from src.entities.cliente import Cliente
from src.entities.editorial import Editorial
from src.entities.libro import Libro
from src.entities.prestamo import Prestamo
from src.entities.usuario import Usuario

"""Configurar logging"""
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def check_table_exists(table_name: str) -> bool:
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text(
                    """
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = :table_name
                );
            """
                ),
                {"table_name": table_name},
            )
            return result.scalar()
    except Exception as e:
        logger.error(f"Error verificando tabla {table_name}: {e}")
        return False


def get_existing_tables() -> List[str]:
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text(
                    """
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """
                )
            )
            return [row[0] for row in result.fetchall()]
    except Exception as e:
        logger.error(f"Error obteniendo tablas existentes: {e}")
        return []


def create_tables():
    """
    Crea todas las tablas definidas en los modelos de entidades.
    """
    try:
        logger.info("🏗️  Creando tablas faltantes...")
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Tablas creadas exitosamente")
    except Exception as e:
        logger.error(f"❌ Error creando tablas: {e}")
        raise


def verify_migration_success() -> bool:
    required_tables = [
        "usuarios",
        "autores",
        "bibliotecarios",
        "editoriales",
        "libros",
        "prestamos",
        "clientes",
    ]
    existing_tables = get_existing_tables()
    missing_tables = [
        table for table in required_tables if table not in existing_tables
    ]
    if missing_tables:
        logger.warning(f"⚠️  Tablas faltantes: {missing_tables}")
        return False
    logger.info("✅ Todas las tablas requeridas están presentes")
    return True


def run_migrations():
    try:
        logger.info("🔄 Iniciando migración automática...")

        """Verificar conexión a la base de datos"""
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("✅ Conexión a PostgreSQL establecida")

        """Obtener tablas existentes"""
        existing_tables = get_existing_tables()
        logger.info(f"📋 Tablas existentes: {existing_tables}")

        """Crear tablas faltantes"""
        create_tables()

        """Verificar que la migración fue exitosa"""
        if verify_migration_success():
            logger.info("🎉 Migración completada exitosamente!")
            return True
        else:
            logger.error("❌ La migración no se completó correctamente")
            return False

    except SQLAlchemyError as e:
        logger.error(f"❌ Error de base de datos durante la migración: {e}")
        return False
    except Exception as e:
        logger.error(f"❌ Error inesperado durante la migración: {e}")
        return False


def print_migration_status():
    try:
        existing_tables = get_existing_tables()
        required_tables = [
            "usuarios",
            "autores",
            "bibliotecarios",
            "editoriales",
            "libros",
            "prestamos",
            "clientes",
        ]

        print("\n📊 Estado de la Base de Datos:")
        print("=" * 50)

        for table in required_tables:
            status = "✅" if table in existing_tables else "❌"
            print(f"{status} {table}")

        print("=" * 50)

        if len(existing_tables) == len(required_tables):
            print("🎉 Todas las tablas están presentes y actualizadas")
        else:
            print("⚠️  Algunas tablas faltan o necesitan actualización")

    except Exception as e:
        logger.error(f"Error mostrando estado de migración: {e}")
