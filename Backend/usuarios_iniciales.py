"""
Script para crear datos iniciales del sistema: usuarios, editoriales y autores.
"""

from sqlalchemy.orm import Session
from Database.conexion import SessionLocal
from src.controller.auth_controller import create_user
from src.controller.editorial import create_editorial
from src.controller.Autor import create_autor
from src.controller.libro import create_libro
from src.schemas.auth import UserCreate
from src.schemas.editorial import EditorialCreate
from src.schemas.autor import AutorCreate
from src.schemas.libro import LibroCreate


def create_initial_users():
    """Crea usuarios iniciales del sistema."""
    print("\n" + "="*50)
    print("CREANDO USUARIOS INICIALES")
    print("="*50)
    
    db: Session = SessionLocal()
    
    try:
        users_to_create = [
            UserCreate(
                Username="Pablo",
                Correo="Nande@hospital.com",
                Telefono="3258796345",
                Nombre="Administrador",
                password="nande123",
                Rol="Admin",
            ),
            UserCreate(
                Username="emmanuel",
                Correo="Emmanuel@example.com",
                Telefono="3008964725",
                Nombre="Bibliotecario",
                password="emma123",
                Rol="Bibliotecario",
            ),
            UserCreate(
                Username="Santiago",
                Correo="correo.prueba160205@gmail.com",
                Telefono="3008964725",
                Nombre="Bibliotecario",
                password="santi123",
                Rol="Bibliotecario",
            ),
            UserCreate(
                Username="Omar",
                Correo="Omar@example.com",
                Telefono="3115489637",
                Nombre="Bibliotecario",
                password="lamosca123",
                Rol="Bibliotecario",
            ),
        ]

        for user in users_to_create:
            try:
                created_user = create_user(db, user)
                print(f"✅ Usuario creado: {created_user.Username} - Rol: {created_user.Rol}")
            except Exception as e:
                db.rollback()
                print(f"❌ No se pudo crear el usuario {user.Username}: {e}")
    
    except Exception as e:
        print(f"❌ Error general al crear usuarios: {e}")
    
    finally:
        db.close()


def create_initial_editorials():
    """Crea editoriales iniciales del sistema."""
    print("\n" + "="*50)
    print("CREANDO EDITORIALES INICIALES")
    print("="*50)
    
    db: Session = SessionLocal()
    
    try:
        editorials_to_create = [
            EditorialCreate(
                Nombre="Planeta",
                Pais="España",
                Contacto="contacto@planeta.com"
            ),
            EditorialCreate(
                Nombre="Penguin Random House",
                Pais="Estados Unidos",
                Contacto="info@penguinrandomhouse.com"
            ),
            EditorialCreate(
                Nombre="Alfaguara",
                Pais="México",
                Contacto="editorial@alfaguara.com"
            ),
            EditorialCreate(
                Nombre="Norma",
                Pais="Colombia",
                Contacto="contacto@norma.com"
            ),
            EditorialCreate(
                Nombre="Anagrama",
                Pais="España",
                Contacto="info@anagrama.es"
            ),
        ]

        for editorial in editorials_to_create:
            try:
                created_editorial = create_editorial(db, editorial)
                print(f"✅ Editorial creada: {created_editorial.Nombre} - País: {created_editorial.Pais}")
            except Exception as e:
                db.rollback()
                print(f"❌ No se pudo crear la editorial {editorial.Nombre}: {e}")
    
    except Exception as e:
        print(f"❌ Error general al crear editoriales: {e}")
    
    finally:
        db.close()


def create_initial_autores():
    """Crea autores iniciales del sistema."""
    print("\n" + "="*50)
    print("CREANDO AUTORES INICIALES")
    print("="*50)
    
    db: Session = SessionLocal()
    
    try:
        autores_to_create = [
            AutorCreate(
                Cedula_Autor="1234567890",
                Nombre="Gabriel García Márquez",
                Telefono="3001234567",
                Edad="87"
            ),
            AutorCreate(
                Cedula_Autor="0987654321",
                Nombre="Isabel Allende",
                Telefono="3007654321",
                Edad="82"
            ),
            AutorCreate(
                Cedula_Autor="1122334455",
                Nombre="Jorge Luis Borges",
                Telefono="3009876543",
                Edad="86"
            ),
            AutorCreate(
                Cedula_Autor="5544332211",
                Nombre="Mario Vargas Llosa",
                Telefono="3115556789",
                Edad="88"
            ),
            AutorCreate(
                Cedula_Autor="6677889900",
                Nombre="Julio Cortázar",
                Telefono="3002223344",
                Edad="69"
            ),
            AutorCreate(
                Cedula_Autor="9988776655",
                Nombre="Pablo Neruda",
                Telefono="3008887766",
                Edad="69"
            ),
            AutorCreate(
                Cedula_Autor="4455667788",
                Nombre="Laura Esquivel",
                Telefono="3004445566",
                Edad="74"
            ),
            AutorCreate(
                Cedula_Autor="7788990011",
                Nombre="Carlos Fuentes",
                Telefono="3007778899",
                Edad="83"
            ),
        ]

        for autor in autores_to_create:
            try:
                created_autor = create_autor(db, autor)
                print(f"✅ Autor creado: {created_autor.Nombre} - Cédula: {created_autor.Cedula_Autor}")
            except Exception as e:
                db.rollback()
                print(f"❌ No se pudo crear el autor {autor.Nombre}: {e}")
    
    except Exception as e:
        print(f"❌ Error general al crear autores: {e}")
    
    finally:
        db.close()


