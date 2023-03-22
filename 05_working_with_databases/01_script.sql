-- create an sql database
CREATE DATABASE sampledb;

-- select the sql database created
USE sampledb;

-- create the employees table in the database
-- id field is the integer and can not be null
-- name field is a string of fifty characters
-- role field is a string of thirty characters
-- id field is the primary key meaning it is not supposed to have duplicates across the table
CREATE TABLE employees (
    id INT NOT NULL,
    name VARCHAR(50),
    role VARCHAR(30),
    PRIMARY KEY (id)
);

-- create the salary table in the database
CREATE TABLE salary (
    id INT NOT NULL,
    salary INT,
    PRIMARY KEY (id),
);

-- add a foreign key restraint to the id column of the salary table referencing the id column of the employees table
-- create a relationship between the salary and employees table
-- establishes that an employee number in the salary table must match an employee number in the employees table
-- guarantees that a record cannot be added in the salary table if the table does not have a corresponding record in the employees table
ALTER TABLE salary ADD FOREIGN KEY (id) REFERENCES employees(id);

-- create the orders table in the database
-- add a foreign key constraint directly to the command
CREATE TABLE orders (
    invoice INT NOT NULL,
    id INT NOT NULL,
    total INT,
    PRIMARY KEY (invoice),
    FOREIGN KEY (id) REFERENCES employees (id)
);

-- notes
    -- relational databases have a rigid structure implemented in the form of a schema for the data being stored
    -- non relational databases do not impose restrictions on the data structure hence allowing for more flexibility and scalability
    -- common examples of relational databases are mysql, postgresql, and sqlite
    -- sql statements often have three components, e.g. operation to be performed, target for the operation, condition that narrows the scope of the operation
    -- all sql statements must have an operation and target but the condition is optional
    -- the fields that link different tables are called keys
    -- primary keys uniquely identify a record in a table
    -- foreign keys are fields in another table that correspond to the primary key of a record in the first table
    -- 'mysql -uroot -p' is the command to connect to mysql from the command line
    -- '-uroot' specifies the user name, i.e. the root user in this case
    -- '-p' specifies that the password will be prompted for