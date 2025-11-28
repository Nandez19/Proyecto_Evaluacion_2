"""
Configuración compartida para todas las pruebas
Fixtures y configuración común
"""
import pytest
from datetime import datetime
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from Database.conexion import Base, get_db
from main import app

# Base de datos en memoria para testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Hacer que SQLite soporte UUID convirtiéndolos a String
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_conn, connection_record):
    """Configurar SQLite para soportar foreign keys"""
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# Monkey patch para que SQLite soporte UUID como TEXT
import sqlalchemy.dialects.sqlite.base as sqlite_base
from sqlalchemy.dialects.postgresql import UUID

# Agregar soporte para UUID en SQLite
def visit_UUID(self, type_, **kw):
    return "TEXT"

if not hasattr(sqlite_base.SQLiteTypeCompiler, 'visit_UUID'):
    sqlite_base.SQLiteTypeCompiler.visit_UUID = visit_UUID

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """
    Crear una sesión de base de datos para cada test.
    Se crea y destruye la base de datos para cada prueba.
    """
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Limpiar después de cada prueba
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """
    Cliente de prueba para hacer requests HTTP a la API.
    Sobrescribe la dependencia get_db para usar la sesión de prueba.
    """
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    from fastapi.testclient import TestClient
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def usuario_ejemplo(db_session):
    """Fixture para crear un usuario de ejemplo"""
    from src.entities.usuario import Usuario
    from src.auth.jwt_handler import get_password_hash
    
    usuario = Usuario(
        Username="testuser",
        Nombre="Usuario Test",
        Correo="test@example.com",
        Telefono="3001234567",
        Password_Hash=str(get_password_hash("Password123!")),
        Activo=True,
        Rol="USER",
        Fecha_creacion=datetime.now()
    )
    db_session.add(usuario)
    db_session.commit()
    db_session.refresh(usuario)
    return usuario


@pytest.fixture
def admin_ejemplo(db_session):
    """Fixture para crear un usuario administrador de ejemplo"""
    from src.entities.usuario import Usuario
    from src.auth.jwt_handler import get_password_hash
    
    admin = Usuario(
        Username="admin",
        Nombre="Administrador",
        Correo="admin@system.com",
        Telefono="3009876543",
        Password_Hash=str(get_password_hash("Admin123!")),
        Activo=True,
        Rol="ADMIN",
        Fecha_creacion=datetime.now()
    )
    db_session.add(admin)
    db_session.commit()
    db_session.refresh(admin)
    return admin


@pytest.fixture
def token_usuario(client, usuario_ejemplo):
    """
    Fixture para obtener token JWT de un usuario normal.
    Hace login y devuelve el token.
    """
    # Tu login usa Form data, NO JSON
    login_data = {
        "username": usuario_ejemplo.Username,
        "password": "Password123!"
    }
    response = client.post("/auth/login", data=login_data)
    
    if response.status_code != 200:
        raise Exception(f"Login falló: {response.json()}")
    
    return response.json()["access_token"]


@pytest.fixture
def token_admin(client, admin_ejemplo):
    """
    Fixture para obtener token JWT de un administrador.
    Hace login y devuelve el token.
    """
    # Tu login usa Form data, NO JSON
    login_data = {
        "username": admin_ejemplo.Username,
        "password": "Admin123!"
    }
    response = client.post("/auth/login", data=login_data)
    
    if response.status_code != 200:
        raise Exception(f"Login falló: {response.json()}")
    
    return response.json()["access_token"]


@pytest.fixture
def headers_usuario(token_usuario):
    """
    Fixture para obtener headers con token de usuario normal.
    """
    return {"Authorization": f"Bearer {token_usuario}"}


@pytest.fixture
def headers_admin(token_admin):
    """
    Fixture para obtener headers con token de admin.
    """
    return {"Authorization": f"Bearer {token_admin}"}


@pytest.fixture
def autor_ejemplo(db_session):
    """Fixture para crear un autor de ejemplo"""
    from src.entities.autor import Autor
    
    autor = Autor(
        Cedula_Autor="1234567890",
        Nombre="Gabriel García Márquez",
        Telefono="3001234567",
        Edad="95"
    )
    db_session.add(autor)
    db_session.commit()
    db_session.refresh(autor)
    return autor


@pytest.fixture
def bibliotecario_ejemplo(db_session):
      from src.entities.bibliotecario import Bibliotecario
      biblio = Bibliotecario(
          Cedula_Bibliotecario="1234567890",
          Nombre="Ejemplo",
          Telefono="3001234567",
          Edad="30",
          # Asigna Id_usuario_creacion si es requerido
      )
      db_session.add(biblio)
      db_session.commit()
      db_session.refresh(biblio)
      return biblio

@pytest.fixture
def cliente_ejemplo(db_session):

    from src.entities.cliente import Cliente

    cliente = Cliente(
        Cedula_Cliente="1234567890",
        Nombre="Ejemplo",
        Telefono="3001234567",
        Correo="ejemplo@example.com",
        # Asigna Id_usuario_creacion si es requerido
    )
    db_session.add(cliente)
    db_session.commit()
    db_session.refresh(cliente)
    return cliente