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

# print the resulting dataframe
print(employees)

# create a new series of employee data without salary data
new_employees = pd.Series({"name": "dave jones", "job": "marketing"}, name = 9004)

# add the new employee data to the employees dataframe
employees = employees.append(new_employees)

# print the resulting dataframe after adding a new employee
print(employees)

# print the resulting dataframe if the salary column is not null
print(employees[employees["salary"].notnull()])

# notes
    # creating a dataframe from a list of lists
    # changing the default column data types is crucial if you plan to join other dataframes
    # pandas allow you to join dataframes together in the same way you would join tables in a relational database
    # dataframes support database style join operations though the merge and join methods
    # the append method has been deprecated in favor of the concat method