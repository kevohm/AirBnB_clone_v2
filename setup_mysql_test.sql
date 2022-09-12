-- test create user and database
-- grant test user all privilages to test db created
CREATE USER IF NOT EXISTS "hbnb_test"@"localhost" IDENTIFIED BY "hbnb_test_pwd";
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;
GRANT SELECT on performance_schema.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;
