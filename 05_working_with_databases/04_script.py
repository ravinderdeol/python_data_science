# import the mysql connector module to connect to mysql database
import mysql.connector

try:
    # connect to my sql database using the root user, password, local host, and database name
    cnx = mysql.connector.connect(user = "{root_user}", password = "{your_password}", host = "{local_host}", database = "{your_database}")

    # create a cursor object to interact with the database
    cursor = cnx.cursor()
    
    # sql query that retrieves the id, name, role, and salary of employees from two tables, employees and salary, based on a specified condition of having an employee id greater than a certain value
    query = ("""SELECT e.id, e.name, e.role, s.salary FROM employees e JOIN salary S ON e.id = s.id WHERE e.id > %s""")

    # define the value of the id parameter used in the my sql query
    id = 9001

    # execute the my sql query using the cursor and the id parameter
    cursor.execute(query, (id,))

    # loop that goes through the result set returned by the sql query and extracts the id, name, role, and salary values for each row
    for (id, name, role, salary) in cursor:
        print("{}, {}, {}, {}".format(id, name, role, salary))

# catch any exceptions and print out the error message
except mysql.connector.Error as err:
    print("error code:", err.errno)
    print("error message: {}".format(err.msg))

# close the cursor and connection
finally:
    cursor.close()
    cnx.close()

# notes
    # select statements can be also be written to join rows from different tables
    # typically tables are joined through the foreign key relationship