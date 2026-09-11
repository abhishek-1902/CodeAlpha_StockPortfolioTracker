import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

portfolio = []

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter 'done' when you have finished.\n")

while True:
    stock = input("Enter stock symbol: ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.\n")
            continue

    except ValueError:
        print("Please enter a valid number.\n")
        continue

    price = stock_prices[stock]
    total = price * quantity

    portfolio.append({
        "stock": stock,
        "quantity": quantity,
        "price": price,
        "total": total
    })

    print(f"Added {quantity} shares of {stock}.")
    print(f"Investment: ${total:,.2f}\n")

# Calculate total investment
total_investment = sum(item["total"] for item in portfolio)

print("\n" + "=" * 45)
print("           PORTFOLIO SUMMARY")
print("=" * 45)

if portfolio:
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<12}{'Total':<12}")
    print("-" * 45)

    for item in portfolio:
        print(
            f"{item['stock']:<10}"
            f"{item['quantity']:<10}"
            f"${item['price']:<11,.2f}"
            f"${item['total']:<11,.2f}"
        )

    print("-" * 45)
    print(f"Total Investment: ${total_investment:,.2f}")

    # Save portfolio to CSV
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Stock", "Quantity", "Price", "Total"])

        for item in portfolio:
            writer.writerow([
                item["stock"],
                item["quantity"],
                item["price"],
                item["total"]
            ])

    print("\nPortfolio saved successfully to portfolio.csv")

else:
    print("No stocks were added to the portfolio.")

print("\nThank you for using Stock Portfolio Tracker!")
