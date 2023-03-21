# import the pandas data reader library and rename it
import pandas_datareader.data as pdr

# retrieve the stock data for ferrari from stooq
race_index = pdr.get_data_stooq("race", "2023-01-01", "2023-01-07")

# print the data frame to the console
print(race_index)

# notes
    # script obtains stock data from stooq but it can also obtain data from other sources
    # pandas data reader is designed to interface some of the most popular finance data apis
    # pandas data reader imports data into easy to read data frames
    # review the docs to read about its scope at pandas-datareader.readthedocs.io