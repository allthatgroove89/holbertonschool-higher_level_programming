-- This script creates a database named hbtn_0c_0 in the MySQL server
IF NOT EXISTS (SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'hbtn_0c_0')
BEGIN
	CREATE DATABASE hbtn_0c_0;
END;
