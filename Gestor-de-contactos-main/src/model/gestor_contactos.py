"""
Clase GestorContactos: Maneja contactos, incluyendo registro, edición, importación, exportación y filtrado.
"""

class GestorContactos:
    """
    Administra la lista de contactos de un usuario.

    Métodos:
        ver_contactos() - Muestra y devuelve todos los contactos.
        registrar_contacto(contacto) - Registra un nuevo contacto con validaciones.
        editar_contacto(contacto, ...) - Modifica campos específicos de un contacto.
        importar_contactos(archivo) - Importa contactos desde archivo VCF.
        exportar_contactos(nombre_archivo) - Exporta los contactos a formato VCF.
        filtrar_contactos(criterio, valor) - Devuelve una lista filtrada de contactos.
    """

    def __init__(self, nombre_usuario=None, usar_db=False):
        """
        Inicializa el gestor de contactos.

        Args:
            nombre_usuario (str): Nombre del usuario dueño de los contactos.
            usar_db (bool): Indica si se usa base de datos.
        """
        self.nombre_usuario = nombre_usuario
        self.usar_db = usar_db
        if usar_db and nombre_usuario:
            self.contactos = obtener_contactos(nombre_usuario)
        else:
            self.contactos: list[Contacto] = []

    def ver_contactos(self):
        """
        Muestra por consola y retorna la lista de contactos guardados.

        Returns:
            list[Contacto]: Lista de contactos existentes.
        """
        if not self.contactos:
            print("No hay contactos guardados.")
            return

        lista_aux = []

        print("\nLista de Contactos:")
        for i, contacto in enumerate(self.contactos, start=1):
            print(f"{i}. {contacto.tipo} - {contacto.nombre} ({contacto.telefono})")
            lista_aux.append(contacto)

        return lista_aux

    def registrar_contacto(self, contacto: Contacto):
        """
        Valida y registra un nuevo contacto en la lista o base de datos.

        Args:
            contacto (Contacto): Contacto a registrar.

        Returns:
            Contacto: El contacto registrado.

        Raises:
            CampoVacioError, DatosNoNumericosError, NombreInvalidoError,
            NumeroInvalidoError, TipoContactoError
        """
        if contacto.nombre.strip() == "" or contacto.tipo.strip() == "" or contacto.telefono.strip() == "":
            raise CampoVacioError()

        if not contacto.telefono.isdigit():
            raise DatosNoNumericosError(contacto.telefono)

        if len(contacto.nombre) < 30 and len(contacto.nombre) > 0:
            if 10 <= len(contacto.telefono) <= 12:
                if contacto.tipo.lower() in ["profesional", "personal"]:
                    self.contactos.append(contacto)
                    if self.usar_db:
                        guardar_contacto(self.nombre_usuario, contacto)
                    return contacto
                else:
                    raise TipoContactoError(contacto.tipo)
            else:
                raise NumeroInvalidoError()
        else:
            raise NombreInvalidoError()

    def editar_contacto(self, contacto: Contacto, nuevo_tipo: str = None, nuevo_nombre: str = None, nuevo_telefono: str = None):
        """
        Edita los datos de un contacto existente.

        Args:
            contacto (Contacto): Contacto a modificar.
            nuevo_tipo (str, optional): Nuevo tipo.
            nuevo_nombre (str, optional): Nuevo nombre.
            nuevo_telefono (str, optional): Nuevo número de teléfono.

        Returns:
            Contacto: El contacto actualizado.

        Raises:
            NombreVacioError, DatosInsuficientesError, ContactoNoEncontradoError,
            NombreCortoError, NumeroInvalidoError
        """
        if nuevo_nombre is not None and nuevo_nombre.strip() == "":
            raise NombreVacioError()

        if not nuevo_nombre and not nuevo_tipo and not nuevo_telefono:
            raise DatosInsuficientesError()

        if self.usar_db:
            from src.Db.usuario_db import obtener_usuario_por_nombre
            session = Session()
            usuario = obtener_usuario_por_nombre(self.nombre_usuario)
            if not usuario:
                session.close()
                return

            contacto_db = session.query(ContactoDB).filter_by(
                nombre=contacto.nombre,
                telefono=contacto.telefono,
                tipo=contacto.tipo,
                id_usuario=usuario.id_usuario
            ).first()

            if not contacto_db:
                raise ContactoNoEncontradoError(contacto)

            if nuevo_nombre:
                if len(nuevo_nombre.strip()) < 3:
                    raise NombreCortoError()
                contacto_db.nombre = nuevo_nombre.strip()
                contacto.nombre = nuevo_nombre

            if nuevo_telefono:
                if not nuevo_telefono.isdigit() or not 10 <= len(nuevo_telefono.strip()) <= 12:
                    raise NumeroInvalidoError()
                contacto_db.telefono = nuevo_telefono.strip()
                contacto.telefono = nuevo_telefono

            if nuevo_tipo:
                if nuevo_tipo.strip().lower() not in ["profesional", "personal"]:
                    print("⚠️ El tipo debe ser 'profesional' o 'personal'")
                else:
                    contacto_db.tipo = nuevo_tipo.strip()
                    contacto.tipo = nuevo_tipo

            session.commit()
            session.close()
            return

        if contacto not in self.contactos:
            raise ContactoNoEncontradoError(contacto)

        if nuevo_nombre:
            if len(nuevo_nombre.strip()) < 3:
                raise NombreCortoError()
            contacto.nombre = nuevo_nombre.strip()

        if nuevo_telefono:
            if not nuevo_telefono.isdigit() or not 10 <= len(nuevo_telefono.strip()) <= 12:
                raise NumeroInvalidoError()
            contacto.telefono = nuevo_telefono.strip()

        if nuevo_tipo:
            if nuevo_tipo.strip().lower() not in ["profesional", "personal"]:
                print("⚠️ El tipo debe ser 'profesional' o 'personal'")
            else:
                contacto.tipo = nuevo_tipo.strip()

        return contacto

    def importar_contactos(self, archivo):
        """
        Importa contactos desde un archivo .vcf.

        Args:
            archivo (str): Ruta al archivo.

        Raises:
            ErrorArchivoInexistente, ErrorFormatoArchivoInvalido
        """
        archivo = archivo.strip().strip('"').strip("'")
        if not os.path.isabs(archivo):
            archivo = os.path.abspath(archivo)

        if not os.path.exists(archivo):
            raise ErrorArchivoInexistente(archivo)

        with open(archivo, "r", encoding="utf-8") as file:
            contenido = file.read().strip()

        if not contenido:
            return

        if "FN:" not in contenido or "TEL:" not in contenido or "CATEGORIES:" not in contenido:
            raise ErrorFormatoArchivoInvalido(archivo)

        with open(archivo, "r", encoding="utf-8") as file:
            contactos_temporales = []
            nombre = telefono = tipo = None

            for linea in file:
                linea = linea.strip()
                if linea.startswith("BEGIN:VCARD"):
                    nombre = telefono = tipo = None
                elif linea.startswith("FN:"):
                    nombre = linea[3:]
                elif linea.startswith("TEL:"):
                    telefono = linea[4:]
                elif linea.startswith("CATEGORIES:"):
                    tipo = linea[11:]
                elif linea.startswith("END:VCARD"):
                    if nombre and telefono and tipo:
                        contacto = Contacto(tipo, nombre, telefono)
                        contactos_temporales.append(contacto)

            for contacto in contactos_temporales:
                if contacto not in self.contactos:
                    self.contactos.append(contacto)
                    if self.usar_db:
                        guardar_contacto(self.nombre_usuario, contacto)

            print(f"Se importaron {len(self.contactos)} contactos correctamente.")

    def exportar_contactos(self, nombre_archivo: str):
        """
        Exporta los contactos actuales a un archivo .vcf.

        Args:
            nombre_archivo (str): Nombre del archivo destino.

        Raises:
            ErrorSinContactos: Si no hay contactos para exportar.
        """
        if not self.contactos:
            raise ErrorSinContactos()

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for contacto in self.contactos:
                vcard = (
                    f"BEGIN:VCARD\n"
                    f"FN:{contacto.nombre}\n"
                    f"TEL:{contacto.telefono}\n"
                    f"CATEGORIES:{contacto.tipo}\n"
                    f"END:VCARD\n"
                )
                archivo.write(vcard)

    def filtrar_contactos(self, criterio: str, valor: str) -> list[Contacto]:
        """
        Filtra los contactos en base al criterio especificado.

        Args:
            criterio (str): Campo por el cual filtrar ('nombre', 'telefono', 'tipo').
            valor (str): Valor a buscar.

        Returns:
            list[Contacto]: Contactos que cumplen con el criterio.

        Raises:
            ErrorCriterioInexistente, ErrorNombreCaracterInvalido, DatosNoNumericosError
        """
        criterios_validos = ["nombre", "telefono", "tipo"]
        if criterio not in criterios_validos:
            raise ErrorCriterioInexistente(
                f"El criterio '{criterio}' no es válido. Debe ser 'nombre', 'telefono' o 'tipo'.")

        if criterio == "nombre" and not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", valor):
            raise ErrorNombreCaracterInvalido(f"El nombre '{valor}' contiene caracteres no permitidos.")

        if criterio == "telefono" and not valor.isdigit():
            raise DatosNoNumericosError(f"El teléfono '{valor}' contiene caracteres no numéricos.")

        contactos_filtrados = []
        for contacto in self.contactos:
            if criterio == "tipo" and contacto.tipo.lower() == valor.lower():
                contactos_filtrados.append(contacto)
            elif criterio == "nombre" and valor.lower() in contacto.nombre.lower():
                contactos_filtrados.append(contacto)
            elif criterio == "telefono" and valor in contacto.telefono:
                contactos_filtrados.append(contacto)

        return contactos_filtrados
