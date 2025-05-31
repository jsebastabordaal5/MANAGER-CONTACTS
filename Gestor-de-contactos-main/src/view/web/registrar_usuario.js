document.addEventListener('DOMContentLoaded', () => {
    const btnRegistrar = document.getElementById('btnRegistrar');

    btnRegistrar.addEventListener('click', async () => {
        const nombre = document.getElementById('usuario').value.trim();
        const contraseña = document.getElementById('contraseña').value;

        if (!nombre || !contraseña) {
            alert('Por favor, completa todos los campos.');
            return;
        }

        try {
            const response = await fetch('/api/v1/registrar', {
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
            window.location.href = 'index.html'; // Redirige a la página principal o login
        } catch (error) {
            alert('Error de conexión con el servidor.');
            console.error(error);
        }
    });
});
