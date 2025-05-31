from src.model.usuario import Usuario
from src.model.errores import ErrorUsuarioYaExistente, ContraseñaVaciaError, NombreVacioError, ErrorUsuarioInexistente, ContraseñaIncorrectaError, NombreInvalidoError, ErrorUsuarioNulo, ErrorTipoInvalidoUsuario
from src.Db.usuario_db import registrar_usuario , autenticar_usuario


class GestorUsuarios:
    """
    Clase encargada de gestionar operaciones relacionadas con usuarios: registro, autenticación, cierre y eliminación.
    Puede trabajar tanto en memoria como con base de datos.
    """

    def __init__(self, usar_db = False):
        """
        Inicializa el gestor de usuarios, indicando si se usará almacenamiento en base de datos o en memoria.
        """
        self.usuarios: list[Usuario] = []
        self.usar_db = usar_db

    def registrar_usuario(self, usuario: Usuario):
        """
        Registra un nuevo usuario, validando su tipo, existencia previa y si la base de datos está activa.
        En caso de estar en modo local, añade el usuario a la lista si no hay duplicados.
        """
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
        """
        Inicia sesión para un usuario si el nombre y la contraseña coinciden.
        Realiza la validación en la base de datos si está activa, o en la lista local si no.
        """
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
        """
        Finaliza la sesión del usuario activo mostrando un mensaje en consola.
        """
        print("sesión cerrada")

    def eliminar_usuario(self, nombre: str) -> None:
        """
        Elimina un usuario de la lista local si se encuentra por su nombre.
        Informa si fue encontrado o no.
        """
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                self.usuarios.delete(usuario)
                print(f"Usuario{usuario.nombre} eliminado correctamente")
            else:
                print("El usuario no fue encontrado")


