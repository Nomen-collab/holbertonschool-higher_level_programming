-- 2-create_read_user.sql

-- Créer la base de données 'hbtn_0d_2' si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Créer l'utilisateur 'user_0d_2' si l'utilisateur n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Accorder uniquement le privilège SELECT sur la base 'hbtn_0d_2' à l'utilisateur 'user_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Recharger les privilèges pour appliquer les modifications
FLUSH PRIVILEGES;
