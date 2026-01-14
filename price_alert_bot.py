import requests
import telebot
import time

# Credentials (Fill these locally, but clear them before uploading to GitHub)
BOT_TOKEN = "8504559981:AAFspiT9zI1QrKL-lBibJsTzVndVl6F380Y"
CHAT_ID = "6196771679"

bot = telebot.TeleBot(BOT_TOKEN)

def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    return float(response.json()["price"])

print("--- Professional Price Monitor Started ---")

# This is an infinite loop that checks the price every 60 seconds
while True:
    try:
        current_price = get_btc_price()
        
        # We only send a message if it's a specific "alert" 
        # For example, if price is above 97,000
        if current_price > 97000:
            msg = f"⚠️ ALERT: Bitcoin is booming! Current price: ${current_price:,.2f}"
            bot.send_message(CHAT_ID, msg)
            print("Alert sent to Telegram!")
        
        print(f"Monitoring... Current Price: ${current_price:,.2f}")
        
        # Wait for 60 seconds before checking again
        time.sleep(60) 
        
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10) # Wait a bit before retrying