import telebot
#from telebot.types import Message

#paste your telegram bot token
TOKEN = ''
#paste your telegram ID - for receive debug message
MY_ID = 0000000

bot = telebot.TeleBot(TOKEN)

bot.send_message(MY_ID, 'START!')

def buildDebugMessage(message):
    now = datetime.datetime.now()
    now = now.strftime("%d-%m-%Y %H:%M:%S")
    contentType = str(message.content_type)
    string = "%s %s %s (@%s id: %i)\nContentType: %s\n" % (now, message.chat.first_name, message.chat.last_name, message.chat.username, message.chat.id, contentType)
    if contentType == 'text':
        string += 'Text: %s' % (message.text)

    return string

@bot.message_handler(func=lambda message: True)
def incoming_message(message):
    print(message.text)
    
    #Forward all messages to MY_ID
    if message.chat.id != MY_ID:
        string = buildDebugMessage(message)
        bot.send_message(MY_ID, string)

    if "подтверди" in message.text:
        bot.reply_to(message, "подтверждаю")
    else:
        bot.reply_to(message, "угу")

bot.polling()
