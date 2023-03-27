-- open mysql from the command line at the root directory and enter the password
mysql -root -p

-- select the sql database created
USE sampledb;

-- create a database for stock quotes
CREATE TABLE stocks (
    symbol VARCHAR(5) NOT NULL,
    name VARCHAR(30) NOT NULL,
    price DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (symbol)
);

-- show the tables in the database
SHOW TABLES;

-- notes
    -- use analytical sql to analyze data in a datbase instread of storing, retrieving, and updating it