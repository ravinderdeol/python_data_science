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

# print the data frame
print(df)

# reset the index of the data frame moving moves the multi index back into columns
df = df.reset_index()

# group the sales data by employee and convert the invoice and total data for each employee into a dictionary
# create a new data frame using the groupby object
# reset the index which moves the multi index back into columns
# rename the first column to sales
# convert the data frame to a json formatted string with records orientation
json_doc = (df.groupby(["employee"], as_index = True)
            .apply(lambda x: x[["invoice", "total"]].to_dict("records"))
            .reset_index()
            .rename(columns = {0: "sales"})
            .to_json(orient = "records"))

# load the json formatted string into a Python object then re-serialize it into a formatted json string
# print the json formatted string
print(json.dumps(json.loads(json_doc), indent = 2))

# notes
    # script that converts json data into a data frame
    # after converting it to a data frame it is converted back to json
    # pandas comes with various reader methods each of which is designed to load data in a certain format