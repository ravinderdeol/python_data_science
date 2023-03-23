# import the mysql connector module
import mysql.connector

# wrap the code in a try block to catch any possible exceptions
try:
    
    # create a connection to a mysql server with the given credentials
    cnx = mysql.connector.connect(user = "{root_user}", password = "{your_password}", host = "{local_host}", database = "{your_database}")

    # create a cursor object to interact with the database
    cursor = cnx.cursor()

    # create a list of employees with their details as tuples
    employees = [
        (9001, "jeff russell", "sales"),
        (9002, "jane boorman", "sales"),
        (9003, "tom heints", "sales"),
    ]

    # define a query to add employees to the database
    query_add_employee = ("""INSERT INTO employees (id, name, role) VALUES (%s, %s, %s)""")

    # iterate through the list of employees and execute the query for each one
    for employee in employees:
        cursor.execute(query_add_employee, employee)

    # create a list of salaries with employee ids and their salaries as tuples
    salary = [
        (9001, 3000),
        (9002, 2800),
        (9003, 2500)
    ]

    # define a query to add salaries to the database
    query_add_salary = ("""INSERT INTO salary (id, salary) VALUES (%s, %s)""")

    # iterate through the list of salaries and execute the query for each one
    for s in salary:
        cursor.execute(query_add_salary, s)

    # create a list of orders with invoice numbers, employee ids, and total amounts as tuples
    orders = [
        (2608, 9001, 35),
        (2617, 9001, 35),
        (2620, 9001, 139),
        (2621, 9002, 95),
        (2626, 9002, 218)
    ]

    # define a query to add orders to the database
    query_add_order = ("""INSERT INTO orders (invoice, id, total) VALUES (%s, %s, %s)""")

    # iterate through the list of orders and execute the query for each one
    for order in orders:
        cursor.execute(query_add_order, order)

    # commit the changes to the database
    cnx.commit()

# catch any exceptions and print out the error message
except mysql.connector.Error as err:
    print("error code:", err.errno)
    print("error message: {}".format(err.msg))

# close the cursor and connection
finally:
    cursor.close()
    cnx.close()

# notes
    # you can add data to mysql tables in the command line but it is more common to do it via an application