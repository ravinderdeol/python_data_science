# import the yfinance library to fetch financial data
import yfinance as yf

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

# print the final data list
print(data)

# notes
    # this scrip obtains stock data from yfinance