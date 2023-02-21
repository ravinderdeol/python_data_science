# import the json and pandas libraries
import json
import pandas as pd

# create a list of dictionaries where each dictionary represents an employees data
data = [
    {"empno": 9001, "salary": 3000},
    {"empno": 9002, "salary": 2800},
    {"empno": 9003, "salary": 2500},
]

# convert the list of dictionaries to a json string
json_data = json.dumps(data)

# use the pandas read json method to read the json string into a dataframe
salary = pd.read_json(json_data)

# set the index of the dataframe to the empno column
salary = salary.set_index("empno")

# print the resulting dataframe
print(salary)

# notes
    # converting a json document to a pandas object