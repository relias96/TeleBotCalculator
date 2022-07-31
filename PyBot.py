import telebot
from sympy import *

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

with open('API_Token.txt') as f:
   API_TOKEN = str(f.read())


bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am TeleBotCalculator.\n
I can reply to the following commands:\n
- simplify\n
- derivate\n
- integrate\n
- plot\n
- maximum\n
- minimum
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(regexp="simplify .*")
def echo_message(message):
    term = message.text.replace('simplify ', '')
    bot.reply_to(message, simplify(term)) 

@bot.message_handler(regexp="derivate .*")
def echo_message(message):
    term = message.text.replace('derivate ', '')
    bot.reply_to(message, term) 

@bot.message_handler(regexp="integrade .*")
def echo_message(message):
    term = message.text.replace('integrade ', '')
    bot.reply_to(message, term) 

@bot.message_handler(regexp="plot .*")
def echo_message(message):
    term = message.text.replace('plot ', '')
    bot.reply_to(message, term) 

@bot.message_handler(regexp="maximum .*")
def echo_message(message):
    term = message.text.replace('maximum ', '')
    bot.reply_to(message, term) 

@bot.message_handler(regexp="minimum .*")
def echo_message(message):
    term = message.text.replace('minimum ', '')
    bot.reply_to(message, term) 




# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, 'command not found')
    




bot.infinity_polling()
