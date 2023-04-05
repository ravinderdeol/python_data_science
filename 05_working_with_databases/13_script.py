# import the mongoclient class from the pymongo module
from pymongo import MongoClient

# connect to a mongodb atlas cluster using a connection string with a username, password, and database name
client = MongoClient("mongodb+srv://{username}:{password}@{database}.zspqmkn.mongodb.net/?retryWrites=true&w=majority")

# access a specific database called sampledb using the client object
database = client["sampledb"]

# access a specific collection called employees within the sampledb database
employees_collection = database["employees"]

# define a dictionary containing data for a new employee
employee_data = {
    "id": 9001,
    "name": "jeff russell",
    "orders": [2608, 2617, 2620],
}

# insert the employee data into the employees collection and store the result
result = employees_collection.insert_one(employee_data)

# print the id of the newly inserted document
print(result.inserted_id)

# find the first document in the employees collection where the id field equals 9001
employee_find = employees_collection.find_one({"id": 9001})

# print the document found by the query
print(employee_find)

# notes
    # document orientated databases store each record as a separate document
    # each document in a document orientated database can have its own structure
    # document orientated databases are the most popular of nosql databases
    # mongodb is one of the most popular document orientated databases
    # mongodb is designed to manage collections of json like documents
    # you can use mongodb atlas which requires no installation
    # mongodb groups documents into collections