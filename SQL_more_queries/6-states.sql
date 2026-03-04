-- script that creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create table states
CREATE TABLE IF NOT EXISTS states FROM htbn_0d_usa(
	id INT PRIMARY KEY,
	name VARCHAR(256)
);
