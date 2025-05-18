
-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL
);

-- Tabla de contactos
CREATE TABLE IF NOT EXISTS contactos (
    id_contacto SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    tipo TEXT NOT NULL,
    id_usuario INTEGER NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- Insertar usuarios
INSERT INTO usuarios (nombre, contrasena) VALUES ('juan', 'clave123');
INSERT INTO usuarios (nombre, contrasena) VALUES ('maria', 'segura456');
INSERT INTO usuarios (nombre, contrasena) VALUES ('pedroperez', 'caguamas12');

-- Insertar contactos para Juan (id_usuario = 1)
INSERT INTO contactos (nombre, telefono, tipo, id_usuario) VALUES 
('Carlos Pérez', '3024839892', 'personal', 1),
('Ana Torres', '30056734651', 'personal', 1),
('Luis Ramírez', '30287512093', 'profesional', 1),
('Felipe', '30045826571', 'profesional', 1),
('Jose', '30056805881', 'profesional', 1),
('Marulete', '30056805882', 'personal', 1);


-- Insertar contactos para María (id_usuario = 2)
INSERT INTO contactos (nombre, telefono, tipo, id_usuario) VALUES 
('Lucía Gómez', '3058769092', 'profesional', 2),
('Pedro Ruiz', '3038471263', 'personal', 2),
('Cata', '30293812821', 'personal', 2),
('Elena Díaz', '30283709271', 'personal', 2);

-- Insertar contactos para pedroperez(id_usuario = 3)
INSERT INTO contactos (nombre, telefono, tipo, id_usuario) VALUES
('Parcerito', '12345678910', 'personal', 3);
