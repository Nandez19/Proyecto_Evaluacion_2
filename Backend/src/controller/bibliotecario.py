from sqlalchemy.orm import Session
from uuid import UUID 
from sqlalchemy.exc import IntegrityError  
from src.entities.bibliotecario import Bibliotecario  
from src.schemas.bibliotecario import BibliotecarioCreate 

def create_bibliotecario(db: Session, bibliotecario: BibliotecarioCreate):  
    try:
        new_bibliotecario = Bibliotecario(

            Cedula_Bibliotecario=bibliotecario.Cedula_Bibliotecario,
            Nombre=bibliotecario.Nombre,
            Telefono=bibliotecario.Telefono,
            Edad=bibliotecario.Edad,
     
        )
        db.add(new_bibliotecario)
        db.commit()
        db.refresh(new_bibliotecario)
        return new_bibliotecario
    except IntegrityError:
        db.rollback()
        return None 

def get_bibliotecario(db: Session, biblio_id: str):
    try:
        biblio_uuid = UUID(biblio_id)
        return db.query(Bibliotecario).filter(Bibliotecario.Id_Bibliotecario == biblio_uuid).first()
    except ValueError:
        return None

def get_bibliotecarios(db: Session):
    return db.query(Bibliotecario).all()

def update_bibliotecario(db: Session, biblio_id: str, bibliotecario: BibliotecarioCreate):
    try:
        biblio_uuid = UUID(biblio_id)  # Convierte a UUID
        db_bibliotecario = db.query(Bibliotecario).filter(Bibliotecario.Id_Bibliotecario == biblio_uuid).first()
        if db_bibliotecario:
            db_bibliotecario.Cedula_Bibliotecario = bibliotecario.Cedula_Bibliotecario
            db_bibliotecario.Nombre = bibliotecario.Nombre
            db_bibliotecario.Telefono = bibliotecario.Telefono
            db_bibliotecario.Edad = bibliotecario.Edad
            db.commit()
            db.refresh(db_bibliotecario)
        return db_bibliotecario
    except ValueError:
        return None

def delete_bibliotecario(db: Session, biblio_id: str): 
    try:
        biblio_uuid = UUID(biblio_id)  # Convierte a UUID
        db_bibliotecario = db.query(Bibliotecario).filter(Bibliotecario.Id_Bibliotecario == biblio_uuid).first()
        if db_bibliotecario:
            db.delete(db_bibliotecario)
            db.commit()
        return db_bibliotecario
    except ValueError:
        return None