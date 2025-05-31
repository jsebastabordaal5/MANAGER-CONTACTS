document.getElementById('btnImportar').addEventListener('click', () => {
    const rutaArchivo = document.getElementById('rutaArchivo').value.trim();
    const nombreUsuario = localStorage.getItem('usuarioActual');

    if (!nombreUsuario) {
        alert('No hay sesión iniciada.');
        window.location.href = 'iniciar_sesion_screen.html';
        return;
    }

    if (!rutaArchivo) {
        alert('Por favor ingresa la ruta del archivo.');
        return;
    }

    fetch('http://127.0.0.1:8000/api/v1/contactos/importar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nombre_usuario: nombreUsuario,
            ruta_archivo: rutaArchivo
        })
    })
    .then(res => {
        if (!res.ok) {
            return res.json().then(data => { throw new Error(data.detail || 'Error al importar'); });
        }
        return res.json();
    })
    .then(data => {
        alert(data.mensaje);
    })
    .catch(error => {
        alert('Error: ' + error.message);
    });
});
