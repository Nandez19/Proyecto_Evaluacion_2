from sqlalchemy.orm import Session

from src.entities.editorial import Editorial as editorial


def create_editorial(db: Session, editorial: editorial):
    new_editorial = editorial(
        Id_Editorial=str(editorial.Id_Editorial),
        Nombre=editorial.Nombre,
        Pais=editorial.Pais,
        Contacto=editorial.Contacto
    )
    db.add(new_editorial)
    db.commit()
    db.refresh(new_editorial)
    return new_editorial


def get_editorial(db: Session, editorial_id: int):
    return (
        db.query(editorial)
        .filter(editorial.Id_Editorial == editorial_id)
        .first()
    )


def get_editoriales(db: Session):
    return db.query(editorial).all()


def delete_editorial(db: Session, editorial_id: int):
    db_editorial = (
        db.query(editorial)
        .filter(editorial.Id_Editorial == editorial_id)
        .first()
    )
    if db_editorial:
        db.delete(db_editorial)
        db.commit()
    return db_editorial
