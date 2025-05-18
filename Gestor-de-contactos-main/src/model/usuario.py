from src.model.gestor_contactos import GestorContactos
from src.model.contacto import Contacto
class Usuario:
    def __init__(self, nombre : str , contraseña : str , usar_db : bool= False ):
        self.nombre= nombre.strip()
        self.contraseña = contraseña.strip()
        self.gestor= GestorContactos(nombre_usuario=nombre , usar_db= usar_db)
        

    def __str__(self):
        return f"Nombre: {self.nombre}, Contraseña : {self.contraseña}"

