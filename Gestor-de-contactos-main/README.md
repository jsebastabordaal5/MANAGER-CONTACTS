# GestorDeContactos
El objetivo de este proyecto es desarrollar una aplicación para la gestión de contactos personales y profesionales, permitiendo almacenar, organizar y manipular información de manera eficiente




![image](https://github.com/user-attachments/assets/8fa9f15b-096e-41f3-ae8b-4964b2bee244)



# Requisitos:


# 1. Crear un contacto:
El sistema debe permitir al usuario crear un contacto.

## Caso de prueba 1: Caso normal:
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Personal" | "Juan Sebastián" | "3226130937" |

## Caso de prueba 2: Caso normal:
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Profesional" | "Tomás Henao" | "3146272068" |

## Caso de prueba 3: Caso normal:
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Profesional" | "Daniel Olarte" | "3148122216" |


## Caso de prueba 4: Nombre con más de 12 caracteres:
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Profesional" | "Daniel Olarte Pérez Valencia Villa Andrade" | "3148122216" |


## Caso de prueba 5: Teléfono con más de 10 dígitos:
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Personal" | "Samuel Flórez" | "99999999999999999" |


## Caso de prueba 6: Nombre con un sólo caracter:
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Personal" | "Y" | "331 2498 3127" |


## Caso de prueba 7: Tipo de Contacto Inválido:
| Tipo | Nombre | Teléfono | Error           |
|------|--------|----------|----------|
| "Parcero" | "Juan González" | "331 2498 3127" | Error! Tipo de contacto Inválido|



## Caso de prueba 8: Datos NO numéricos:
| Tipo | Nombre | Teléfono | Error           |
|------|--------|----------|----------|
| "Profesional" | "Juan Mecánico" | "313 812 149916" | Error! Contiene letras|



## Caso de prueba 9: Campos vacíos:
| Tipo | Nombre | Teléfono | Error           |
|------|--------|----------|----------|
| "Profesional" | "" | "313 812 149916" | Error! Campo Vacío|


| Tipo | Nombre | Teléfono | Error           |
|------|--------|----------|----------|
| "Profesional" | "Felipe Sánchez" | "" | Error! Campo vacío|


| Tipo | Nombre | Teléfono | Error           |
|------|--------|----------|----------|
| "" | "Felipe Sánchez" | "313 812 149916" | Error! Campo vacío|








# 2. Editar un contacto:
El sistema debe permitir al usuario editar la informacion de un contacto

## Caso de prueba 1: Caso normal-Editar tipo de contacto:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
|Valor a cambiar| Nuevo valor|
|---------------|------------|
| "tipo" | "profesional"| 

Resultado:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "profesional" | "samuel" | "300222398" |


## Caso de prueba 2: Caso normal- Editar nombre de contacto :
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
|Valor a cambiar| Nuevo valor|
|---------------|------------|
| "nombre" | "juan"| 

Resultado:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "juan" | "300222398" |

## Caso de prueba 3: Caso normal-Editar numero de contacto:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
|Valor a cambiar| Nuevo valor|
|---------------|------------|
| "telefono" | "3005680588"| 

Resultado:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "3005680588" |

## Caso de prueba 4: Caso Extremo-Editar contacto con nombre muy corto:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
|Valor a cambiar| Nuevo valor|
|---------------|------------|
| "nombre" | "a"| 

Resultado:
| Eror|
|------|
| "Error: El nombre es demasiado corto. Debe tener al menos 3 caracteres" |

## Caso de prueba 5: Caso Extremo-Editar contacto con telefono muy largo:

Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
|Valor a cambiar| Nuevo valor|
|---------------|------------|
| "telefono" | "1234567898765432123"| 

Resultado:
| Error|
|------|
| "Error: El número de teléfono debe tener exactamente 10 dígitos |


## Caso de prueba 6: Caso Extremo-Editar contacto con telefono ivalido:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
|Valor a cambiar| Nuevo valor|
|---------------|------------|
| "telefono" | "1"| 

Resultado:
| Error|
|------|
| "Error: El número de teléfono debe tener exactamente 10 dígitos |


## Caso de prueba 7: Caso Error-Editar contacto no existente:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
|      |       |        |

Al editar:
| Error|
|------|
| "Error: El contacto no fue encontrado"|


## Caso de prueba 8: Caso Error-Editar contacto sin valores:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
| nuevo tipo |nuevo Nombre | nuevo Teléfono|
|------|--------|---------|
|      |       |        |

Resultado:
| Error|
|------|
| "Error: Debe proporcionar al menos un dato para modificar el contacto|


## Caso de prueba 9 : Caso Error-Editar contacto nombre vacio:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
| nuevo tipo |nuevo Nombre | nuevo Teléfono|
|------|--------|---------|
|      |    " "   |        |

Resultado:
| Error|
|------|
| "Error: El nombre no puede ser un campo vacio|





# 3. Filtrar un contacto por nombre y categoría:
El sistema debe permitir al usuario filtrar la
lista de contactos por nombre y categoría.


## Caso de prueba Normal 1: Filtrar contactos por nombre:

| Nombre: | Carlos |
|------|--------|

| "personal" | "Carlos Pérez" | "555123456" |
| "personal" | "Carlos Gómez" | "555987654" |
|------|--------|---------|



## Caso de prueba Normal 2: Filtrar contactos por teléfono:
| Teléfono: | "555123456" |
|------|--------|

| "personal" | "Carlos Pérez" | "555123456" |
|------|--------|---------|



## Caso de prueba normal 3: Filtrar contactos por tipo:
| Tipo: | "profesional" |
|------|--------|

| "profesional" | "Ana López" | "555654321" |
| "profesional" | "Carlos Gómez" | "555987654" |
|------|--------|---------|



## Caso de uso Extremo 4: Filtrar contactos por parte del teléfono:
| Teléfono: | "56" |
|------|--------|

| "personal" | "Carlos Pérez" | "555123456" |
| "profesional" | "Ana López" | "555654321" |
|------|--------|---------|



## Caso de uso extremo 5: Filtrar contactos por parte del nombre:

| Nombre: | "Car" |
|------|--------|


| "personal" | "Carlos Pérez" | "555123456" |
| "profesional" | "Carlos Gómez" | "555987654" |
|------|--------|---------|



## Caso de uso extremo #6: Filtrar contactos cuando son del mismo tipo:
| Tipo: | "Profesional" |
|------|--------|

 |"profesional" | "Carlos Gómez" | "555987654" |
 |"profesional" | "Mateo Acevedo" | "34566172" |
 |"profesional" | "Robert Jesus" | "889006755" |


 ## Caso de uso Error #7: Filtrar por criterio inexistente:
| Edad: | 29 |
|------|--------|

| Error! Criterio inexistente! |


 ## Caso de uso Error #8: Filtrar nombre con caracter inválido:
| Edad: | C@rlos|
|------|--------|

| Error! Nombre con caracteres incorrectos |



 ## Caso de uso Error #9: Filtrar teléfono con digitos inválidos:
| Teléfono: | "abc 123 cde"|
|------|--------|

| Error! Teléfono con dígitos incorrectos |




# 4. Exportar e importar los contactos en formato vcards (.vcf): 
El sistema debe permitir al
usuario exportar los contactos a un archivo .vcf e importarlos al sistema desde un
archivo .vcf.


## Caso de prueba 1: Caso normal-Exportar contacto:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |


Se ejecuta la función exportar_contactos

Resultado:
| Archivo generado .vcf|
|------|
| BEGIN:VCARD
FN:samuel
TEL:300222398
CATEGORIES:personal
END:VCARD|

## Caso de prueba 2: Caso normal-Importar contacto:
| Contenido del archivo|
|------|
| BEGIN:VCARD
FN:samuel
TEL:300222398
CATEGORIES:personal
END:VCARD|


Se ejecuta la función importar_contactos

Contactos del usuario:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |





## Caso de prueba 3: Caso normal-exportar multiples contactos:

Contactos:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |
| "profesional" | "ana" | "3104567890" |

Se ejecuta la función exportar_contactos

Resultado:
| Archivo generado .vcf|
|------|
| BEGIN:VCARD
FN:samuel
TEL:300222398
CATEGORIES:personal
END:VCARD|
| BEGIN:VCARD
FN:ana
TEL:3104567890
CATEGORIES:profesional
END:VCARD|



## Caso de prueba 4: Caso Extremo-exporta contacto nombre largo:
| Tipo     | Nombre (200 caracteres) | Teléfono   |  
|----------|-------------------------|------------|  
| personal | aaaaaaaaaa...(200 "a")  | 300222398  |  

Se ejecuta la función exportar_contactos

| Archivo generado .vcf |  
|----------------------|  
| BEGIN:VCARD  
FN:aaaaaaaaaaaaaaaaaaaaaaaa... (200 caracteres "a")  
TEL:300222398  
CATEGORIES:personal  
END:VCARD |  


## Caso de prueba 5: Caso Extremo-exporta contacto nombre largo:

Archivo de Entrada (`contactos_vacio.vcf`):  
*(Archivo vacío, sin contenido)*  

Se ejecuta la función importar_contactos intentando importar contactos desde un archivo vacío.  

Resultado Esperado:  

| Contactos Importados |  
|----------------------|  
| Ninguno (lista vacía) | 


## Caso de prueba 6: Caso Extremo-Exportar e importar contacto con caracteres especiales:

Contacto:

| Tipo     | Nombre             | Teléfono         |  
|----------|--------------------|-----------------|  
| personal | José López 🎉✨     | +57-300-555-6666 |  


1. Se ejecuta exportar_contactos
2. Se importa el archivo con importar_contacto

| Archivo generado .vcf |  
|----------------------|  
| BEGIN:VCARD  
FN:José López 🎉✨  
TEL:+57-300-555-6666  
CATEGORIES:personal  
END:VCARD |  



## Caso de prueba 7: Caso Error-Exportar contactos cuando no hay contactos registrados  :

contactos :
| Tipo | Nombre | Teléfono |  
|------|--------|---------|  
|  |    |    |   


Se ejecuta `exportar_contactos cuando no hay contactos registrados.

| Error Lanzado |  
|--------------|  
| Error: No hay contactos para exportar. |  

## Caso de prueba 8: Caso Error-importar desde un archivo inexistente  :

| Nombre del Archivo | Estado |  
|--------------------|--------|  
| archivo_inexistente.vcf | *(No existe)* |  

Se ejecuta importar_contactos

Resultado:
| Error Lanzado |  
|--------------|  
| Error: El archivo  no existe. Verifique la ruta y el nombre del archivo | 

## Caso de prueba 9: Caso Error-importar archivo con formato invalido  :
| Contenido del Archivo |  
|----------------------|  
| CONTACTO: samuel, 300222398 |  

Se ejecuta importar_contactos  

### Resultado :  

| Error Lanzado |  
|--------------|  
| Error : El archivo no tiene un formato VCF válido. Verifique el contenido y la estructura |


# 5. Crear un usuario:
El sistema debe permitir al usuario darse de alta.

## Caso de prueba 1: Caso Normal-Registrar usuario:
Usuario:

| Nombre de Usuario | Contraseña |  
|------------------|------------|  
| "juan" | "password123" |    


| Validación | Resultado Esperado |  
|------------|--------------------|  
|Cantidad de usuarios en lista | 1 usuario en lista |  

## Caso de prueba 2: Caso Normal-Registrar multiples usuarios:
Usuarios:

| Nombre de Usuario | Contraseña |  
|------------------|------------|  
| "juan" | "password123" |  
| "maria" | "password321" | 

| Validación | Resultado Esperado |  
|------------|--------------------|  
|Cantidad de usuarios en lista | 2 usuario en lista | 


## Caso de prueba 3: Caso Normal-Registrar usuarios similares:

| Nombre de Usuario | Contraseña |  
|------------------|------------|  
| "juan1" | "password123" |  
| "juan" | "password12" |

| Validación | Resultado Esperado |  
|------------|--------------------|  
|Cantidad de usuarios en lista | 2 usuario en lista | 

## Caso de prueba 4: Caso Extremo-Registrar usuario nombre y contraseña largos:
Usuario:

| Nombre de Usuario | Contraseña |  
|------------------|------------|  
| "juan" | "password123" |  
| "juan" | "otraClave456" |

| Validación | Resultado Esperado |  
|------------|--------------------|  
|Cantidad de usuarios en lista | 1 usuario en lista | 

## Caso de prueba 5: Caso Extremo-Registrar usuario con caracteres especiales:
Usuario:

| Nombre de Usuario   | Contraseña    |  
|--------------------|--------------|  
| "J@hn_Doe 123"    | "P@ssw0rd!"  |  

| Validación | Resultado Esperado |  
|------------|--------------------|  
|Cantidad de usuarios en lista | 1 usuario en lista | 


## Caso de prueba 6: Caso Extremo-Registrar usuario con espacios en los campos:
| Nombre de Usuario            | Contraseña                   |  
|-----------------------------|-----------------------------|  
| "   usuario con espacios   "  | "   contraseña con espacios   "  | 

Resultado:

| Nombre de Usuario            | Contraseña                   |  
|-----------------------------|-----------------------------|  
| "usuario con espacios"  | "contraseña con espacios"  | 


## Caso de prueba 7: Caso Error-Registrar usuario nulo:

 Datos de entrada  :

| Usuario |  
|---------|  
| `None`  |  


| Error |  
|-------|  
| Error: No se puede registrar un usuario nulo. Verifique los datos de entrada |  

## Caso de prueba 8: Caso Error-Registrar usuario ya registrado:

| Nombre            | Contraseña        |  
|------------------|------------------|  
| usuarioRepetido | contraseña123     |  
| usuarioRepetido | otracontraseña   |  

Resultado :

| Error |  
|-------|  
| Error: El usuario ya está registrado. Elija un nombre diferente |  


## Caso de prueba 9: Caso Error-Intentar registrar un usuario de tipo invalido:

| Tipo de dato proporcionado | Valor |  
|--------------------------|--------------------------------------------|  
| `str`                   | `"Este es un string, no un objeto Usuario"` |  

Resultado:

| Error |  
|-------|  
| Error: Debes proporcionar un objeto de tipo Usuario |


# 6. Iniciar sesión:
El sistema debe permitir al usuario iniciar sesión para ver la lista de sus
contactos.


## Caso de Prueba normal #1: credenciales correctas:
| Nombre | Contraseña |
|------|----------|
| "juan" | "12345" | Ingreso exitoso |


## Caso de Prueba normal #2: iniciar sesión luego de registrarse:
| Nombre | Contraseña |
|------|----------|
| "juan" | "12345" | Registro exitoso |

| Sesión iniciada|


## Caso de Prueba normal #3: iniciar sesión después de cerrar sesión:

Sesión cerrada!

| Nombre | Contraseña |
|------|----------|
| "juan" | "12345" | Ingreso exitoso |



## Caso de Prueba extrema #4: Credenciales extremadamente largas:
| Nombre | Contraseña |
|------|----------|
| "juan garzón garzón villa sanchez" | "123456gsuyh2tn_@" |



## Caso de Prueba extrema #5: Credenciales en mayusculas o minúsuclas:
| Nombre | Contraseña |
|------|----------|
| "Juan" | "ClaveSegura123" |

| Nombre | Contraseña |
|------|----------|
| "juan" | "clavesegura123" |



## Caso de Prueba extrema #6: iniciar sesión en diferentes dispositivos:

### Dispositivo 1:
| "juan" | "12345" |


### Dispositivo 2:
| "juan" | "12345" |


## Caso de Prueba error #7: usuario inexistente:
| Nombre | Contraseña |
|------|----------|
| "usuario inexistente" | "clave123" | !Error,  Usuario inexistente ! |


## Caso de Prueba error #8: contraseña vacía |
| Nombre | Contraseña |
|------|----------|
| "juan" | " " | !Error,  Contraseña vacía |


## Caso de Prueba error #9: nombre vacío |
| Nombre | Contraseña |
|------|----------|
| "" | " 12345 " | !Error,  nombre vacío |


















