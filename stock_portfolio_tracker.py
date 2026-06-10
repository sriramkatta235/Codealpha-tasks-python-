stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 420
}

total_investment = 0
portfolio = []

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        value = stock_prices[stock] * quantity
        total_investment += value
        portfolio.append(f"{stock}, {quantity}, {value}")
    else:
        print("Stock not found.")

print("\nTotal Investment Value:", total_investment)

with open("portfolio_report.txt", "w") as file:
    file.write("Stock Portfolio Report\n")
    file.write("----------------------\n")
    for item in portfolio:
        file.write(item + "\n")
    file.write(f"\nTotal Investment Value: {total_investment}")

print("Report saved to portfolio_report.txt")
