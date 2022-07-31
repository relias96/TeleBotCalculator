import sympy
import telebot
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

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


@bot.message_handler(regexp="simplify .*")
def echo_message(message):
    term = message.text.replace('simplify ', '')
    bot.send_message(message.chat.id, simplify(term))

@bot.message_handler(regexp="derivate .*")
def echo_message(message):
    term = message.text.replace('derivate ', '')
    bot.reply_to(message, term) 

@bot.message_handler(regexp="integrade .*")
def echo_message(message):
    term = message.text.replace('integrade ', '')
    bot.reply_to(message, term) 

#function to plot a graph
@bot.message_handler(regexp="plot .* from\[\d+,\d+\]")
def echo_message(message):
    term = message.text.replace('plot ', '')
    term, intervals = term.split('from')
    func = sympy.parse_expr(term)
    i, j = intervals.replace("[","").replace("]","").split(",")
    plt.style.use('ggplot')
    x = np.linspace(float(i), float(j), 1000)
    y = func(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='x', ylabel='y',
           xlim=(float(i), float(j)), xticks=np.arange(float(i), float(j)),
           ylim=(min(y), max(y)),yticks=np.arange(min(y), max(y)))
    plt.show()
    bot.send_photo(message.chat.id, plt.gcf())

#function to find the maximum of a function
@bot.message_handler(regexp="maximum .*")
def echo_message(message):
    term = message.text.replace('maximum ', '')
    term = maximum(term, x)
    bot.reply_to(message, term) 

#function to find the minimum of a function
@bot.message_handler(regexp="minimum .*")
def echo_message(message):
    term = message.text.replace('minimum ', '')
    term = minimum(term, x)
    bot.reply_to(message, term) 



bot.infinity_polling()
