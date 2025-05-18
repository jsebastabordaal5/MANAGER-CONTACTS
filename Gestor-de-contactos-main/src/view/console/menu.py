from src.model.sistema import Sistema
from src.model.usuario import Usuario
from src.model.contacto import Contacto
from src.model.gestor_contactos import GestorContactos
from src.model.gestor_usuarios import GestorUsuarios

class Menu:
    def __init__(self, sistema: Sistema):
        self.sistema = sistema

    def mostrar_menu(self):
        while True:
            print("\n📌 MENÚ PRINCIPAL")
            print("1️⃣  Registrar usuario")
            print("2️⃣  Iniciar sesión")
            print("3️⃣  Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.iniciar_sesion()
            elif opcion == "3":
                print("👋 Saliendo del sistema...\n")
                break
            else:
                print("⚠️ Opción no válida. Intente de nuevo.")

    def registrar_usuario(self):
        nombre = str(input("Ingrese el nombre de usuario:"))
        contraseña = str(input("Ingrese una contraseña:"))
        usuario = Usuario(nombre, contraseña)
        self.sistema.gestor_usuarios.registrar_usuario(usuario)
        print("✅ Usuario registrado correctamente.")
        return

    def iniciar_sesion(self):
        nombre = input("Ingrese nombre de usuario: ")
        contrasena = input("Ingrese contraseña: ")
        usuario = self.sistema.gestor_usuarios.iniciar_sesion(nombre, contrasena)
        if usuario:
            if isinstance(usuario, Usuario):
                self.opciones_usuario(usuario)

    def opciones_usuario(self, usuario: Usuario):
        while True:
            print(f"\n👤 MENÚ DE USUARIO ({usuario.nombre})")
            print("1️⃣  Crear contacto")
            print("2️⃣  Ver contacto")
            print("3️⃣  Editar contactos")
            print("4️⃣  Filtrar contactos")
            print("5️⃣  Exportar contactos")
            print("6️⃣  Importar contactos")
            print("7️⃣  Cerrar sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_contacto(usuario)
            elif opcion == "2":
                usuario.gestor.ver_contactos()
            elif opcion == "3":
                self.editar_contacto(usuario)
            elif opcion == "4":
                self.filtrar_contacto(usuario)
            elif opcion == "5":
                nombre_archivo = input("Ingrese el nombre del archivo para exportar: ")
                usuario.gestor.exportar_contactos(nombre_archivo)

            elif opcion == "6":
                ruta_archivo = input("Ingrese la ubicación del archivo que desea importar: ").strip().replace('"', '')
                usuario.gestor.importar_contactos(ruta_archivo)

            elif opcion == "7":
                self.sistema.gestor_usuarios.cerrar_sesion()
                print("🚪 Sesión cerrada.")
                break
            else:
                print("⚠️ Opción no válida. Intente de nuevo.")

    def crear_contacto(self, usuario):
        tipo = input("Ingrese tipo de contacto (Personal o profesional): ")
        nombre = input("Ingrese nombre del contacto: ")
        telefono = input("Ingrese teléfono del contacto: ")
        contacto = Contacto(tipo, nombre, telefono)
        usuario.gestor.registrar_contacto(contacto)

    def editar_contacto(self, usuario: Usuario):
        contactos = usuario.gestor.ver_contactos()
        if not contactos:
            print("⚠️ No hay contactos disponibles para editar.")
            return

        try:
            seleccion = int(input("Seleccione el número del contacto a editar: "))
            if 1 <= seleccion <= len(contactos):
                contacto = contactos[seleccion - 1]
            else:
                print("⚠️ Número fuera de rango.")
                return
        except ValueError:
            print("⚠️ Entrada inválida. Debe ingresar un número.")
            return

        nuevo_nombre = input("Ingrese el nuevo nombre (Deje vacío para no cambiar): ")
        if nuevo_nombre == "":
            nuevo_nombre = None

        nuevo_telefono = input("Ingrese el nuevo teléfono (Deje vacío para no cambiar): ")
        if nuevo_telefono == "":
            nuevo_telefono = None

        nuevo_tipo = input("Ingrese el nuevo tipo (Deje vacío para no cambiar): ")
        if nuevo_tipo == "":
            nuevo_tipo = None

        usuario.gestor.editar_contacto(contacto, nuevo_tipo, nuevo_nombre, nuevo_telefono)
        print("✅ Contacto editado correctamente.")


        print("\n✅ Fin de la lista de contactos.")

    def filtrar_contacto(self, usuario: Usuario):
        print("\n🔍 Filtrar contactos")
        print("1. Filtrar por nombre")
        print("2. Filtrar por teléfono")
        print("3. Filtrar por tipo")

        opcion = input("Elige un criterio (1-3): ").strip()
        criterios = {"1": "nombre", "2": "telefono", "3": "tipo"}

        if opcion not in criterios:
            print("⚠️ Opción inválida. Inténtalo de nuevo.")
            return

        criterio = criterios[opcion]
        valor = input(f"Ingrese el {criterio} que desea buscar: ").strip()

        # Llamamos a la función de filtrado
        resultados = usuario.gestor.filtrar_contactos(criterio, valor)

        if not resultados:
            print(f"⚠️ No se encontraron contactos con {criterio}: {valor}")
            return

        print("\n📋 Contactos encontrados:")
        for idx, contacto in enumerate(resultados, start=1):
            print(f"{idx}. {contacto.tipo} - {contacto.nombre} - {contacto.telefono}")

        print("\n✅ Fin de los resultados.")

# Inicializar y ejecutar el menú del sistema
# if __name__ == "__main__":
#     sistema = Sistema()
#     menu = Menu(sistema)
#     menu.mostrar_menu()