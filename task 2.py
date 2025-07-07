# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3500,
    "MSFT": 310
}

portfolio = {}
total_investment = 0

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("❌ Invalid number. Try again.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"✅ Added {quantity} shares of {stock} worth ${investment}")
    print()

# Display portfolio summary
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment: ${total_investment}")

# Optional: Save to file
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print("📁 Portfolio saved to 'portfolio_summary.txt'")
