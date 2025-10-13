from sqlalchemy.orm import Session

from src.entities.prestamo import Prestamo 


def create_prestamo(db: Session, prestamo: Prestamo):
    new_prestamo = Prestamo(
        #Id_Prestamo=str(prestamo.Id_Prestamo),
        Fecha_Prestamo=prestamo.Fecha_Prestamo,
        Fecha_Devolucion=prestamo.Fecha_Devolucion,
        Estado=prestamo.Estado,
        Id_Bibliotecario=str(prestamo.Id_Bibliotecario),
        Id_Cliente=str(prestamo.Id_Cliente)
    )
    db.add(new_prestamo)
    db.commit()
    db.refresh(new_prestamo)
    return new_prestamo


def get_prestamo(db: Session, prestamo_id: int):
    return (
        db.query(Prestamo)
        .filter(Prestamo.Id_Prestamo == prestamo_id)
        .first()
    )


def get_prestamos(db: Session):
    return db.query(Prestamo).all()


def update_prestamo(db: Session, prestamo_id: int, prestamo: Prestamo):
    db_prestamo = (
        db.query(Prestamo)
        .filter(Prestamo.Id_Prestamo == prestamo_id)
        .first()
    )
    if db_prestamo:
        db_prestamo.Fecha_Prestamo = prestamo.Fecha_Prestamo
        db_prestamo.Fecha_Devolucion = prestamo.Fecha_Devolucion
        db_prestamo.Estado = prestamo.Estado
        db_prestamo.Id_Bibliotecario = str(prestamo.Id_Bibliotecario)
        db_prestamo.Id_Cliente = str(prestamo.Id_Cliente)
        db.commit()
        db.refresh(db_prestamo)
    return db_prestamo



def delete_prestamo(db: Session, prestamo_id: int):
    db_prestamo = (
        db.query(Prestamo)
        .filter(Prestamo.Id_Prestamo == prestamo_id)
        .first()
    )
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo
