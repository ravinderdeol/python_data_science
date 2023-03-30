# import the warnings module to suppress warning messages
import warnings

# import pandas module and alias it as pd
import pandas as pd

# import mysql connector module
import mysql.connector

# import errorcode module from mysql connector
from mysql.connector import errorcode

# filter and suppress user warning messages from pandas module
warnings.filterwarnings("ignore", category = UserWarning, module = "pandas")

try:

    # connect to mysql database using mysql connector module
    cnx = mysql.connector.connect(user = "root", password = "password", host = "host", database = "database")
    
    # sql query to retrieve data from mysql database
    query = ("""
        SELECT s.* FROM stocks AS s
        LEFT JOIN (
            SELECT DISTINCT(ticker) FROM
                (SELECT
                    price/LAG(price) OVER(PARTITION BY ticker ORDER BY date) AS dif, ticker 
                    FROM stocks) AS b
                WHERE dif < 0.99) AS a
            ON a.ticker = s.ticker
            WHERE a.ticker IS NULL;""")
    
    # read the result of sql query into a pandas dataframe
    df_stocks = pd.read_sql(query, con = cnx)

    # set the multi index for the dataframe
    df_stocks = df_stocks.set_index(["ticker", "date"])

    # print the dataframe to the console
    print(df_stocks)

except mysql.connector.Error as err:

    # print the error code if an error occurs
    print("error code:", err.errno)

    # print the error message if an error occurs
    print("error message: {}".format(err.msg))

finally:

    # close the database connection
    cnx.close()

# notes
    # this script fetches the results into a pandas data frame
    # the mysql query is explained in the previous script
    # a multi index is a way to create a hierarchical index structure consisting of multiple levels
    # multi indexing allows you group and analyze data by multiple dimensions