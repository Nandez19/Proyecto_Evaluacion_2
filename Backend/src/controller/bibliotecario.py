from sqlalchemy.orm import Session

from src.entities.bibliotecario import Bibliotecario


def create_bibliotecario(db: Session, bibliotecario: Bibliotecario):
    new_bibliotecario = Bibliotecario(
        # Id_Bibliotecario=str(bibliotecario.Id_Bibliotecario),
        Cedula_Bibliotecario=bibliotecario.Cedula_Bibliotecario,
        Nombre=bibliotecario.Nombre,
        Telefono=bibliotecario.Telefono,
        Edad=bibliotecario.Edad,
    )
    db.add(new_bibliotecario)
    db.commit()
    db.refresh(new_bibliotecario)
    return new_bibliotecario


def get_bibliotecario(db: Session, bibliotecario_id: int):
    return (
        db.query(Bibliotecario)
        .filter(Bibliotecario.Id_Bibliotecario == bibliotecario_id)
        .first()
    )


def get_bibliotecarios(db: Session):
    return db.query(Bibliotecario).all()


def update_bibliotecario(
    db: Session, bibliotecario_id: int, bibliotecario: Bibliotecario
):
    db_bibliotecario = (
        db.query(Bibliotecario)
        .filter(Bibliotecario.Id_Bibliotecario == bibliotecario_id)
        .first()
    )
    if db_bibliotecario:
        db_bibliotecario.Cedula_Bibliotecario = bibliotecario.Cedula_Bibliotecario
        db_bibliotecario.Nombre = bibliotecario.Nombre
        db_bibliotecario.Telefono = bibliotecario.Telefono
        db_bibliotecario.Edad = bibliotecario.Edad
        db.commit()
        db.refresh(db_bibliotecario)
    return db_bibliotecario


def delete_bibliotecario(db: Session, bibliotecario_id: int):
    db_bibliotecario = (
        db.query(Bibliotecario)
        .filter(Bibliotecario.Id_Bibliotecario == bibliotecario_id)
        .first()
    )
    if db_bibliotecario:
        db.delete(db_bibliotecario)
        db.commit()
    return db_bibliotecario
