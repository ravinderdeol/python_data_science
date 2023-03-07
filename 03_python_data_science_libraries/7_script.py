# import the pandas library and assign it to the variable pd
import pandas as pd

# create a list of lists where each inner list represents an employees data
employees_data = [
    ["9001", "jeff russell", "sales"],
    ["9002", "jane boorman", "engineering"],
    ["9003", "tom heints", "sales"],
]

# create a list of lists where each inner list represents an employees salary data
salaries_data = [
    [9001, 3000],
    [9002, 2800],
    [9003, 2500],
]

# create a list of lists where each inner list represents an employees sales data
orders_data = [
    [2608, 9001, 35],
    [2617, 9001, 35],
    [2620, 9001, 139],
    [2621, 9002, 95],
    [2626, 9002, 218],
    [2604, 9003, 24],
]

# create a dataframe from the employees_data list of lists and specify column names for the dataframe
employees = pd.DataFrame(employees_data, columns = ["number", "name", "job"])

# define a dictionary that specifies the data types for each column in the employees dataframe
column_types = {"number": int, "name": str, "job": str}

# use the astype method to cast the columns in the employees dataframe to the specified data types
employees = employees.astype(column_types)

# use the set index method to set the index of the employees dataframe to the number column
employees = employees.set_index("number")

# create a new dataframe from the salaries data list of lists and specify column names for the dataframe
salaries = pd.DataFrame(salaries_data, columns = ["number", "salary"])

# use the set index method to set the index of the salaries dataframe to the number column
salaries = salaries.set_index("number")

# use the join method to join the salaries dataframe with the employees dataframe based on the number column
employees = employees.join(salaries)

# create a new dataframe from the orders data list of lists and specify column names for the dataframe
orders = pd.DataFrame(orders_data, columns = ["product", "number", "sold"])

# use the merge method to join the orders dataframe with the employees dataframe based on the number column
employees_orders = employees.merge(orders, how = "inner", left_on = "number", right_on = "number").set_index("product")

# group the orders dataframe by the number column and calculate the mean of the sold column
print(orders.groupby(["number"])["sold"].mean())

# group the orders dataframe by the number column and calculate the sum of the sold column
print(orders.groupby(["number"])["sold"].sum())

# notes
    # the groupby function lets you aggregate data over multiple rows