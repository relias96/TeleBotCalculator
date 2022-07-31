
import telebot
from sympy import *
import io
from PIL import Image
from sympy.parsing.sympy_parser import T


x, y, z = symbols('x y z')

with open('API_Token.txt') as f:
   API_TOKEN = str(f.read())


bot = telebot.TeleBot(API_TOKEN)

def extract_arg(arg):
    return arg.split()[1:]

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

@bot.message_handler(commands=["simplify"])
def simplify_message(message):
    term = extract_arg(message.text)[0]
    bot.reply_to(message, simplify(term))



@bot.message_handler(commands=["derivate"])
def derivate_message(message):
    term = extract_arg(message.text)[0]
    bot.reply_to(message, diff(term)) 


@bot.message_handler(commands=["integrate"])
def integrate_message(message):
    term = extract_arg(message.text)[0]
    bot.reply_to(message, integrate(term, x)) 


#function to plot a graph
@bot.message_handler(commands=["plot"])
def plot_message(message):
    args = extract_arg(message.text)[:]
    term = args[0]
    func = parse_expr(term, transformations='all')
    i, j = args[-3], args[-1]
    p1 = plot(func, show=False, xlim=(i, j), ylim=(minimum(func, x, domain=Interval(float(i),float(j))),
                                                   maximum(func, x, domain=Interval(float(i), float(j)))))
    img_buf = io.BytesIO()
    p1.save(img_buf)
    im = Image.open(img_buf)
    bot.send_photo(message.chat.id, im)

#function to find the maximum of a function
@bot.message_handler(commands=["maximum"])
def echo_message(message):
    term = extract_arg(message.text)[0]
    func = parse_expr(term, local_dict={'x':x}, transformations=T[:])
    m = maximum(func, x)
    bot.reply_to(message, m)


#function to find the minimum of a function
@bot.message_handler(commands=["minimum"])
def echo_message(message):
    term = extract_arg(message.text)[0]
    func = parse_expr(term, local_dict={'x': x}, transformations=T[:])
    m = minimum(func, x)
    bot.reply_to(message, m)


# Handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, 'command not found')

bot.infinity_polling()
