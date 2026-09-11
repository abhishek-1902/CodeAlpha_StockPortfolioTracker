A command-line stock portfolio tracker built with Python for the CodeAlpha Python Programming Internship.

## Features
- Uses a hardcoded dictionary of stock prices.
- Accepts stock symbols and quantities from the user.
- Calculates the value of each holding.
- Calculates total portfolio investment.
- Validates stock symbols and quantities.
- Saves the portfolio summary to `portfolio.csv`.

## Technologies
- `csv` module

## Sample Output
```text
===== STOCK PORTFOLIO TRACKER =====
Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN
Type 'done' when you have finished adding stocks.

Enter stock symbol: AAPL
Enter quantity of AAPL: 5

Enter stock symbol: TSLA
Enter quantity of TSLA: 2

Enter stock symbol: done

===== PORTFOLIO SUMMARY =====
AAPL: 5 shares × $180.00 = $900.00
TSLA: 2 shares × $250.00 = $500.00

Total Investment: $1400.00
Portfolio saved to portfolio.csv
```

## CSV Output
```csv
Stock,Quantity,Price,Value
AAPL,5,180.00,900.00
TSLA,2,250.00,500.00

Total Investment,,,1400.00
```


