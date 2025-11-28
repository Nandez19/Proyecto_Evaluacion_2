from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.entities.autor import Autor
from src.schemas.autor import AutorCreate


def create_autor(db: Session, autor: AutorCreate):
    """
    Crea un nuevo autor en la base de datos.
    Maneja IntegrityError para cédulas duplicadas.
    """
    try:
        new_autor = Autor(

            Cedula_Autor=autor.Cedula_Autor,
            Nombre=autor.Nombre,
            Telefono=autor.Telefono,
            Edad=autor.Edad,

        )
        db.add(new_autor)
        db.commit()
        db.refresh(new_autor)
        return new_autor
    except IntegrityError:
        db.rollback()  
        return None  


def get_autor(db: Session, autor_id: int):
    return db.query(Autor).filter(Autor.Id_Autor == autor_id).first()


def get_autores(db: Session):
    return db.query(Autor).all()


def update_autor(db: Session, autor_id: int, autor: Autor):
    db_autor = db.query(Autor).filter(Autor.Id_Autor == autor_id).first()
    if db_autor:
        db_autor.Cedula_Autor = autor.Cedula_Autor
        db_autor.Nombre = autor.Nombre
        db_autor.Telefono = autor.Telefono
        db_autor.Edad = autor.Edad
        db.commit()
        db.refresh(db_autor)
    return db_autor


def delete_autor(db: Session, autor_id: int):
    db_autor = db.query(Autor).filter(Autor.Id_Autor == autor_id).first()
    if db_autor:
        db.delete(db_autor)
        db.commit()
    return db_autor
