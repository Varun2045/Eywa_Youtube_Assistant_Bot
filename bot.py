import telebot

# 1. Paste the token you got from BotFather inside the quotes below
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"

# 2. Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# 3. Create a handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your YouTube Summarizer Bot. Send me a link!")

# 4. Create a handler for all other text messages (just to echo them for now)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}. (I'm still learning how to process YouTube links!)")

# 5. Keep the bot running
print("Bot is running... Press Ctrl+C to stop.")
bot.infinity_polling()