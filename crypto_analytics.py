import requests
import pandas as pd
from datetime import datetime
import time
import matplotlib.pyplot as plt

# 1. Function to fetch price from Binance
def get_crypto_price(symbol="BTCUSDT"):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url)
        data = response.json()
        return float(data['price'])
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# 2. Data collection (Fetching price 7 times for a better graph)
prices_list = []
points_to_collect = 7

print("--- Starting Data Collection for Portfolio Project ---")
for i in range(points_to_collect):
    price = get_crypto_price()
    if price:
        timestamp = datetime.now().strftime("%H:%M:%S")
        prices_list.append({"Time": timestamp, "Price": price})
        print(f"[{i+1}/{points_to_collect}] Time: {timestamp} | Price: ${price}")
    
    if i < points_to_collect - 1:
        time.sleep(3) # Wait 3 seconds between updates

# 3. Process data with Pandas
df = pd.DataFrame(prices_list)

# Save to CSV
df.to_csv("btc_prices_history.csv", index=False)
print("\n[SUCCESS] Data saved to 'btc_prices_history.csv'")

# 4. Statistical Analysis
print("\n--- Market Analysis Summary ---")
avg_p = df['Price'].mean()
max_p = df['Price'].max()
min_p = df['Price'].min()

print(f"Average Price: ${avg_p:.2f}")
print(f"Highest Price: ${max_p:.2f}")
print(f"Lowest Price: ${min_p:.2f}")

# 5. Data Visualization (Creating the Chart)
print("\nGenerating visual report...")
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['Price'], marker='o', linestyle='-', color='#1f77b4', linewidth=2)

# Adding labels and style
plt.title('Bitcoin Price Monitoring (Real-Time)', fontsize=14)
plt.xlabel('Time (HH:MM:SS)', fontsize=12)
plt.ylabel('Price in USD', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Save the plot as an image for Upwork Portfolio
plt.savefig("btc_price_chart.png")
print("[SUCCESS] Chart saved as 'btc_price_chart.png'")

# Show the chart window
print("\nOpening chart window... (Close the window to finish)")
plt.show()