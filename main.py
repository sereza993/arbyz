from config import token

import telebot

API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
привет я арбузик бот я пока глупый но скоро научусь)!\
""")

@bot.message_handler(content_types=['photo'] )
def send_photo(message):
    bot.reply_to(message, f'это фото')





@bot.message_handler(commands=['arbuz' ])
def send_kakoi(message):
    bot.send_message(message.chat.id, "большой арбуз")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()


