import telebot
import requests
import pandas as pd
import os
from datetime import datetime

# --- CONFIGURATION ---
# Using the credentials from your screenshots
BOT_TOKEN = "8504559981:AAFspiT9zI1QrKL-lBibJsTzVndVl6F380Y"
CHAT_ID = "6196771679"
SYMBOL = "BTCUSDT"
DATABASE_FILE = "crypto_history.csv"

bot = telebot.TeleBot(BOT_TOKEN)

# 1. Fetch live price from Binance API
def get_crypto_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url).json()
        return float(response['price'])
    except Exception as e:
        print(f"API Error: {e}")
        return None

# 2. Save data to Excel/CSV for analytics
def save_to_history(price):
    data = {
        'Timestamp': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
        'Asset': [SYMBOL],
        'Price_USD': [price]
    }
    df = pd.DataFrame(data)
    
    # Create file with headers if it doesn't exist, otherwise append without headers
    if not os.path.isfile(DATABASE_FILE):
        df.to_csv(DATABASE_FILE, index=False)
    else:
        df.to_csv(DATABASE_FILE, mode='a', index=False, header=False)

# --- TELEGRAM BOT COMMANDS ---

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🚀 **Crypto Tracker Bot is Active**\n\n"
        "Available commands:\n"
        "/price - Get live BTC price and log data\n"
        "/report - Download historical data (CSV/Excel)"
    )
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

@bot.message_handler(commands=['price'])
def handle_price(message):
    price = get_crypto_price(SYMBOL)
    if price:
        save_to_history(price)
        response = f"🎯 **Current {SYMBOL} Price:** `${price}`\n✅ Data has been logged to history."
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "⚠️ Failed to fetch price from API.")

@bot.message_handler(commands=['report'])
def handle_report(message):
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'rb') as file:
            bot.send_document(
                message.chat.id, 
                file, 
                caption="📊 **Crypto Market History Report**\nOpen this file in Excel for analysis."
            )
    else:
        bot.reply_to(message, "❌ History is empty. Use /price to collect data.")

# Start the bot
if __name__ == "__main__":
    print("--- Crypto Analysis Bot is running... ---")
    bot.polling(none_stop=True)
