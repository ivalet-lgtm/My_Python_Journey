import requests

# Using Binance API (Alternative source)
url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

print("--- Automated Bitcoin Price Tracker (Binance) ---")

try:
    response = requests.get(url, timeout=10)
    data = response.json()
    
    # Binance returns data in a simpler format: {"symbol":"BTCUSDT","price":"95123.45"}
    price = data["price"]
    symbol = data["symbol"]

    print(f"Connection Status: Success!")
    print(f"Asset: {symbol}")
    print(f"Current Price: ${float(price):,.2f}") # Format as a nice number

except Exception as e:
    print(f"Failed to fetch data. Error: {e}")