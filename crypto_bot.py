import requests
import telebot

# Credentials
BOT_TOKEN = "YOUR_TOKEN_HERE"
CHAT_ID = "6196771679" 

bot = telebot.TeleBot(BOT_TOKEN)

def get_crypto_update():
    # Fetching price from Binance
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    price = float(data["price"])
    return price

print("--- Sending Live Crypto Update to Telegram ---")

try:
    btc_price = get_crypto_update()
    
    # Building a professional message
    message = (
        f"💰 *Bitcoin Live Update*\n\n"
        f"Current Price: ${btc_price:,.2f}\n"
        f"Status: Market is Active ✅\n\n"
        f"Strategy: HOLD 🚀"
    )
    
    # We use parse_mode='Markdown' to make the text bold
    bot.send_message(CHAT_ID, message, parse_mode='Markdown')
    print("Success: Message sent!")

except Exception as e:

    print(f"Error: {e}")
