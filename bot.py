import telebot
#from telebot.types import Message

#paste your telegram bot token
TOKEN = ''
#paste your telegram ID - for receive debug message
MY_ID = 0000000

STICKER_PATH = 'stickers'

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

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.reply_to(message, "это стикер")
    
    # Check folder for download
    try:
        if not os.path.exists(STICKER_PATH):
            os.makedirs(STICKER_PATH)
    except Exception as e:
        print(e)

    #Save stiker to localdisk
    try:
        file_info = bot.get_file(message.sticker.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

		# src='/mnt/files/tmp/'+file_info.file_path;
        src = file_info.file_path;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
            
        print("stiker downloaded")


        #Send file
        bot.send_document(message.chat.id, open(src, 'rb'))
        print("stiker sent")
    except Exception as e:
        print(e)

@bot.message_handler(func=lambda message: True)
def incoming_message(message):
    print(message.text)

    # Пересылать сообщения от всех пользователей -> админу в чат
    if message.chat.id != MY_ID:
        string = buildDebugMessage(message)
        bot.send_message(MY_ID, string)

    if "подтверди" in message.text:
        bot.reply_to(message, "подтверждаю")
    else:
        bot.reply_to(message, "угу")

bot.polling()
