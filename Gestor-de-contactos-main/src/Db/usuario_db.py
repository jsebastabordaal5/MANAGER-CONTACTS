from src.Db.conexion_db import Session
from src.Db.db import UsuarioDB, ContactoDB
from src.model.usuario import Usuario
from src.model.contacto import Contacto
from src.model.gestor_contactos import GestorContactos


def registrar_usuario(nombre, contrasena):
    session = Session()
    if session.query(UsuarioDB).filter_by(nombre=nombre).first():
        session.close()
        return None  # Ya existe
    nuevo = UsuarioDB(nombre=nombre, contrasena=contrasena)
    session.add(nuevo)
    session.commit()
    session.close()
    return True


def autenticar_usuario(nombre: str, contraseña: str):
    session = Session()
    usuario_db = session.query(UsuarioDB).filter_by(nombre=nombre, contrasena=contraseña).first()
    
    if not usuario_db:
        session.close()
        return None

    usuario = Usuario(usuario_db.nombre, usuario_db.contrasena,usar_db=True)
    
    session.close()

    return usuario

def obtener_id_usuario(nombre_usuario):
    usuario = obtener_usuario_por_nombre(nombre_usuario)
    if usuario:
        return usuario.id_usuario
    return None

def obtener_usuario_por_nombre(nombre_usuario: str):
    session = Session()
    try:
        usuario = session.query(UsuarioDB).filter_by(nombre=nombre_usuario).first()
        return usuario
    finally:
        session.close()