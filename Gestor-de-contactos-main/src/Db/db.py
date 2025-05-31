"""
Modelos ORM para la base de datos de usuarios y contactos.
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class UsuarioDB(Base):
    """
    Modelo de tabla para usuarios.

    Atributos:
        id_usuario (int): ID único del usuario.
        nombre (str): Nombre del usuario (único).
        contrasena (str): Contraseña del usuario.
        contactos (list[ContactoDB]): Lista de contactos asociados.
    """
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    contrasena = Column(String, nullable=False)

    contactos = relationship("ContactoDB", back_populates="usuario")

    def __repr__(self):
        return f"Usuario {self.id_usuario}.{self.nombre} -- {self.contrasena}"

class ContactoDB(Base):
    """
    Modelo de tabla para contactos.

    Atributos:
        id_contacto (int): ID único del contacto.
        nombre (str): Nombre del contacto.
        telefono (str): Número de teléfono.
        tipo (str): Tipo de contacto (ej: familiar, trabajo, etc.).
        id_usuario (int): ID del usuario propietario.
        usuario (UsuarioDB): Relación inversa con el usuario.
    """
    __tablename__ = 'contactos'

    id_contacto = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))

    usuario = relationship("UsuarioDB", back_populates="contactos")

    def __repr__(self):
        return f"{self.id_contacto}.{self.tipo} -- {self.nombre} -- {self.telefono} -- ID Usuarios: {self.id_usuario}"
