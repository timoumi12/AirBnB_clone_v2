-- -- Create Database and grant permission to User

CREATE DATABASE IF NOT EXIST hbnb_dev_db;

CREATE USER IF NOT EXIST hbnb_dev@localhost;
SET PASSWORD FOR hbnb_dev@localhost = 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;

GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;

FLUSH PRIVILEGES;
