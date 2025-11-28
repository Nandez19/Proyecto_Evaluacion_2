from sqlalchemy.orm import Session
from uuid import UUID 
from sqlalchemy.exc import IntegrityError 
from src.entities.cliente import Cliente  
from src.schemas.cliente import ClienteCreate  

def create_cliente(db: Session, cliente: ClienteCreate):
    """
    Crea un nuevo cliente en la base de datos.
    Maneja IntegrityError para cédulas o correos duplicados.
    """
    try:
        new_cliente = Cliente(

            Cedula_Cliente=cliente.Cedula_Cliente,
            Nombre=cliente.Nombre,
            Telefono=cliente.Telefono,
            Correo=cliente.Correo,
        )
        db.add(new_cliente)
        db.commit()
        db.refresh(new_cliente)
        return new_cliente
    except IntegrityError:
    
        db.rollback()  
        return None  

def get_cliente(db: Session, cliente_id: str):
    """
    Obtiene un cliente por ID (convierte string a UUID).
    """
    try:
        cliente_uuid = UUID(cliente_id)  # Convierte la string del endpoint a UUID
        return db.query(Cliente).filter(Cliente.Id_Cliente == cliente_uuid).first()
    except ValueError:
        return None  

def get_clientes(db: Session):
    """
    Obtiene todos los clientes.
    """
    return db.query(Cliente).all()

def update_cliente(db: Session, cliente_id: str, cliente: ClienteCreate):
    """
    Actualiza un cliente por ID (convierte string a UUID).
    """
    try:
        cliente_uuid = UUID(cliente_id)  # Convierte a UUID
        db_cliente = db.query(Cliente).filter(Cliente.Id_Cliente == cliente_uuid).first()
        if db_cliente:
            db_cliente.Cedula_Cliente = cliente.Cedula_Cliente
            db_cliente.Nombre = cliente.Nombre
            db_cliente.Telefono = cliente.Telefono
            db_cliente.Correo = cliente.Correo
            db.commit()
            db.refresh(db_cliente)
        return db_cliente
    except ValueError:
        return None

def delete_cliente(db: Session, cliente_id: str):
    """
    Elimina un cliente por ID (convierte string a UUID).
    """
    try:
        cliente_uuid = UUID(cliente_id)  # Convierte a UUID
        db_cliente = db.query(Cliente).filter(Cliente.Id_Cliente == cliente_uuid).first()
        if db_cliente:
            db.delete(db_cliente)
            db.commit()
        return db_cliente
    except ValueError:
        return None