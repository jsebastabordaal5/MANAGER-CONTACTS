/**
 * Script que permite iniciar sesión en el sistema.
 * Captura nombre de usuario y contraseña desde el formulario.
 * Envía una solicitud POST a la API para autenticación.
 * Si es exitoso, guarda el nombre de usuario en localStorage y redirige al menú principal.
 * Si falla, muestra un mensaje de error.
 */


document.addEventListener('DOMContentLoaded', () => {
    const btnLogin = document.getElementById('btnLogin');
    btnLogin.addEventListener('click', manejarLogin);
});

async function manejarLogin() {
    const nombre = document.getElementById('usuario').value.trim();
    const contraseña = document.getElementById('contraseña').value;

    if (!nombre || !contraseña) {
        alert('Por favor, completa todos los campos.');
        return;
    }

    try {
        const response = await fetch('/api/v1/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nombre, contraseña }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert('Error: ' + errorData.detail);
            return;
        }

        const data = await response.json();
        alert(data.mensaje);

        // Guardar el nombre de usuario en localStorage para usar en otras peticiones
        localStorage.setItem('usuarioActual', nombre);

        window.location.href = 'menu_usuario_screen.html';
    } catch (error) {
        alert('Error de conexión con el servidor.');
        console.error(error);
    }
}
