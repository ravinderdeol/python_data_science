-- "select date, ticker, price," specifies the columns to be included in the result set
-- "lag(price) over" applies the lag function to the price column in the stocks table
-- "partition by ticker" partitions the result set by the ticker column meaning the lag function is applied separately to each group of rows with the same ticker
-- "order by date" orders the result set by the date meaning the lag function retrieves the value from the previous row with the closest previous date for each group of rows with the same ticker
-- "as prev_price" gives a name to the new column that contains the previous price
SELECT date, ticker, price, LAG(price) OVER(PARTITION BY ticker ORDER BY date) AS prev_price FROM stocks;

-- notes
    -- with stock data in the database you can play queries against it using analytical sql