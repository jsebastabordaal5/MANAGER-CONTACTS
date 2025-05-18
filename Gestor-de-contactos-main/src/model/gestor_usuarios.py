from src.model.usuario import Usuario
from src.model.errores import ErrorUsuarioYaExistente, ContraseñaVaciaError, NombreVacioError, ErrorUsuarioInexistente, ContraseñaIncorrectaError, NombreInvalidoError, ErrorUsuarioNulo, ErrorTipoInvalidoUsuario
from src.Db.usuario_db import registrar_usuario , autenticar_usuario


class GestorUsuarios:

    def __init__(self,usar_db = False):
        self.usuarios: list[Usuario] = []
        self.usar_db= usar_db


    def registrar_usuario(self, usuario: Usuario):

        if usuario == None:
            raise ErrorUsuarioNulo()

        if not isinstance(usuario, Usuario):
            raise ErrorTipoInvalidoUsuario()
        
        if self.usar_db:
            if not registrar_usuario(usuario.nombre, usuario.contraseña):
                raise ErrorUsuarioYaExistente(usuario.nombre)
            return
            

        for user in self.usuarios:
            if user.nombre.strip().lower() == usuario.nombre.strip().lower():
                raise ErrorUsuarioYaExistente(usuario.nombre)

        self.usuarios.append(usuario)
        return

    def iniciar_sesion(self, nombre: str, contraseña: str) -> Usuario | None:
        if not nombre:
            raise NombreVacioError("El nombre de usuario no puede estar vacío.")

        if not contraseña:
            raise ContraseñaVaciaError("La contraseña no puede estar vacía.")
        
        if self.usar_db:
            usuario = autenticar_usuario(nombre, contraseña)
            if usuario:
                print("Sesión iniciada exitosamente")
                return usuario
            else:
                raise ErrorUsuarioInexistente()

        for usuario in self.usuarios:
            if usuario.nombre.lower() == nombre.lower():  # Ignorar mayúsculas/minúsculas
                if usuario.contraseña == contraseña:
                    print("Sesión iniciada exitosamente")
                    return usuario
                else:
                    raise ContraseñaIncorrectaError()

        raise ErrorUsuarioInexistente()

    def cerrar_sesion(self) -> None:
        print("sesión cerrada")

    def eliminar_usuario(self, nombre: str) -> None:
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                self.usuarios.delete(usuario)
                print(f"Usuario{usuario.nombre} eliminado correctamente")
            else:
                print("El usuario no fue encontrado")

