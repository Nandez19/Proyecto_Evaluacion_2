from sqlalchemy.orm import Session

from src.entities.autor import Autor as autor


def create_autor(db: Session, autor: autor):
    new_autor = autor(
        Id_Autor=str(autor.Id_Autor),
        Cedula_Autor=autor.Cedula_Autor,
        Nombre=autor.Nombre,
        Telefono=autor.Telefono,
        Edad=autor.Edad
    )
    db.add(new_autor)
    db.commit()
    db.refresh(new_autor)
    return new_autor


def get_autor(db: Session, autor_id: int):
    return (
        db.query(autor)
        .filter(autor.Id_Autor == autor_id)
        .first()
    )


def get_autores(db: Session):
    return db.query(autor).all()


def delete_autor(db: Session, autor_id: int):
    db_autor = (
        db.query(autor)
        .filter(autor.Id_Autor == autor_id)
        .first()
    )
    if db_autor:
        db.delete(db_autor)
        db.commit()
    return db_autor
