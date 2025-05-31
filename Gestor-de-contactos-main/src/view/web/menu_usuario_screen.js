document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('btnAgregar').addEventListener('click', () => {
        window.location.href = "agregar_contacto_screen.html";
    });
    document.getElementById('btnEditar').addEventListener('click', () => {
        window.location.href = "editar_contacto_screen.html";
    });
    document.getElementById('btnVer').addEventListener('click', () => {
        window.location.href = "ver_contactos_screen.html";
    });
    document.getElementById('btnImportar').addEventListener('click', () => {
        window.location.href = "importar_contacto_screen.html";
    });
    document.getElementById('btnExportar').addEventListener('click', () => {
        window.location.href = "exportar_contacto_screen.html";
    });
    document.getElementById('btnSalir').addEventListener('click', () => {
        alert("Sesión cerrada");
        localStorage.removeItem('usuarioActual');  // borramos usuario actual de localStorage
        window.location.href = "iniciar_sesion_screen.html";
    });
});