def create_initial_libros():
    """Crea libros iniciales del sistema."""
    print("\n" + "="*50)
    print("CREANDO LIBROS INICIALES")
    print("="*50)
    
    db: Session = SessionLocal()
    
    try:
        # Obtener autores y editoriales existentes
        from src.controller.Autor import get_autores
        from src.controller.editorial import get_editoriales
        
        autores = get_autores(db)
        editoriales = get_editoriales(db)
        
        if not autores or not editoriales:
            print("❌ No se pueden crear libros sin autores y editoriales")
            return
        
        # Asignar algunos autores y editoriales a los libros
        libros_to_create = [
            LibroCreate(
                Codigo_Libro="LIB001",
                Titulo="Cien años de soledad",
                Año="1967",
                Precio="45000",
                Id_Autor=str(autores[0].Id_Autor),  # Gabriel García Márquez
                Id_Editorial=str(editoriales[0].Id_Editorial)  # Planeta
            ),
            LibroCreate(
                Codigo_Libro="LIB002",
                Titulo="La casa de los espíritus",
                Año="1982",
                Precio="38000",
                Id_Autor=str(autores[1].Id_Autor),  # Isabel Allende
                Id_Editorial=str(editoriales[1].Id_Editorial)  # Penguin Random House
            ),
            LibroCreate(
                Codigo_Libro="LIB003",
                Titulo="El Aleph",
                Año="1949",
                Precio="35000",
                Id_Autor=str(autores[2].Id_Autor),  # Jorge Luis Borges
                Id_Editorial=str(editoriales[2].Id_Editorial)  # Alfaguara
            ),
            LibroCreate(
                Codigo_Libro="LIB004",
                Titulo="La ciudad y los perros",
                Año="1963",
                Precio="42000",
                Id_Autor=str(autores[3].Id_Autor),  # Mario Vargas Llosa
                Id_Editorial=str(editoriales[3].Id_Editorial)  # Norma
            ),
            LibroCreate(
                Codigo_Libro="LIB005",
                Titulo="Rayuela",
                Año="1963",
                Precio="40000",
                Id_Autor=str(autores[4].Id_Autor),  # Julio Cortázar
                Id_Editorial=str(editoriales[4].Id_Editorial)  # Anagrama
            ),
            LibroCreate(
                Codigo_Libro="LIB006",
                Titulo="Veinte poemas de amor y una canción desesperada",
                Año="1924",
                Precio="28000",
                Id_Autor=str(autores[5].Id_Autor),  # Pablo Neruda
                Id_Editorial=str(editoriales[0].Id_Editorial)  # Planeta
            ),
            LibroCreate(
                Codigo_Libro="LIB007",
                Titulo="Como agua para chocolate",
                Año="1989",
                Precio="36000",
                Id_Autor=str(autores[6].Id_Autor),  # Laura Esquivel
                Id_Editorial=str(editoriales[1].Id_Editorial)  # Penguin Random House
            ),
            LibroCreate(
                Codigo_Libro="LIB008",
                Titulo="La muerte de Artemio Cruz",
                Año="1962",
                Precio="39000",
                Id_Autor=str(autores[7].Id_Autor),  # Carlos Fuentes
                Id_Editorial=str(editoriales[2].Id_Editorial)  # Alfaguara
            ),
        ]

        for libro in libros_to_create:
            try:
                created_libro = create_libro(db, libro)
                print(f"✅ Libro creado: {created_libro.Titulo} - Año: {created_libro.Año}")
            except Exception as e:
                db.rollback()
                print(f"❌ No se pudo crear el libro {libro.Titulo}: {e}")
    
    except Exception as e:
        print(f"❌ Error general al crear libros: {e}")
    
    finally:
        db.close()


def create_all_initial_data():
    """Ejecuta la creación de todos los datos iniciales."""
    print("\n" + "🚀 INICIANDO CREACIÓN DE DATOS INICIALES" + "\n")
    
    try:
        create_initial_users()
        create_initial_editorials()
        create_initial_autores()
        create_initial_libros()
        
        print("\n" + "="*50)
        print("✅ PROCESO COMPLETADO")
        print("="*50 + "\n")

    except Exception as e:
        print(f"\n❌ Error general al crear datos iniciales: {e}\n")


if __name__ == "__main__":
    create_all_initial_data()