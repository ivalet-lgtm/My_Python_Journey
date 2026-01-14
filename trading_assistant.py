import requests

# Use Binance API to get Bitcoin price
url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# Professional settings for our assistant
target_to_sell = 98000
target_to_buy = 90000

print("--- Professional Trading Assistant ---")

try:
    response = requests.get(url, timeout=10)
    data = response.json()
    current_price = float(data["price"])

    print(f"Current Bitcoin Price: ${current_price:,.2f}")

    # Logic for decision making
    if current_price >= target_to_sell:
        print("ALERT: Price is HIGH! Strategy: Consider SELLING for profit.")
    elif current_price <= target_to_buy:
        print("ALERT: Price is LOW! Strategy: Consider BUYING more.")
    else:
        print("Status: Price is STABLE. Strategy: HOLD (No action needed).")

except Exception as e:
    print(f"Error connecting to exchange: {e}")