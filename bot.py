import telebot
#from telebot.types import Message

#paste your telegram bot token
TOKEN = ''
#paste your telegram ID - for receive debug message
MY_ID = 0000000

bot = telebot.TeleBot(TOKEN)

bot.send_message(MY_ID, 'START!')

@bot.message_handler(func=lambda message: True)
def incoming_message(message):
    print(message.text)
    if "подтверди" in message.text:
        bot.reply_to(message, "подтверждаю")
    else:
        bot.reply_to(message, "угу")

bot.polling()
