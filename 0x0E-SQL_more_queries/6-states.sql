-- creates the database hbtn_0d_usa and the table states
CREATE USER IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	name VARCHAR(256) NOT NULL);
