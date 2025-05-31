/**
 * Permite al usuario seleccionar un contacto desde un menú desplegable,
 * visualizar su información y editar sus datos (nombre, tipo, teléfono).
 * La edición se realiza mediante una solicitud POST a la API.
 * Si hay errores de validación, se muestran mensajes en pantalla.
 * Al finalizar, se recarga la lista de contactos y se limpia el formulario.
 */


const contactoSelect = document.getElementById('contactoSelect');
const form = document.getElementById('editarContactoForm');
const tipoInput = document.getElementById('tipo');
const nombreInput = document.getElementById('nombre');
const telefonoInput = document.getElementById('telefono');
const nombreOriginalInput = document.getElementById('nombreOriginal');
const mensaje = document.getElementById('mensaje');

async function cargarContactos() {
    try {
        const usuario = localStorage.getItem("usuarioActual");
        const response = await fetch(`/api/v1/contactos?nombre_usuario=${usuario}`);
        if (!response.ok) throw new Error('Error al cargar contactos');

        const contactos = await response.json();

        contactoSelect.innerHTML = '<option value="" disabled selected>-- Elige un contacto --</option>';

        contactos.forEach(c => {
            const option = document.createElement('option');
            option.value = c.nombre;
            option.textContent = `${c.tipo} - ${c.nombre} (${c.telefono})`;
            contactoSelect.appendChild(option);
        });
    } catch (error) {
        mensaje.textContent = error.message;
    }
}

contactoSelect.addEventListener('change', () => {
    mensaje.textContent = '';
    const seleccionado = contactoSelect.value;
    if (!seleccionado) {
        form.style.display = 'none';
        return;
    }

    const usuario = localStorage.getItem("usuarioActual");
    fetch(`/api/v1/contactos?nombre_usuario=${usuario}`)
        .then(res => res.json())
        .then(contactos => {
            const contacto = contactos.find(c => c.nombre === seleccionado);
            if (!contacto) {
                mensaje.textContent = 'Contacto no encontrado';
                form.style.display = 'none';
                return;
            }

            nombreOriginalInput.value = contacto.nombre;
            tipoInput.value = contacto.tipo;
            nombreInput.value = contacto.nombre;
            telefonoInput.value = contacto.telefono;

            form.style.display = 'block';
        })
        .catch(() => {
            mensaje.textContent = 'Error al obtener datos del contacto';
            form.style.display = 'none';
        });
});

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    mensaje.textContent = '';

    const usuario = localStorage.getItem("usuarioActual");

    const formData = new FormData();
    formData.append("nombre_original", nombreOriginalInput.value);
    formData.append("tipo", tipoInput.value);
    formData.append("nombre", nombreInput.value.trim());
    formData.append("telefono", telefonoInput.value.trim());
    formData.append("nombre_usuario", usuario);

    try {
        const response = await fetch('/api/v1/contactos/editar', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            const errorData = await response.json();
            if (Array.isArray(errorData)) {
                const errores = errorData.map(e => `${e.loc?.join(".")}: ${e.msg}`).join("\n");
                throw new Error(errores);
            } else {
                throw new Error(errorData.detail || 'Error al editar contacto');
            }
        }

        const result = await response.json();
        mensaje.style.color = 'green';
        mensaje.textContent = result.mensaje;

        await cargarContactos();
        form.style.display = 'none';
        contactoSelect.value = '';
    } catch (error) {
        mensaje.style.color = 'red';
        mensaje.textContent = error.message;
    }
});

window.addEventListener('DOMContentLoaded', cargarContactos);
