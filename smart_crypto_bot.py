import telebot
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time
import os

# Configuration
TOKEN = "8504559981:AAFspiT9zI1QrKL-lBibJsTzVndVl6F380Y"
bot = telebot.TeleBot(TOKEN)

def get_btc_price():
    """Fetches real-time BTC price from Binance API."""
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    try:
        data = requests.get(url).json()
        return float(data['price'])
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def create_report():
    """Collects market data, processes it with Pandas, and generates a visual chart."""
    prices = []
    times = []
    
    print("Log: Generating analytics report...")
    # Collecting 5 data points for the trend chart
    for i in range(5):
        p = get_btc_price()
        if p:
            t = datetime.now().strftime("%H:%M:%S")
            prices.append(p)
            times.append(t)
        time.sleep(1) # Interval between data points
    
    # Create DataFrame for analysis
    df = pd.DataFrame({"Time": times, "Price": prices})
    
    # Visualization using Matplotlib
    plt.figure(figsize=(8, 4))
    plt.plot(df['Time'], df['Price'], marker='o', color='green', linewidth=2)
    plt.title("Bitcoin Price Performance (Real-Time)")
    plt.xlabel("Timestamp")
    plt.ylabel("Price (USD)")
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Export chart as image
    file_path = "report.png"
    plt.savefig(file_path)
    plt.close() # Close plot to free up memory
    return file_path

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Sends a greeting and list of available commands."""
    welcome_text = (
        "Welcome to AiBatono Crypto Bot! 🚀\n\n"
        "Available commands:\n"
        "/price - Get live Bitcoin price\n"
        "/report - Generate a 5-second analytics chart"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['price'])
def send_price(message):
    """Replies with the current market price."""
    price = get_btc_price()
    if price:
        bot.send_message(message.chat.id, f"🎯 Current BTC Price: ${price:,.2f}")

@bot.message_handler(commands=['report'])
def send_report(message):
    """Triggers the data collection and sends the generated chart to the user."""
    bot.send_message(message.chat.id, "📊 Analyzing market data, please wait...")
    
    try:
        photo_path = create_report()
        # Send the generated chart image
        with open(photo_path, 'rb') as photo:
            bot.send_photo(
                message.chat.id, 
                photo, 
                caption="✅ Here is your real-time market analysis report."
            )
        # Cleanup: Remove the temporary file
        os.remove(photo_path)
    except Exception as e:
        bot.send_message(message.chat.id, "❌ Sorry, I couldn't generate the report.")
        print(f"Error in report generation: {e}")

# Start the bot
if __name__ == "__main__":
    print("Status: AiBatono Bot is now online...")
    bot.polling(none_stop=True)
