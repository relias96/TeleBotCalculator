import telebot

with open('API_Token.txt') as f:
   API_TOKEN = str(f.read())


bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am TeleBotCalculator.\
I can reply to the following commands:\
- simplify\
- derivate\
- integrate\
- plot\
- maximum\
- minimum\ 
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
