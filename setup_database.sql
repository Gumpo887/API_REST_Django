-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS api_rest_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Usar la base de datos
USE api_rest_db;

-- Asegurarse de que el usuario tiene permisos
-- Si usa root sin contraseña (por defecto en XAMPP/WAMP)
-- Los permisos ya están asignados

-- O si desea crear un usuario específico:
-- CREATE USER 'api_user'@'localhost' IDENTIFIED BY 'password';
-- GRANT ALL PRIVILEGES ON api_rest_db.* TO 'api_user'@'localhost';
-- FLUSH PRIVILEGES;
