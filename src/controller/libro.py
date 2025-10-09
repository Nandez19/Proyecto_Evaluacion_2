from sqlalchemy.orm import Session

from src.entities.libro import Libro as libro


def create_libro(db: Session, libro: libro):
    new_libro = libro(
        Id_Libro=str(libro.Id_Libro),
        Codigo_Libro=libro.Codigo_Libro,
        Titulo=libro.Titulo,
        Año=libro.Año,
        Precio=libro.Precio,
        Id_Autor=str(libro.Id_Autor),
        Id_Editorial=str(libro.Id_Editorial),
        Id_Prestamo=str(libro.Id_Prestamo)
    )
    db.add(new_libro)
    db.commit()
    db.refresh(new_libro)
    return new_libro


def get_libro(db: Session, libro_id: int):
    return (
        db.query(libro)
        .filter(libro.Id_Libro == libro_id)
        .first()
    )


def get_libros(db: Session):
    return db.query(libro).all()


def delete_libro(db: Session, libro_id: int):
    db_libro = (
        db.query(libro)
        .filter(libro.Id_Libro == libro_id)
        .first()
    )
    if db_libro:
        db.delete(db_libro)
        db.commit()
    return db_libro
