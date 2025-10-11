from sqlalchemy.orm import Session

from src.entities.editorial import Editorial


def create_editorial(db: Session, editorial: Editorial):
    new_editorial = Editorial(
        #Id_Editorial=str(editorial.Id_Editorial),
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
        db.query(Editorial)
        .filter(Editorial.Id_Editorial == editorial_id)
        .first()
    )


def get_editoriales(db: Session):
    return db.query(Editorial).all()


def delete_editorial(db: Session, editorial_id: int):
    db_editorial = (
        db.query(Editorial)
        .filter(Editorial.Id_Editorial == editorial_id)
        .first()
    )
    if db_editorial:
        db.delete(db_editorial)
        db.commit()
    return db_editorial
