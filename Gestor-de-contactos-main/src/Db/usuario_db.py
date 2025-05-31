"""
Módulo para manejar operaciones relacionadas con usuarios en la base de datos.
"""

from src.Db.conexion_db import Session
from src.Db.db import UsuarioDB, ContactoDB
from src.model.usuario import Usuario
from src.model.contacto import Contacto
from src.model.gestor_contactos import GestorContactos

def registrar_usuario(nombre, contrasena):
    """
    Registra un nuevo usuario en la base de datos.

    Args:
        nombre (str): Nombre del usuario.
        contrasena (str): Contraseña del usuario.

    Returns:
        bool or None: True si el usuario fue registrado, None si el usuario ya existe.
    """
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
    """
    Autentica un usuario con nombre y contraseña.

    Args:
        nombre (str): Nombre del usuario.
        contraseña (str): Contraseña del usuario.

    Returns:
        Usuario or None: Objeto Usuario si es válido, None si no existe.
    """
    session = Session()
    usuario_db = session.query(UsuarioDB).filter_by(nombre=nombre, contrasena=contraseña).first()
    if not usuario_db:
        session.close()
        return None

    usuario = Usuario(usuario_db.nombre, usuario_db.contrasena, usar_db=True)
    session.close()
    return usuario

def obtener_id_usuario(nombre_usuario):
    """
    Obtiene el ID de un usuario dado su nombre.

    Args:
        nombre_usuario (str): Nombre del usuario.

    Returns:
        int or None: ID del usuario, o None si no se encuentra.
    """
    usuario = obtener_usuario_por_nombre(nombre_usuario)
    if usuario:
        return usuario.id_usuario
    return None

def obtener_usuario_por_nombre(nombre_usuario: str):
    """
    Obtiene un objeto UsuarioDB dado su nombre.

    Args:
        nombre_usuario (str): Nombre del usuario.

    Returns:
        UsuarioDB or None: Objeto de la base de datos o None si no se encuentra.
    """
    session = Session()
    try:
        usuario = session.query(UsuarioDB).filter_by(nombre=nombre_usuario).first()
        return usuario
    finally:
        session.close()
