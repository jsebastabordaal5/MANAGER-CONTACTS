/**
 * Exporta todos los contactos de un usuario autenticado a un archivo .vcf.
 * El usuario debe ingresar el nombre del archivo.
 * Se hace una solicitud POST a la API para realizar la exportación.
 * Si no hay sesión iniciada o falta el nombre del archivo, se notifica al usuario.
 */


document.querySelector("button").addEventListener("click", () => {
    const nombreArchivo = document.getElementById("usuario").value.trim();
    const usuario = localStorage.getItem("usuarioActual");

    if (!usuario) {
        alert("No hay sesión iniciada.");
        window.location.href = "iniciar_sesion_screen.html";
        return;
    }

    if (nombreArchivo === "") {
        alert("Por favor ingresa el nombre del archivo.");
        return;
    }

    fetch("http://127.0.0.1:8000/api/v1/contactos/exportar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nombre_usuario: usuario,
            ruta_archivo: nombreArchivo
        })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => { throw new Error(data.detail); });
        }
        return response.json();
    })
    .then(data => {
        alert(data.mensaje);
    })
    .catch(error => {
        alert("Error al exportar contactos: " + error.message);
        console.error(error);
    });
});
