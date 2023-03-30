-- sql query to retrieve historical prices of stocks with previous price for each stock
-- "select date, ticker, price," specifies the columns to be included in the result set
-- "lag(price) over" applies the lag function to the price column in the stocks table
-- "partition by ticker" partitions the result set by the ticker column meaning the lag function is applied separately to each group of rows with the same ticker
-- "order by date" orders the result set by the date meaning the lag function retrieves the value from the previous row with the closest previous date for each group of rows with the same ticker
-- "as prev_price" gives a name to the new column that contains the previous price
SELECT date, ticker, price, LAG(price) OVER(PARTITION BY ticker ORDER BY date) AS prev_price FROM stocks;

-- sql query to retrieve the rows of only those tickers whose prices did not drop more than one percent from the previous day over the period specified
-- select all columns from the stocks table
-- join with a subquery that selects tickers where the ratio of the current price to the previous price is less than 0.99
-- select only distinct tickers from a subquery that calculates the ratio of the current price to the previous price
-- calculate the ratio of the current price to the previous price using the lag function and partition by ticker
-- filter out rows where the ticker in the subquery is not null indicating a ratio less than 0.99
SELECT s.* FROM stocks AS s
LEFT JOIN (
    SELECT DISTINCT(ticker) 
    FROM (
        SELECT price/LAG(price) OVER(PARTITION BY ticker ORDER BY date) AS dif, ticker 
        FROM stocks
    ) AS b
    WHERE dif < 0.99
) AS a ON a.ticker = s.ticker
WHERE a.ticker IS NULL;

-- notes
    -- with stock data in the database you can play queries against it using analytical sql
    -- subqueries are queries nested inside another query and usually enclosed in parentheses
    -- subqueries are often used by the main query to perform further processing or filtering