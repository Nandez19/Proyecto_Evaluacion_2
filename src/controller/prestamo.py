from sqlalchemy.orm import Session

from src.entities.prestamo import Prestamo as prestamo


def create_prestamo(db: Session, prestamo: prestamo):
    new_prestamo = prestamo(
        Id_Prestamo=str(prestamo.Id_Prestamo),
        Fecha_Prestamo=prestamo.Fecha_Prestamo,
        Fecha_Devolucion=prestamo.Fecha_Devolucion,
        Estado=prestamo.Estado,
        Id_Bilbiotecario=str(prestamo.Id_Bibliotecario),
        Id_Usuario=str(prestamo.Id_Usuario)
    )
    db.add(new_prestamo)
    db.commit()
    db.refresh(new_prestamo)
    return new_prestamo


def get_prestamo(db: Session, prestamo_id: int):
    return (
        db.query(prestamo)
        .filter(prestamo.Id_Prestamo == prestamo_id)
        .first()
    )


def get_prestamos(db: Session):
    return db.query(prestamo).all()


def delete_prestamo(db: Session, prestamo_id: int):
    db_prestamo = (
        db.query(prestamo)
        .filter(prestamo.Id_Prestamo == prestamo_id)
        .first()
    )
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo
