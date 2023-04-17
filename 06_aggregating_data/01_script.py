# imports the pandas library and renames it as 'pd' to be used later in the code.
import pandas as pd

## -- data to aggregate -- ##

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

## -- combining dataframes -- ##

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

## -- grouping and aggregating data -- ##

# group rows of the result dataframe then calculate the sum of the numerical values in other columns for each group creating a new dataframe
df_date_region = df_result.groupby(["Date", "Region"]).sum()

## -- viewing aggregations by multi index -- ##

# filter rows to only include those with an index that matches the tuple
df_date_region = df_date_region[df_date_region.index.isin([("2021-08-04", "East"), ("2021-08-06", "West")])]

## -- slicing a range of aggregated values -- ##

# slice rows with index values between the two tuples
df_date_region = df_date_region[("2021-08-04", "East"):("2021-08-06", "West")]

## -- slicing within aggregation levels -- ##

# use loc to slice based on index values between the two tuples and select all columns
df_date_region = df_date_region.loc[(slice("2021-08-04", "2021-08-06"), slice(None)), :]

## -- adding a grand total -- ##

# calculate the sum of each column in the dataframe and store it in the ps pandas series object
ps = df_date_region.sum(axis = 0)

# rename the pandas series object to 'all' and 'all'
ps.name = ("All", "All")

# append the pandas series object to the original dataframe to create a new dataframe
df_date_region_total = df_date_region.append(ps)

# select and print the rows of the dataframe where the index is 'all' and 'all'
# print(df_date_region_total[df_date_region_total.index.isin([("All", "All")])])

## -- adding subtotals -- ##

# initialize an empty dataframe to store the subtotals
df_totals = pd.DataFrame(columns=df_date_region.columns)

# iterate over each unique date value in the index of the dataframe 'df_date_region'
for date, date_df in df_date_region.groupby(level=0):
    
    # append the current date dataframe to the 'df_totals' dataframe
    df_totals = df_totals.append(date_df)

    # calculate the sum of each column for the current date dataframe and store it in a pandas series object
    ps = date_df.sum(axis=0)

    # set the name of the pandas series object to a tuple with the date value and 'all'
    ps.name = (date, "All")

    # append the pandas series object to the 'df_totals' dataframe as a new row
    df_totals = df_totals.append(ps)

# append the total row to the 'df_totals' dataframe only once
df_totals = df_totals.append(df_date_region_total.loc[("All", "All")])

## -- selecting all rows in a group -- ##

# group the dataframe by the values in the date and region columns
group = df_result.groupby(["Date", "Region"])

# get the group of rows in the dataframe at the specified date and region value
print(group.get_group(("2021-08-05", "East")))

# notes
    # aggregate functions return a single result row based on an entire group of rows
    # aggregate functions form a single aggregated summary row for each group
    # aggregating data can answer specific questions in a summarised way
    # data in this script would often be stored in seperate databases
    # in the merge method the order number column is used to join the dataframes by default
    # to perform aggregate calculations on data it must first be sorted into relevant groups
    # the groupby function splits data into subsets that have matching values for one or more columns
    # multindex dataframes are dataframes that have multiple levels of indexing
    # index.isin is a pandas method returning a boolean array indicating whether the data at each index matches the given value
    # you can pass more than one index value to the isin method to filter for multiple values
    # the order of the retrieved records will match the order of the records in the dataframe not the order specified in the isin method
    # the append method will be replaced with concat in a future version of pandas
    # put each of these ways to work with dataframes in separate scripts to practice with separate files for the data


