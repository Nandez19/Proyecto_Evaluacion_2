"""
Script para crear datos iniciales del sistema: usuarios, editoriales, autores, 
bibliotecarios, clientes y préstamos.
"""

from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from Database.conexion import SessionLocal
from src.controller.auth_controller import create_user
from src.controller.editorial import create_editorial
from src.controller.Autor import create_autor
from src.controller.libro import create_libro
from src.controller.bibliotecario import create_bibliotecario
from src.controller.cliente import create_cliente
from src.controller.prestamo import create_prestamo
from src.schemas.auth import UserCreate
from src.schemas.editorial import EditorialCreate
from src.schemas.autor import AutorCreate
from src.schemas.libro import LibroCreate
from src.schemas.bibliotecario import BibliotecarioCreate
from src.schemas.cliente import ClienteCreate
from src.schemas.prestamo import PrestamoCreate


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
        from src.controller.Autor import get_autores
        from src.controller.editorial import get_editoriales
        
        autores = get_autores(db)
        editoriales = get_editoriales(db)
        
        if not autores or not editoriales:
            print("❌ No se pueden crear libros sin autores y editoriales")
            return
        
        libros_to_create = [
            LibroCreate(
                Codigo_Libro="LIB001",
                Titulo="Cien años de soledad",
                Año="1967",
                Precio="45000",
                Id_Autor=str(autores[0].Id_Autor),
                Id_Editorial=str(editoriales[0].Id_Editorial)
            ),
            LibroCreate(
                Codigo_Libro="LIB002",
                Titulo="La casa de los espíritus",
                Año="1982",
                Precio="38000",
                Id_Autor=str(autores[1].Id_Autor),
                Id_Editorial=str(editoriales[1].Id_Editorial)
            ),
            LibroCreate(
                Codigo_Libro="LIB003",
                Titulo="El Aleph",
                Año="1949",
                Precio="35000",
                Id_Autor=str(autores[2].Id_Autor),
                Id_Editorial=str(editoriales[2].Id_Editorial)
            ),
            LibroCreate(
                Codigo_Libro="LIB004",
                Titulo="La ciudad y los perros",
                Año="1963",
                Precio="42000",
                Id_Autor=str(autores[3].Id_Autor),
                Id_Editorial=str(editoriales[3].Id_Editorial)
            ),
            LibroCreate(
                Codigo_Libro="LIB005",
                Titulo="Rayuela",
                Año="1963",
                Precio="40000",
                Id_Autor=str(autores[4].Id_Autor),
                Id_Editorial=str(editoriales[4].Id_Editorial)
            ),
            LibroCreate(
                Codigo_Libro="LIB006",
                Titulo="Veinte poemas de amor y una canción desesperada",
                Año="1924",
                Precio="28000",
                Id_Autor=str(autores[5].Id_Autor),
                Id_Editorial=str(editoriales[0].Id_Editorial)
            ),
            LibroCreate(
                Codigo_Libro="LIB007",
                Titulo="Como agua para chocolate",
                Año="1989",
                Precio="36000",
                Id_Autor=str(autores[6].Id_Autor),
                Id_Editorial=str(editoriales[1].Id_Editorial)
            ),
            LibroCreate(
                Codigo_Libro="LIB008",
                Titulo="La muerte de Artemio Cruz",
                Año="1962",
                Precio="39000",
                Id_Autor=str(autores[7].Id_Autor),
                Id_Editorial=str(editoriales[2].Id_Editorial)
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


def create_initial_bibliotecarios():
    """Crea bibliotecarios iniciales del sistema."""
    print("\n" + "="*50)
    print("CREANDO BIBLIOTECARIOS INICIALES")
    print("="*50)
    
    db: Session = SessionLocal()
    
    try:
        bibliotecarios_to_create = [
            BibliotecarioCreate(
                Cedula_Bibliotecario="1001234567",
                Nombre="Ana María López",
                Telefono="3101234567",
                Edad="32"
            ),
            BibliotecarioCreate(
                Cedula_Bibliotecario="1002345678",
                Nombre="Carlos Andrés Ramírez",
                Telefono="3102345678",
                Edad="28"
            ),
            BibliotecarioCreate(
                Cedula_Bibliotecario="1003456789",
                Nombre="María Fernanda González",
                Telefono="3103456789",
                Edad="35"
            ),
            BibliotecarioCreate(
                Cedula_Bibliotecario="1004567890",
                Nombre="Juan Pablo Martínez",
                Telefono="3104567890",
                Edad="30"
            ),
            BibliotecarioCreate(
                Cedula_Bibliotecario="1005678901",
                Nombre="Laura Cristina Silva",
                Telefono="3105678901",
                Edad="27"
            ),
        ]

        for bibliotecario in bibliotecarios_to_create:
            try:
                created_biblio = create_bibliotecario(db, bibliotecario)
                print(f"✅ Bibliotecario creado: {created_biblio.Nombre} - Cédula: {created_biblio.Cedula_Bibliotecario}")
            except Exception as e:
                db.rollback()
                print(f"❌ No se pudo crear el bibliotecario {bibliotecario.Nombre}: {e}")
    
    except Exception as e:
        print(f"❌ Error general al crear bibliotecarios: {e}")
    
    finally:
        db.close()


def create_initial_clientes():
    """Crea clientes iniciales del sistema."""
    print("\n" + "="*50)
    print("CREANDO CLIENTES INICIALES")
    print("="*50)
    
    db: Session = SessionLocal()
    
    try:
        clientes_to_create = [
            ClienteCreate(
                Cedula_Cliente="1010123456",
                Nombre="Andrés Felipe Castro",
                Telefono="3201234567",
                Correo="andres.castro@email.com"
            ),
            ClienteCreate(
                Cedula_Cliente="1020234567",
                Nombre="Carolina Gómez Pérez",
                Telefono="3202345678",
                Correo="carolina.gomez@email.com"
            ),
            ClienteCreate(
                Cedula_Cliente="1030345678",
                Nombre="Diego Alejandro Torres",
                Telefono="3203456789",
                Correo="diego.torres@email.com"
            ),
            ClienteCreate(
                Cedula_Cliente="1040456789",
                Nombre="Valentina Rodríguez",
                Telefono="3204567890",
                Correo="valentina.rodriguez@email.com"
            ),
            ClienteCreate(
                Cedula_Cliente="1050567890",
                Nombre="Santiago Muñoz Herrera",
                Telefono="3205678901",
                Correo="santiago.munoz@email.com"
            ),
            ClienteCreate(
                Cedula_Cliente="1060678901",
                Nombre="Sofía Paola Jiménez",
                Telefono="3206789012",
                Correo="sofia.jimenez@email.com"
            ),
            ClienteCreate(
                Cedula_Cliente="1070789012",
                Nombre="Mateo Andrés Vargas",
                Telefono="3207890123",
                Correo="mateo.vargas@email.com"
            ),
            ClienteCreate(
                Cedula_Cliente="1080890123",
                Nombre="Isabella Moreno López",
                Telefono="3208901234",
                Correo="isabella.moreno@email.com"
            ),
        ]

        for cliente in clientes_to_create:
            try:
                created_cliente = create_cliente(db, cliente)
                print(f"✅ Cliente creado: {created_cliente.Nombre} - Cédula: {created_cliente.Cedula_Cliente}")
            except Exception as e:
                db.rollback()
                print(f"❌ No se pudo crear el cliente {cliente.Nombre}: {e}")
    
    except Exception as e:
        print(f"❌ Error general al crear clientes: {e}")
    
    finally:
        db.close()


def create_initial_prestamos():
    """Crea préstamos iniciales del sistema."""
    print("\n" + "="*50)
    print("CREANDO PRÉSTAMOS INICIALES")
    print("="*50)
    
    db: Session = SessionLocal()
    
    try:
        from src.controller.libro import get_libros
        from src.controller.cliente import get_clientes
        from src.controller.bibliotecario import get_bibliotecarios
        
        libros = get_libros(db)
        clientes = get_clientes(db)
        bibliotecarios = get_bibliotecarios(db)
        
        if not libros or not clientes or not bibliotecarios:
            print("❌ No se pueden crear préstamos sin libros, clientes y bibliotecarios")
            return
        
        # Fechas para los préstamos
        hoy = datetime.now()
        
        prestamos_to_create = [
            PrestamoCreate(
                Fecha_Prestamo=hoy - timedelta(days=10),
                Fecha_Devolucion=hoy + timedelta(days=5),
                Estado="Prestado",
                Id_Libro=str(libros[0].Id_Libro),
                Id_Cliente=str(clientes[0].Id_Cliente),
                Id_Bibliotecario=str(bibliotecarios[0].Id_Bibliotecario)
            ),
            PrestamoCreate(
                Fecha_Prestamo=hoy - timedelta(days=8),
                Fecha_Devolucion=hoy + timedelta(days=7),
                Estado="Prestado",
                Id_Libro=str(libros[1].Id_Libro),
                Id_Cliente=str(clientes[1].Id_Cliente),
                Id_Bibliotecario=str(bibliotecarios[1].Id_Bibliotecario)
            ),
            PrestamoCreate(
                Fecha_Prestamo=hoy - timedelta(days=20),
                Fecha_Devolucion=hoy - timedelta(days=5),
                Estado="Devuelto",
                Id_Libro=str(libros[2].Id_Libro),
                Id_Cliente=str(clientes[2].Id_Cliente),
                Id_Bibliotecario=str(bibliotecarios[0].Id_Bibliotecario)
            ),
            PrestamoCreate(
                Fecha_Prestamo=hoy - timedelta(days=5),
                Fecha_Devolucion=hoy + timedelta(days=10),
                Estado="Prestado",
                Id_Libro=str(libros[3].Id_Libro),
                Id_Cliente=str(clientes[3].Id_Cliente),
                Id_Bibliotecario=str(bibliotecarios[2].Id_Bibliotecario)
            ),
            PrestamoCreate(
                Fecha_Prestamo=hoy - timedelta(days=25),
                Fecha_Devolucion=hoy - timedelta(days=10),
                Estado="Devuelto",
                Id_Libro=str(libros[4].Id_Libro),
                Id_Cliente=str(clientes[4].Id_Cliente),
                Id_Bibliotecario=str(bibliotecarios[1].Id_Bibliotecario)
            ),
            PrestamoCreate(
                Fecha_Prestamo=hoy - timedelta(days=3),
                Fecha_Devolucion=hoy + timedelta(days=12),
                Estado="Prestado",
                Id_Libro=str(libros[5].Id_Libro),
                Id_Cliente=str(clientes[5].Id_Cliente),
                Id_Bibliotecario=str(bibliotecarios[3].Id_Bibliotecario)
            ),
            PrestamoCreate(
                Fecha_Prestamo=hoy - timedelta(days=30),
                Fecha_Devolucion=hoy - timedelta(days=15),
                Estado="Devuelto",
                Id_Libro=str(libros[6].Id_Libro),
                Id_Cliente=str(clientes[6].Id_Cliente),
                Id_Bibliotecario=str(bibliotecarios[2].Id_Bibliotecario)
            ),
            PrestamoCreate(
                Fecha_Prestamo=hoy - timedelta(days=1),
                Fecha_Devolucion=hoy + timedelta(days=14),
                Estado="Prestado",
                Id_Libro=str(libros[7].Id_Libro),
                Id_Cliente=str(clientes[7].Id_Cliente),
                Id_Bibliotecario=str(bibliotecarios[4].Id_Bibliotecario)
            ),
        ]

        for i, prestamo in enumerate(prestamos_to_create, 1):
            try:
                created_prestamo = create_prestamo(db, prestamo)
                print(f"✅ Préstamo #{i} creado - Estado: {created_prestamo.Estado}")
            except Exception as e:
                db.rollback()
                print(f"❌ No se pudo crear el préstamo #{i}: {e}")
    
    except Exception as e:
        print(f"❌ Error general al crear préstamos: {e}")
    
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
        create_initial_bibliotecarios()
        create_initial_clientes()
        create_initial_prestamos()
        
        print("\n" + "="*50)
        print("✅ PROCESO COMPLETADO")
        print("="*50 + "\n")

    except Exception as e:
        print(f"\n❌ Error general al crear datos iniciales: {e}\n")


if __name__ == "__main__":
    create_all_initial_data()