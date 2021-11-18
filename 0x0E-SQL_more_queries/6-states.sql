-- creates the database hbtn_0d_usa and the table states
CREATE USER IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_02.states(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL);
