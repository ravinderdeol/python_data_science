# import the Pandas library and alias it as pd
import pandas as pd

# define a list of driver names
driver_name = ["lewis hamilton", "charles leclerc", "max verstappen"]

# define a list of driver numbers
driver_number = [44, 16, 33]

# define a list of driver teams
driver_team = ["mercedes", "ferrari", "red bull"]

# create a new dataframe from the three lists
driver_data = pd.DataFrame({"name": driver_name, "number": driver_number, "team": driver_team})

# print the new dataframe to the console
print(driver_data)

# notes
    # pandas is the standard for data orientated applications
    # a pandas series is a one-dimensional labeled array
    # by default pandas uses the object data type to store strings
    # you can create a series with user defined indices instead of the default indices
    # use the loc method to access the series using the user defined indices