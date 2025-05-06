-- Active: 1746498985192@@127.0.0.1@3306@tarea2
-- Crear usuario
CREATE USER 'cc5002'@'localhost' IDENTIFIED BY 'programacionweb';

-- Conceder privilegios
GRANT ALL ON tarea2.* TO cc5002@localhost;

-- Eliminar el usuario si es necesario
DROP USER IF EXISTS 'cc5002'@'localhost';