function filtrarContactos() {
    const tipoFiltro = document.getElementById("tipo").value.toLowerCase();
    const nombreFiltro = document.getElementById("nombre").value.toLowerCase();
    const telefonoFiltro = document.getElementById("telefono").value.toLowerCase();

    const usuario = localStorage.getItem("usuarioActual");

    if (!usuario) {
        alert("No hay sesión iniciada.");
        window.location.href = "iniciar_sesion_screen.html";
        return;
    }

    fetch(`http://127.0.0.1:8000/api/v1/contactos?nombre_usuario=${encodeURIComponent(usuario)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("No autorizado o error al obtener contactos");
            }
            return response.json();
        })
        .then(contactos => {
            const tabla = document.getElementById("tablaContactos");
            tabla.innerHTML = ""; // Limpiar tabla

            contactos
                .filter(c => {
                    return (
                        (tipoFiltro === "" || c.tipo.toLowerCase() === tipoFiltro) &&
                        (nombreFiltro === "" || c.nombre.toLowerCase().includes(nombreFiltro)) &&
                        (telefonoFiltro === "" || c.telefono.toLowerCase().includes(telefonoFiltro))
                    );
                })
                .forEach(contacto => {
                    const fila = document.createElement("tr");
                    fila.innerHTML = `
                        <td>${contacto.tipo}</td>
                        <td>${contacto.nombre}</td>
                        <td>${contacto.telefono}</td>
                    `;
                    tabla.appendChild(fila);
                });
        })
        .catch(error => {
            alert("Error: " + error.message);
            console.error(error);
        });
}

// También puedes ejecutar automáticamente la carga sin esperar al botón
document.addEventListener('DOMContentLoaded', filtrarContactos);
