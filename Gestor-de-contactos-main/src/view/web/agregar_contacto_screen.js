function registrarContacto() {
    const tipo = document.getElementById("tipo").value;
    const nombre = document.getElementById("nombre").value.trim();
    const telefono = document.getElementById("telefono").value.trim();
    const usuario = localStorage.getItem("usuarioActual");

    if (!tipo || !nombre || !telefono) {
        alert("Por favor completa todos los campos.");
        return;
    }

    const formData = new FormData();
    formData.append("tipo", tipo);
    formData.append("nombre", nombre);
    formData.append("telefono", telefono);
    formData.append("nombre_usuario", usuario);

    fetch("http://127.0.0.1:8000/api/v1/contactos/registrar", {
        method: "POST",
        body: formData
    })
    .then(async response => {
        const text = await response.text();
        let data;

        try {
            data = JSON.parse(text);
        } catch {
            data = null;
        }

        if (!response.ok) {
            let errorText;
            if (data) {
                if (Array.isArray(data)) {
                    errorText = data.map(e => `${e.loc?.join(".")}: ${e.msg}`).join("\n");
                } else {
                    errorText = data.detail || JSON.stringify(data);
                }
            } else {
                errorText = text || "Error desconocido";
            }
            throw new Error(errorText);
        }

        return data || text;
    })
    .then(data => {
        alert(data.mensaje || "Contacto agregado correctamente.");
        window.location.href = "menu_usuario_screen.html";
    })
    .catch(error => {
        alert("Error al agregar contacto:\n" + error.message);
        console.error(error);
    });
}
