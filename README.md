# 📇 GestorDeContactos

El objetivo de este proyecto es desarrollar una aplicación para la gestión de contactos personales y profesionales, permitiendo almacenar, organizar y manipular información de manera eficiente.

---

![image](https://github.com/user-attachments/assets/8fa9f15b-096e-41f3-ae8b-4964b2bee244)

---

# 📌 Requisitos:

---

# 1. Crear un contacto

📝 *El sistema debe permitir al usuario crear un contacto.*

---

## ✅ Caso de prueba 1: Caso normal
| Tipo       | Nombre           | Teléfono    |
|------------|------------------|-------------|
| "Personal" | "Juan Sebastián" | "3226130937" |

---

## ✅ Caso de prueba 2: Caso normal
| Tipo         | Nombre       | Teléfono    |
|--------------|--------------|-------------|
| "Profesional" | "Tomás Henao" | "3146272068" |

---

## ✅ Caso de prueba 3: Caso normal
| Tipo         | Nombre         | Teléfono    |
|--------------|----------------|-------------|
| "Profesional" | "Daniel Olarte" | "3148122216" |

---

## ⚠️ Caso de prueba 4: Nombre con más de 12 caracteres
| Tipo         | Nombre                                         | Teléfono    |
|--------------|------------------------------------------------|-------------|
| "Profesional" | "Daniel Olarte Pérez Valencia Villa Andrade"   | "3148122216" |

---

## ⚠️ Caso de prueba 5: Teléfono con más de 10 dígitos
| Tipo       | Nombre         | Teléfono          |
|------------|----------------|-------------------|
| "Personal" | "Samuel Flórez" | "99999999999999999" |

---

## ⚠️ Caso de prueba 6: Nombre con un solo carácter
| Tipo       | Nombre | Teléfono      |
|------------|--------|---------------|
| "Personal" | "Y"    | "331 2498 3127" |

---

## ❌ Caso de prueba 7: Tipo de contacto inválido
| Tipo      | Nombre         | Teléfono      | Error                          |
|-----------|----------------|---------------|--------------------------------|
| "Parcero" | "Juan González" | "331 2498 3127" | Error! Tipo de contacto inválido |

---

## ❌ Caso de prueba 8: Datos NO numéricos
| Tipo         | Nombre         | Teléfono        | Error                |
|--------------|----------------|-----------------|----------------------|
| "Profesional" | "Juan Mecánico" | "313 812 149916" | Error! Contiene letras |

---

## ❌ Caso de prueba 9: Campos vacíos

| Tipo         | Nombre | Teléfono        | Error               |
|--------------|--------|-----------------|---------------------|
| "Profesional" | ""     | "313 812 149916" | Error! Campo vacío  |

| Tipo         | Nombre           | Teléfono | Error               |
|--------------|------------------|----------|---------------------|
| "Profesional" | "Felipe Sánchez" | ""       | Error! Campo vacío  |

| Tipo | Nombre           | Teléfono        | Error               |
|------|------------------|-----------------|---------------------|
| ""   | "Felipe Sánchez" | "313 812 149916" | Error! Campo vacío  |








---

# 2. ✏️ Editar un contacto

🛠️ *El sistema debe permitir al usuario editar la información de un contacto.*

---

## ✅ Caso de prueba 1: Caso normal - Editar tipo de contacto

**Contacto original:**
| Tipo       | Nombre  | Teléfono   |
|------------|---------|------------|
| "personal" | "samuel" | "300222398" |

**Al editar:**
| Valor a cambiar | Nuevo valor   |
|-----------------|---------------|
| "tipo"          | "profesional" |

**Resultado:**
| Tipo         | Nombre  | Teléfono   |
|--------------|---------|------------|
| "profesional" | "samuel" | "300222398" |

---

## ✅ Caso de prueba 2: Caso normal - Editar nombre de contacto

**Contacto original:**
| Tipo       | Nombre  | Teléfono   |
|------------|---------|------------|
| "personal" | "samuel" | "300222398" |

**Al editar:**
| Valor a cambiar | Nuevo valor |
|-----------------|-------------|
| "nombre"        | "juan"      |

**Resultado:**
| Tipo       | Nombre | Teléfono   |
|------------|--------|------------|
| "personal" | "juan" | "300222398" |

---

## ✅ Caso de prueba 3: Caso normal - Editar número de contacto

**Contacto original:**
| Tipo       | Nombre  | Teléfono   |
|------------|---------|------------|
| "personal" | "samuel" | "300222398" |

**Al editar:**
| Valor a cambiar | Nuevo valor  |
|-----------------|--------------|
| "telefono"      | "3005680588" |

**Resultado:**
| Tipo       | Nombre  | Teléfono    |
|------------|---------|-------------|
| "personal" | "samuel" | "3005680588" |

---

## ⚠️ Caso de prueba 4: Caso extremo - Editar con nombre muy corto

**Contacto original:**
| Tipo       | Nombre  | Teléfono   |
|------------|---------|------------|
| "personal" | "samuel" | "300222398" |

**Al editar:**
| Valor a cambiar | Nuevo valor |
|-----------------|-------------|
| "nombre"        | "a"         |

**Resultado:**
| Error |
|-------|
| "Error: El nombre es demasiado corto. Debe tener al menos 3 caracteres" |

---

## ⚠️ Caso de prueba 5: Caso extremo - Teléfono muy largo

**Contacto original:**
| Tipo       | Nombre  | Teléfono   |
|------------|---------|------------|
| "personal" | "samuel" | "300222398" |

**Al editar:**
| Valor a cambiar | Nuevo valor           |
|-----------------|------------------------|
| "telefono"      | "1234567898765432123"  |

**Resultado:**
| Error |
|-------|
| "Error: El número de teléfono debe tener exactamente 10 dígitos" |

---

## ⚠️ Caso de prueba 6: Caso extremo - Teléfono inválido

**Contacto original:**
| Tipo       | Nombre  | Teléfono   |
|------------|---------|------------|
| "personal" | "samuel" | "300222398" |

**Al editar:**
| Valor a cambiar | Nuevo valor |
|-----------------|-------------|
| "telefono"      | "1"         |

**Resultado:**
| Error |
|-------|
| "Error: El número de teléfono debe tener exactamente 10 dígitos" |

---

## ❌ Caso de prueba 7: Error - Contacto no existente

**Contacto:**
| Tipo | Nombre | Teléfono |
|------|--------|----------|
|      |        |          |

**Al editar:**
| Error |
|-------|
| "Error: El contacto no fue encontrado" |

---

## ❌ Caso de prueba 8: Error - Sin valores a editar

**Contacto original:**
| Tipo       | Nombre  | Teléfono   |
|------------|---------|------------|
| "personal" | "samuel" | "300222398" |

**Al editar:**
| Nuevo tipo | Nuevo Nombre | Nuevo Teléfono |
|------------|---------------|----------------|
|            |               |                |

**Resultado:**
| Error |
|-------|
| "Error: Debe proporcionar al menos un dato para modificar el contacto" |

---

## ❌ Caso de prueba 9: Error - Nombre vacío

**Contacto original:**
| Tipo       | Nombre  | Teléfono   |
|------------|---------|------------|
| "personal" | "samuel" | "300222398" |

**Al editar:**
| Nuevo tipo | Nuevo Nombre | Nuevo Teléfono |
|------------|----------------|----------------|
|            | " "            |                |

**Resultado:**
| Error |
|-------|
| "Error: El nombre no puede ser un campo vacío" |



---

# 3. 🔍 Filtrar un contacto por nombre y categoría

📂 *El sistema debe permitir al usuario filtrar la lista de contactos por nombre y categoría.*

---

## ✅ Caso de prueba 1: Filtrar contactos por nombre

**Filtro aplicado:**
| Nombre: |
|---------|
| Carlos  |

**Resultado:**
| Tipo      | Nombre         | Teléfono   |
|-----------|----------------|------------|
| "personal" | "Carlos Pérez" | "555123456" |
| "personal" | "Carlos Gómez" | "555987654" |

---

## ✅ Caso de prueba 2: Filtrar contactos por teléfono

**Filtro aplicado:**
| Teléfono:     |
|---------------|
| "555123456"   |

**Resultado:**
| Tipo      | Nombre         | Teléfono   |
|-----------|----------------|------------|
| "personal" | "Carlos Pérez" | "555123456" |

---

## ✅ Caso de prueba 3: Filtrar contactos por tipo

**Filtro aplicado:**
| Tipo:         |
|---------------|
| "profesional" |

**Resultado:**
| Tipo         | Nombre         | Teléfono   |
|--------------|----------------|------------|
| "profesional" | "Ana López"    | "555654321" |
| "profesional" | "Carlos Gómez" | "555987654" |

---

## ⚠️ Caso extremo 4: Filtrar por parte del teléfono

**Filtro aplicado:**
| Teléfono: |
|-----------|
| "56"      |

**Resultado:**
| Tipo         | Nombre         | Teléfono   |
|--------------|----------------|------------|
| "personal"    | "Carlos Pérez" | "555123456" |
| "profesional" | "Ana López"    | "555654321" |

---

## ⚠️ Caso extremo 5: Filtrar por parte del nombre

**Filtro aplicado:**
| Nombre: |
|---------|
| "Car"   |

**Resultado:**
| Tipo         | Nombre         | Teléfono   |
|--------------|----------------|------------|
| "personal"    | "Carlos Pérez" | "555123456" |
| "profesional" | "Carlos Gómez" | "555987654" |

---

## ⚠️ Caso extremo 6: Filtrar contactos del mismo tipo

**Filtro aplicado:**
| Tipo:         |
|---------------|
| "Profesional" |

**Resultado:**
| Tipo         | Nombre         | Teléfono   |
|--------------|----------------|------------|
| "profesional" | "Carlos Gómez" | "555987654" |
| "profesional" | "Mateo Acevedo" | "34566172" |
| "profesional" | "Robert Jesus"  | "889006755" |

---

## ❌ Caso de error 7: Filtrar por criterio inexistente

**Filtro aplicado:**
| Edad: |
|-------|
| 29    |

**Resultado:**
| Error                         |
|------------------------------|
| Error! Criterio inexistente! |

---

## ❌ Caso de error 8: Nombre con carácter inválido

**Filtro aplicado:**
| Nombre: |
|---------|
| C@rlos  |

**Resultado:**
| Error                                   |
|----------------------------------------|
| Error! Nombre con caracteres incorrectos |

---

## ❌ Caso de error 9: Teléfono con dígitos inválidos

**Filtro aplicado:**
| Teléfono:      |
|----------------|
| "abc 123 cde"  |

**Resultado:**
| Error                                 |
|--------------------------------------|
| Error! Teléfono con dígitos incorrectos |




---

# 4. 📤📥 Exportar e importar contactos en formato vCards (.vcf)

🗂️ *El sistema debe permitir al usuario exportar contactos a un archivo `.vcf` e importarlos desde dicho formato.*

---

## ✅ Caso de prueba 1: Exportar contacto (caso normal)

**Contacto:**
| Tipo      | Nombre  | Teléfono   |
|-----------|---------|------------|
| "personal" | "samuel" | "300222398" |

**Acción:** Se ejecuta `exportar_contactos`

**Resultado:**
BEGIN:VCARD  
FN:samuel  
TEL:300222398  
CATEGORIES:personal  
END:VCARD


**Acción:** Se ejecuta `importar_contactos`

**Resultado:**
| Error lanzado                                                         |
|------------------------------------------------------------------------|
| Error: El archivo no tiene un formato VCF válido. Verifique el contenido y la estructura. |


---

# 5. 👤 Crear un usuario

🆕 *El sistema debe permitir al usuario darse de alta (registrarse).*

---

## ✅ Caso de prueba 1: Registrar un usuario (caso normal)

**Usuario:**
| Nombre de Usuario | Contraseña     |
|-------------------|----------------|
| "juan"            | "password123"  |

**Validación esperada:**
| Validación                | Resultado Esperado     |
|---------------------------|------------------------|
| Cantidad de usuarios en lista | 1 usuario en lista     |

---

## ✅ Caso de prueba 2: Registrar múltiples usuarios

**Usuarios:**
| Nombre de Usuario | Contraseña     |
|-------------------|----------------|
| "juan"            | "password123"  |
| "maria"           | "password321"  |

**Validación esperada:**
| Validación                | Resultado Esperado     |
|---------------------------|------------------------|
| Cantidad de usuarios en lista | 2 usuarios en lista    |

---

## ✅ Caso de prueba 3: Registrar usuarios similares

**Usuarios:**
| Nombre de Usuario | Contraseña     |
|-------------------|----------------|
| "juan1"           | "password123"  |
| "juan"            | "password12"   |

**Validación esperada:**
| Validación                | Resultado Esperado     |
|---------------------------|------------------------|
| Cantidad de usuarios en lista | 2 usuarios en lista    |

---

## ⚠️ Caso extremo 4: Intentar registrar el mismo nombre de usuario dos veces

**Usuarios:**
| Nombre de Usuario | Contraseña     |
|-------------------|----------------|
| "juan"            | "password123"  |
| "juan"            | "otraClave456" |

**Validación esperada:**
| Validación                | Resultado Esperado     |
|---------------------------|------------------------|
| Cantidad de usuarios en lista | 1 usuario en lista     |

---

## ⚠️ Caso extremo 5: Registrar usuario con caracteres especiales

**Usuario:**
| Nombre de Usuario   | Contraseña   |
|---------------------|--------------|
| "J@hn_Doe 123"       | "P@ssw0rd!"  |

**Validación esperada:**
| Validación                | Resultado Esperado     |
|---------------------------|------------------------|
| Cantidad de usuarios en lista | 1 usuario en lista     |

---

## ⚠️ Caso extremo 6: Registrar usuario con espacios en los campos

**Entrada original:**
| Nombre de Usuario               | Contraseña                     |
|--------------------------------|--------------------------------|
| "   usuario con espacios   "   | "   contraseña con espacios   " |

**Resultado esperado (después de limpiar espacios):**
| Nombre de Usuario         | Contraseña               |
|---------------------------|--------------------------|
| "usuario con espacios"    | "contraseña con espacios"|

---

## ❌ Caso de error 7: Registrar usuario nulo

**Datos de entrada:**
| Usuario |
|---------|
| `None`  |

**Resultado esperado:**
| Error                                              |
|---------------------------------------------------|
| Error: No se puede registrar un usuario nulo. Verifique los datos de entrada |

---

## ❌ Caso de error 8: Registrar usuario ya registrado

**Usuarios:**
| Nombre            | Contraseña       |
|-------------------|------------------|
| usuarioRepetido   | contraseña123    |
| usuarioRepetido   | otracontraseña   |

**Resultado esperado:**
| Error                                                      |
|------------------------------------------------------------|
| Error: El usuario ya está registrado. Elija un nombre diferente |

---

## ❌ Caso de error 9: Intentar registrar un tipo de dato inválido

**Datos de entrada:**
| Tipo de dato proporcionado | Valor                                       |
|----------------------------|---------------------------------------------|
| `str`                      | "Este es un string, no un objeto Usuario"   |

**Resultado esperado:**
| Error                                                   |
|----------------------------------------------------------|
| Error: Debes proporcionar un objeto de tipo Usuario     |



---

# 6. 🔐 Iniciar sesión

*El sistema debe permitir al usuario iniciar sesión para ver la lista de sus contactos.*

---

## ✅ Caso de prueba normal #1: Credenciales correctas

| Nombre | Contraseña | Resultado           |
|--------|------------|---------------------|
| "juan" | "12345"    | Ingreso exitoso     |

---

## ✅ Caso de prueba normal #2: Iniciar sesión luego de registrarse

| Nombre | Contraseña | Resultado           |
|--------|------------|---------------------|
| "juan" | "12345"    | Registro exitoso    |

| Sesión iniciada |

---

## ✅ Caso de prueba normal #3: Iniciar sesión después de cerrar sesión

*Sesión cerrada!*

| Nombre | Contraseña | Resultado           |
|--------|------------|---------------------|
| "juan" | "12345"    | Ingreso exitoso     |

---

## ⚠️ Caso de prueba extremo #4: Credenciales extremadamente largas

| Nombre                              | Contraseña         |
|-----------------------------------|--------------------|
| "juan garzón garzón villa sanchez" | "123456gsuyh2tn_@" |

---

## ⚠️ Caso de prueba extremo #5: Credenciales en mayúsculas o minúsculas

| Nombre | Contraseña         |
|--------|--------------------|
| "Juan" | "ClaveSegura123"   |

| Nombre | Contraseña         |
|--------|--------------------|
| "juan" | "clavesegura123"   |

---

## ⚠️ Caso de prueba extremo #6: Iniciar sesión en diferentes dispositivos

### Dispositivo 1:
| Nombre | Contraseña |
|--------|------------|
| "juan" | "12345"    |

### Dispositivo 2:
| Nombre | Contraseña |
|--------|------------|
| "juan" | "12345"    |

---

## ❌ Caso de error #7: Usuario inexistente

| Nombre               | Contraseña | Resultado                    |
|----------------------|------------|------------------------------|
| "usuario inexistente" | "clave123" | !Error, Usuario inexistente! |

---

## ❌ Caso de error #8: Contraseña vacía

| Nombre | Contraseña | Resultado             |
|--------|------------|-----------------------|
| "juan" | " "        | !Error, Contraseña vacía! |

---

## ❌ Caso de error #9: Nombre vacío

| Nombre | Contraseña  | Resultado          |
|--------|-------------|--------------------|
| ""     | " 12345 "   | !Error, nombre vacío! |



## 📘 Instrucciones de Uso

### 1. 🖥️ Formas de Visualización del Sistema
Nuestro proyecto cuenta con **tres formas de visualización o interacción** con el sistema. Cada una tiene su archivo correspondiente para ejecutarse:

- **Menú por consola:**  
  Ejecute el archivo llamado `app`.

- **Interfaz gráfica de usuario (GUI):**  
  Ejecute el archivo llamado `app_gui`.

- **Interfaz web:**  
  Ejecute el archivo llamado `app_web`.

---

### 2. 🧑‍💻 Creación de Usuario e Inicio de Sesión
- Antes de comenzar, debe **crear un usuario**.
- Una vez registrado, **inicie sesión** con sus credenciales.

> 🧪 **Nota:**  
> En la base de datos ya existen varios usuarios con sus respectivos contactos cargados.  
> Puede utilizar el siguiente usuario para probar rápidamente la aplicación:
> - **Usuario:** juan  
> - **Contraseña:** clave123

---

### 3. 🛠️ Opciones Disponibles
- Después de iniciar sesión, podrá ver la **lista de opciones disponibles** en el sistema.

---

### 4. 📥 Importar Contactos
Para importar contactos al sistema, siga estos pasos:

1. Ingrese la **ruta del archivo** que desea importar.  
2. Para obtener la ruta del archivo:
   - Busque el archivo en su explorador de archivos.
   - Haga clic derecho sobre el archivo.
   - Seleccione **"Copiar ruta"** o **"Copiar dirección"**.
   - Pegue la ruta en el campo correspondiente del sistema.  
3. Solo se permiten archivos en formato **vCard (.vcf)**.  
4. Si no cuenta con un archivo `.vcf`, dentro de la carpeta del proyecto  
   (al mismo nivel que carpetas como `src` y archivos como `app`)  
   encontrará dos archivos de prueba:  
   - `contactos_prueba`  
   - `contactos_prueba_2`  
   Ambos tienen la estructura válida de un archivo `.vcf` y pueden ser usados para probar la funcionalidad de importación.

---

### 5. 📤 Exportar Contactos
Para exportar los contactos del sistema:

- Ingrese el **nombre que desea asignar al archivo exportado**.
- El archivo será guardado en la **carpeta del proyecto**.
- Si no lo encuentra, revise otras subcarpetas del sistema.
- Puede abrir el archivo generado con un editor de texto como **Bloc de notas**.

---

### 6. 📦 Integración con Base de Datos
Nuestro sistema está integrado con **base de datos** con el fin de tener persistencia de los datos.

- Tenemos un **script para la creación de la base de datos** ubicado en la ruta:  
  `src/Db`

- Para alternar entre **usar o no la base de datos**, hemos creado un atributo llamado `usar_db`, que controla este comportamiento:
  - Cuando `usar_db == True`, se **usará la base de datos**.
  - Cuando `usar_db == False`, el sistema **no la utilizará**.

- Para cambiar este valor a su gusto:
  - Diríjase al archivo correspondiente a la forma en que desea ejecutar la aplicación (`app`, `app_gui` o `app_web`).
  - En algún lugar del código encontrará algo como:
    ```python
    usar_db = True
    ```
  - **Cámbielo a `False` si no desea utilizar la base de datos.**

---

**Importante:**  
En la ruta `src/Db` encontrará un archivo llamado `conexion_db.py`.  
En ese archivo se encuentra la **URL o ruta de conexión** a la base de datos.  
Es muy probable que deba **modificar dicha ruta** según la configuración de su equipo.

---

✅ Asegúrese de seguir los pasos correctamente para garantizar una buena experiencia de uso.




















