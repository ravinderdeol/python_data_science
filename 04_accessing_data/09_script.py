import json
import pandas as pd

# define a list of dictionaries that represents some sales data with employee names
data = [
    {
        "employee": "jeff russell",
        "sales": [
            {"invoice": 2608, "total": 35},
            {"invoice": 2617, "total": 35},
            {"invoice": 2620, "total": 139}
        ]
    },
    {
        "employee": "jane boorman",
        "sales": [
            {"invoice": 2621, "total": 95},
            {"invoice": 2626, "total": 218}
        ]
    }
]

# use the json normalize function to create a pandas data frame from the data
# the first argument is the data
# the second argument is the key to normalize
# the third argument is the column to use for grouping
# set the index of the data frame to be a multi index consisting of the employee and invoice columns
df = pd.json_normalize(data, "sales", "employee").set_index(["employee", "invoice"])

print(df)

# notes
    # script that converts json data into a data frame
    # pandas comes with various reader methods each of which is designed to load data in a certain format