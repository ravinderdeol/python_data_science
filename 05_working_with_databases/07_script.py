# import the yfinance library to fetch financial data
import yfinance as yf

# import the mysql connector module to connect to mysql database
import mysql.connector

# import the errorcode module to handle mysql connector errors
from mysql.connector import errorcode

# create an empty list to store the fetched data
data = []

# define a list of stock tickers we want to fetch data for
tickers = ["TSLA", "META", "ORCL", "AMZN"]

# iterate through the tickers list
for ticker in tickers:
    
    # create a ticker object for the current ticker
    tkr = yf.Ticker(ticker)

    # fetch the historical data for the current ticker for the past 5 days
    hist = tkr.history(period = "5d").reset_index()

    # extract the date and closing price columns and convert them into a list of tuples
    records = hist[["Date", "Close"]].to_records(index = False)

    # convert the records object to a list
    records = list(records)

    # format each tuple in records to include the ticker, date as string, and closing price rounded to 2 decimal places
    records = [(ticker, str(elem[0])[:10], round(elem[1], 2)) for elem in records]

    # append the records to the data list
    data = data + records

# try to establish a connection to the mysql database
try:
    
    # establish a connection to the mysql database using the given credentials and database name
    cnx = mysql.connector.connect(user = "{root_user}", password = "{your_password}", host = "{local_host}", database = "{your_database}")

    # create a cursor object to execute sql queries
    cursor = cnx.cursor()

    # define an sql query to insert stock data into the stocks table
    query_add_stocks = ("""INSERT INTO stocks (ticker, date, price) VALUES (%s, %s, %s)""")

    # execute the sql query with the data list adding multiple rows at once
    cursor.executemany(query_add_stocks, data)

    # commit the transaction to the database
    cnx.commit()

# handle any exceptions that may occur during the database operations
except mysql.connector.Error as err:
    print("error code:", err.errno)
    print("error message: {}".format(err.msg))

# execute the code in the finally block regardless of whether an exception occurred or not
finally:
    cursor.close()
    cnx.close()

# notes
    # this script obtains stock data from yfinance and stores it a mysql database