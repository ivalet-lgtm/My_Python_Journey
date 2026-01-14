import telebot
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time
import os

TOKEN = "8504559981:AAFspiT9zI1QrKL-lBibJsTzVndVl6F380Y"
bot = telebot.TeleBot(TOKEN)

def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    return float(data['price'])

def create_report():
    prices = []
    times = []
    
    print("Generating report for user...")
    for i in range(5):
        p = get_btc_price()
        t = datetime.now().strftime("%H:%M:%S")
        prices.append(p)
        times.append(t)
        time.sleep(1)
    
    df = pd.DataFrame({"Time": times, "Price": prices})
    
    plt.figure(figsize=(8, 4))
    plt.plot(df['Time'], df['Price'], marker='o', color='green')
    plt.title("Bitcoin Price Report")
    plt.grid(True)
    
    file_path = "report.png"
    plt.savefig(file_path)
    plt.close()
    return file_path

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Use /price for current price or /report for a 5-second chart.")

@bot.message_handler(commands=['price'])
def send_price(message):
    price = get_btc_price()
    bot.send_message(message.chat.id, f"Current BTC Price: ${price}")

@bot.message_handler(commands=['report'])
def send_report(message):
    bot.send_message(message.chat.id, "Wait a moment, I'm analyzing the market...")
    
    photo_path = create_report()
    

    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption="Here is your real-time analysis!")
    

    os.remove(photo_path)

print("Bot is running...")
bot.polling()