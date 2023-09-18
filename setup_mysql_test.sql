-- a script that prepares a MySQL server for the project
CREATE IF NOT EXIST DATABASE hbnb_dev_db;

CREATE IF NOT EXIST USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'

CREATE UF NOT EXIST DATABASE hbnb_test_db;

CREATE IF NOT EXIST USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost'

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
