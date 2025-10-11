from sqlalchemy.orm import Session

from src.entities.cliente import Cliente 


def create_cliente(db: Session, cliente: Cliente):
    new_cliente = Cliente(
        #Id_Cliente=str(cliente.Id_Cliente),
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
