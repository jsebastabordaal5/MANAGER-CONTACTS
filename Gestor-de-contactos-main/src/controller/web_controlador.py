from fastapi import APIRouter, Request, Form, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.model.usuario import Usuario
from src.model.gestor_usuarios import GestorUsuarios
from src.model.contacto import Contacto
from src.model.sistema import Sistema
from src.model.errores import (
    ErrorUsuarioYaExistente, ContraseñaVaciaError, NombreVacioError,
    ErrorUsuarioInexistente, ContraseñaIncorrectaError, NombreInvalidoError,
    ErrorUsuarioNulo, ErrorTipoInvalidoUsuario, ErrorArchivoInexistente , ErrorFormatoArchivoInvalido
)

class UsuarioInput(BaseModel):
    """Modelo para datos de entrada de usuario."""
    nombre: str
    contraseña: str

class ContactoInput(BaseModel):
    """Modelo para datos de entrada de contacto."""
    tipo: str
    nombre: str
    telefono: str

class EditarContactoInput(BaseModel):
    """Modelo para datos de entrada al editar un contacto."""
    nombre_original: str
    tipo: str
    nombre: str
    telefono: str

class ExportarInput(BaseModel):
    """Modelo para datos de entrada al exportar contactos."""
    nombre_usuario: str
    ruta_archivo: str

class ImportarInput(BaseModel):
    """Modelo para datos de entrada al importar contactos."""
    nombre_usuario: str
    ruta_archivo: str

class WebControlador:
    """Controlador de rutas web de la API para gestionar usuarios y contactos."""

    def __init__(self):
        """Inicializa el router y el sistema."""
        self.router = APIRouter(prefix="/api/v1")
        self.sistema : Sistema = Sistema(usar_db = usar_db)
        self.__registrar_rutas()

    def __registrar_rutas(self):
        """Registra todas las rutas disponibles en la API."""

        @self.router.post("/registrar")
        def registrar_usuario(usuario_input: UsuarioInput):
            """Registra un nuevo usuario en el sistema."""
            try:
                nuevo_usuario = Usuario(usuario_input.nombre, usuario_input.contraseña)
                self.sistema.gestor_usuarios.registrar_usuario(nuevo_usuario)
                return {"mensaje": "Usuario registrado correctamente"}
            except (ErrorUsuarioNulo, ErrorTipoInvalidoUsuario, ErrorUsuarioYaExistente,
                    NombreVacioError, ContraseñaVaciaError, NombreInvalidoError) as e:
                raise HTTPException(status_code=400, detail=str(e))

        @self.router.post("/login")
        def iniciar_sesion(usuario_input: UsuarioInput):
            """Inicia sesión de un usuario. Retorna mensaje de éxito si es válido."""
            try:
                usuario = self.sistema.gestor_usuarios.iniciar_sesion(usuario_input.nombre, usuario_input.contraseña)
                if usuario:
                    return {"mensaje": "Inicio de sesión exitoso", "nombre": usuario.nombre}
            except (NombreVacioError, ContraseñaVaciaError,
                    ErrorUsuarioInexistente, ContraseñaIncorrectaError) as e:
                raise HTTPException(status_code=401, detail=str(e))

        @self.router.post("/contactos/exportar")
        def exportar_contactos(input_data: ExportarInput):
            """Exporta los contactos de un usuario a un archivo."""
            usuario = self.sistema.gestor_usuarios.obtener_usuario_por_nombre(input_data.nombre_usuario)
            if not usuario:
                raise HTTPException(status_code=401, detail="Usuario no encontrado.")
            try:
                usuario.gestor.exportar_contactos(input_data.ruta_archivo)
                return {"mensaje": f"Contactos exportados correctamente a {input_data.ruta_archivo}"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error al exportar contactos: {str(e)}")

        @self.router.post("/contactos/importar")
        def importar_contactos(input_data: ImportarInput):
            """Importa contactos desde un archivo para un usuario."""
            usuario = self.sistema.gestor_usuarios.obtener_usuario_por_nombre(input_data.nombre_usuario)
            if not usuario:
                raise HTTPException(status_code=401, detail="Usuario no encontrado.")
            try:
                usuario.gestor.importar_contactos(input_data.ruta_archivo)
                return {"mensaje": f"Contactos importados correctamente desde {input_data.ruta_archivo}"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error al importar contactos: {str(e)}")

        @self.router.post("/contactos/registrar")
        def registrar_contacto(
            tipo: str = Form(...),
            nombre: str = Form(...),
            telefono: str = Form(...),
            nombre_usuario: str = Form(...)
        ):
            """Registra un nuevo contacto para un usuario."""
            usuario = self.sistema.gestor_usuarios.obtener_usuario_por_nombre(nombre_usuario)
            if not usuario:
                raise HTTPException(status_code=401, detail="No hay ningún usuario logueado.")
            try:
                contacto = Contacto(tipo, nombre, telefono)
                usuario.gestor.registrar_contacto(contacto)
                return {"mensaje": "Contacto registrado correctamente", "contacto": contacto.__dict__}
            except Exception as e:
                raise HTTPException(status_code=400, detail="Error al registrar contacto: " + str(e))

        @self.router.get("/contactos")
        def ver_contactos(nombre_usuario: str):
            """Devuelve la lista de contactos del usuario."""
            usuario = self.sistema.gestor_usuarios.obtener_usuario_por_nombre(nombre_usuario)
            if not usuario:
                raise HTTPException(status_code=401, detail="No hay ningún usuario logueado.")
            contactos = usuario.gestor.ver_contactos()
            return [c.__dict__ for c in contactos]

        @self.router.post("/contactos/editar")
        def editar_contacto(
            nombre_original: str = Form(...),
            tipo: str = Form(...),
            nombre: str = Form(...),
            telefono: str = Form(...),
            nombre_usuario: str = Form(...)
        ):
            """Edita un contacto existente de un usuario."""
            usuario = self.sistema.gestor_usuarios.obtener_usuario_por_nombre(nombre_usuario)
            if not usuario:
                raise HTTPException(status_code=401, detail="No hay usuario logueado.")
            contactos = usuario.gestor.ver_contactos()
            contacto_original = next((c for c in contactos if c.nombre == nombre_original), None)
            if not contacto_original:
                raise HTTPException(status_code=404, detail="Contacto no encontrado.")
            try:
                contacto_modificado = usuario.gestor.editar_contacto(
                    contacto_original,
                    nuevo_tipo=tipo,
                    nuevo_nombre=nombre,
                    nuevo_telefono=telefono
                )
                return {"mensaje": "Contacto editado correctamente", "contacto": contacto_modificado.__dict__}
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))
