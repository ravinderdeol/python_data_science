# imports the pandas library and renames it as 'pd' to be used later in the code.
import pandas as pd

# defines a list of tuples containing order information
orders = [
 (9423517, "2021-08-04", 9001),
 (4626232, "2021-08-04", 9003),
 (9423534, "2021-08-04", 9001),
 (9423679, "2021-08-05", 9002),
 (4626377, "2021-08-05", 9003),
 (4626412, "2021-08-05", 9004),
 (9423783, "2021-08-06", 9002),
 (4626490, "2021-08-06", 9004)
]

# defines a list of tuples containing details for each order
details = [
 (9423517, "Jeans", "Rip Curl", 87.0, 1),
 (9423517, "Jacket", "The North Face", 112.0, 1),
 (4626232, "Socks", "Vans", 15.0, 1),
 (4626232, "Jeans", "Quiksilver", 82.0, 1),
 (9423534, "Socks", "DC", 10.0, 2),
 (9423534, "Socks", "Quiksilver", 12.0, 2),
 (9423679, "T-shirt", "Patagonia", 35.0, 1),
 (4626377, "Hoody", "Animal", 44.0, 1),
 (4626377, "Cargo Shorts", "Animal", 38.0, 1),
 (4626412, "Shirt", "Volcom", 78.0, 1),
 (9423783, "Boxer Shorts", "Superdry", 30.0, 2),
 (9423783, "Shorts", "Globe", 26.0, 1),
 (4626490, "Cargo Shorts", "Billabong", 54.0, 1),
 (4626490, "Sweater", "Dickies", 56.0, 1)
]

# defines a list of tuples containing employee information
emps = [
 (9001, "Jeff Russell", "LA"),
 (9002, "Nick Boorman", "San Francisco"),
 (9003, "Tom Heints", "NYC"),
 (9004, "Maya Silver", "Philadelphia")
]

# defines a list of tuples containing location information
locations = [
 ("LA", "West"),
 ("San Francisco", "West"),
 ("NYC", "East"),
 ("Philadelphia", "East")
]

# creates a pandas dataframe from the 'orders' list of tuples, and sets the column names
df_orders = pd.DataFrame(orders, columns = ["OrderNo", "Date", "EmpNo"])

# creates a pandas dataframe from the 'details' list of tuples, and sets the column names
df_details = pd.DataFrame(details, columns = ["OrderNo", "Item", "Brand", "Price", "Quantity"])

# creates a pandas dataframe from the 'emps' list of tuples, and sets the column names
df_emps = pd.DataFrame(emps, columns = ["EmpNo", "EmpName", "Location"])

# creates a pandas dataframe from the 'locations' list of tuples, and sets the column names
df_locations = pd.DataFrame(locations, columns = ["Location", "Region"])

# creates a new dataframe combining orders and details based on the common order number column
df_sales = df_orders.merge(df_details)

# calculates a new column called total by multiplying the price and quantity columns
df_sales["Total"] = df_sales["Price"] * df_sales["Quantity"]

# selects the three columns from the sales dataframe to assign them to a new dataframe
df_sales = df_sales[["Date", "EmpNo", "Total"]]

# combines the sales and employees dataframe based on the common employee number column
df_sales_emps = df_sales.merge(df_emps)

# combines the sales employees and locations dataframe on the common location column creating a new dataframe
df_result = df_sales_emps.merge(df_locations)

# selects three columns from the result dataframe
df_result = df_result[["Date", "Region", "Total"]]

print(df_result)

# notes
    # aggregate functions return a single result row based on an entire group of rows
    # aggregate functions form a single aggregated summary row for each group
    # aggregating data can answer specific questions in a summarised way
    # data in this script would often be stored in seperate databases
    # in the merge method the order number column is used to join the dataframes by default