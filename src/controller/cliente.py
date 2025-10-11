from sqlalchemy.orm import Session

from src.entities.cliente import Cliente 

def create_cliente(db: Session, cliente: Cliente):
    new_cliente = Cliente(
        Cedula_Cliente=cliente.Cedula_Cliente,
        Nombre=cliente.Nombre,
        Telefono=cliente.Telefono,
        Correo=cliente.Correo
    )
    db.add(new_cliente)
    db.commit()
    db.refresh(new_cliente)
    return new_cliente

def get_cliente(db: Session, cliente_id: int):
    return (
        db.query(Cliente)
        .filter(Cliente.Id_Cliente == cliente_id)
        .first()
    )

def get_clientes(db: Session):
    return db.query(Cliente).all()

def update_cliente(db: Session, cliente_id: int, cliente: Cliente):
    db_cliente = (
        db.query(Cliente)
        .filter(Cliente.Id_Cliente == cliente_id)
        .first()
    )
    if db_cliente:
        db_cliente.Cedula_Cliente = cliente.Cedula_Cliente
        db_cliente.Nombre = cliente.Nombre
        db_cliente.Telefono = cliente.Telefono
        db_cliente.Correo = cliente.Correo
        db.commit()
        db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, cliente_id: int):
    db_cliente = (
        db.query(Cliente)
        .filter(Cliente.Id_Cliente == cliente_id)
        .first()
    )
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente