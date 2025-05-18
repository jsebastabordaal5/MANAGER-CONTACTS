from src.Db.conexion_db import Session
from src.Db.db import UsuarioDB, ContactoDB
from src.model.contacto import Contacto

def guardar_contacto(nombre_usuario, contacto):
    session = Session()
    usuario_db = session.query(UsuarioDB).filter_by(nombre=nombre_usuario).first()
    if usuario_db:
        nuevo = ContactoDB(
            nombre=contacto.nombre,
            telefono=contacto.telefono,
            tipo=contacto.tipo,
            usuario=usuario_db
        )
        session.add(nuevo)
        session.commit()
    session.close()

def obtener_contactos(nombre_usuario):
    session = Session()
    usuario_db = session.query(UsuarioDB).filter_by(nombre=nombre_usuario).first()
    contactos = []
    if usuario_db:
        for c in usuario_db.contactos:
            contactos.append(Contacto(c.tipo, c.nombre, c.telefono))
    session.close()
    return contactos


def actualizar_contacto(nombre_usuario: str, contacto_obj, nombre_anterior: str):
    session = Session()

    usuario_db = session.query(UsuarioDB).filter_by(nombre=nombre_usuario).first()
    if not usuario_db:
        print(f"No se encontró el usuario '{nombre_usuario}' en la base de datos.")
        session.close()
        return

    contacto_db = session.query(ContactoDB).filter_by(
        nombre=nombre_anterior,
        usuario_id=usuario_db.id_usuario
    ).first()

    if contacto_db:
        contacto_db.nombre = contacto_obj.nombre
        contacto_db.telefono = contacto_obj.telefono
        contacto_db.tipo = contacto_obj.tipo
        session.commit()
        print(f"Contacto '{nombre_anterior}' actualizado correctamente.")
    else:
        print(f"No se encontró el contacto '{nombre_anterior}' para el usuario '{nombre_usuario}' en la base de datos.")
    
    session.close()


