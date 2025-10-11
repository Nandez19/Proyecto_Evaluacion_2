from sqlalchemy.orm import Session

from src.entities.libro import Libro 


def create_libro(db: Session, libro: Libro):
    new_libro = Libro(
        #Id_Libro=str(libro.Id_Libro),
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
        db.query(Libro)
        .filter(Libro.Id_Libro == libro_id)
        .first()
    )


def get_libros(db: Session):
    return db.query(Libro).all()


def delete_libro(db: Session, libro_id: int):
    db_libro = (
        db.query(Libro)
        .filter(Libro.Id_Libro == libro_id)
        .first()
    )
    if db_libro:
        db.delete(db_libro)
        db.commit()
    return db_libro
