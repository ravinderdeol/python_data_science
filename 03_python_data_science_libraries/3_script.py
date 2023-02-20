# import the yfinance library and give it the name yf
import yfinance as yf

# Create a variable called tkr and assign it the ticker object from yfinance for the stock symbol tsla
tkr = yf.Ticker("tsla")

# get the historical price data for the past 5 days for the stock tsla
hist = tkr.history(period = "5d")

# drop the dividends and stock splits columns from the historical price data
hist = hist.drop("Dividends", axis = 1)
hist = hist.drop("Stock Splits", axis = 1)

# reset the index of the historical price data to the default numeric index
hist = hist.reset_index()

# set the index of the historical price data to be the date column
hist = hist.set_index("Date")

# print the resulting historical price data
print(hist)

# notes
    # pandas dataframes are similar to a regular sql tables
    # you can replace default indexing with existing columns
    # yfinance automatically indexes dataframes by date