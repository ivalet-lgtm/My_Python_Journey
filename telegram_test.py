import telebot

# Paste your Token from BotFather here
BOT_TOKEN = "8504559981:AAFspiT9zI1QrKL-lBibJsTzVndVl6F380Y"
# Paste your ID from userinfobot here
CHAT_ID = "6196771679"

bot = telebot.TeleBot(BOT_TOKEN)

print("--- Telegram Bot Test ---")

try:
    bot.send_message(CHAT_ID, "Hello! Your Python Bot is now online. 🚀")
    print("Success: Message sent to your Telegram!")
except Exception as e:
    print(f"Error: Could not send message. {e}")