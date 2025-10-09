from sqlalchemy.orm import Session

from src.entities.usuario import Usuario as usuario


def create_usuario(db: Session, usuario: usuario):
    new_usuario = usuario(
        Id_Usuario=str(usuario.Id_Usuario),
        Cedula_Usuario=usuario.Cedula_Usuario,
        Nombre=usuario.Nombre,
        Telefono=usuario.Telefono,
        Correo=usuario.Correo,
        Password_Hash=usuario.Password_Hash,
        Rol=usuario.Rol
        
    )
    db.add(new_usuario)
    db.commit()
    db.refresh(new_usuario)
    return new_usuario


def get_usuario(db: Session, usuario_id: int):
    return (
        db.query(usuario)
        .filter(usuario.Id_Usuario == usuario_id)
        .first()
    )


def get_usuarios(db: Session):
    return db.query(usuario).all()


def delete_usuario(db: Session, usuario_id: int):
    db_usuario = (
        db.query(usuario)
        .filter(usuario.Id_Usuario == usuario_id)
        .first()
    )
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario
