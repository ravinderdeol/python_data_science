# import the mysql connector module to connect to mysql database
import mysql.connector

try:
    # connect to my sql database using the root user, password, local host, and database name
    cnx = mysql.connector.connect(user = "{root_user}", password = "{your_password}", host = "{local_host}", database = "{your_database}")

    # create a cursor object to interact with the database
    cursor = cnx.cursor()

    # define the my sql query to select all columns from the employees table where id is greater than a certain value
    query = ("SELECT * FROM employees WHERE id > %s")

    # define the value of the id parameter used in the my sql query
    id = 9001

    # execute the my sql query using the cursor and the id parameter
    cursor.execute(query, (id,))

    # iterate through the cursor results and print the id, name, and role values for each row
    for (id, name, role) in cursor:
        print("{}, {}, {}".format(id, name, role))

# catch any exceptions and print out the error message
except mysql.connector.Error as err:
    print("error code:", err.errno)
    print("error message: {}".format(err.msg))

# close the cursor and connection
finally:
    cursor.close()
    cnx.close()

# notes
    # unlike insertion operations the selecting row does not require you to perform multiple cursor execute operations in a loop
    # the asterisk in the query is used to select all columns
    # the where clause specifies the condition for selecting rows
    # the execute method requires that binding variables be passed within a tuple or dictionary
    # a cursor object is used to execute queries and fetch results from a database