
import telebot
from sympy import *
import io
from PIL import Image


x, y, z = symbols('x y z')

with open('API_Token.txt') as f:
   API_TOKEN = str(f.read())


bot = telebot.TeleBot(API_TOKEN)

def extract_arg(arg):
    return arg.split()[1:]



def getAnswerXY(term, y):
    '''
    calculates the x value  an y value
    :param term: String or sympy-expression
    :param y: Number (value)
    :return: String of the calculated values
    '''
    if y < 0:
        toSolve = "%s+%s" % (term, y)
    else:
        toSolve = "%s-%s" % (term, y)
    mx = solve(parse_expr(toSolve, local_dict={'x': x}, transformations='all'))[0]
    return "x = %s \ny = %s " % (mx, y)

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    '''
    Message when starting the Bot
    :return: Writes a message in the Chat
    '''
    bot.reply_to(message, """
        Hi there, I am TeleBotCalculator.\n
        I can reply to the following commands:\n
        - /simplify <expression>\n
        - /derivate <expression>\n
        - /integrate < expression>\n
        - /plot <expression> from <IntervallStart> to <IntervallEnd>\n
        - /maximum <expression> (from <IntervallStart> to <IntervallEnd>)\n
        - /minimum <expression> (from <IntervallStart> to <IntervallEnd>)\n
        Write the command "/help" to get more information about the functions """)

# Handle '/help'
@bot.message_handler(commands=['help'])
def send_help(message):
    '''
    Sends a message if help is requiered
    :return: Writes helpfull information in the Chat
    '''
    bot.reply_to(message, """\
    
    Start every command with a Slash ('/')
    
    If you get not Answer, maybe the Bot crashed. Then restart the Bot.
    
    Rule I: Don't use whitespaces in the expression. \n
    Rule II: Only use 'x' as variable. \n
    Rule III: Only use one variable.\n
    
    supported Operators:
    decimal seperator   --> '.'\n
    sinus               --> 'sin()'\n
    quareroot           --> 'sqrt()'\n
    power               --> '**' or '^'\n
    exponetial          --> 'exp()'\n
    """)


# Handle '/simplify'
@bot.message_handler(commands=["simplify"])
def simplify_message(message):
    '''
    Simplifies a given term using Sympy.
    :return: Writes the simplified term in the chat.
    '''
    term = extract_arg(message.text)[0]
    bot.reply_to(message, simplify(term))


# Handle '/derivate'
@bot.message_handler(commands=["derivate"])
def derivate_message(message):
    '''
    Derivates a given term using Sympy.
    :return: Writes the derivate of the term in the chat
    '''
    term = extract_arg(message.text)[0]
    bot.reply_to(message, diff(term))


# Handle '/integrate'
@bot.message_handler(commands=["integrate"])
def integrate_message(message):
    '''
    Integrates a given term using Sympy.
    :return: Writes the 1. integration of the term in the chat
    '''
    term = extract_arg(message.text)[0]
    bot.reply_to(message, integrate(term, x))


#Handle '/plot'
@bot.message_handler(commands=["plot"])
def plot_message(message):
    '''
    Plots the Term
    :return: Sends an image of the plot into the chat
    '''
    args = extract_arg(message.text)[:]
    term = args[0]
    func = parse_expr(term, local_dict={'x':x}, transformations='all')
    img_buf = io.BytesIO()
    if len(args) == 5:
        i, j = args[-3], args[-1]
        p1 = plotting.plot(func, show=False, xlim=(i, j), ylim=(minimum(func, x, domain=Interval(float(i),float(j))),
                                                   maximum(func, x, domain=Interval(float(i), float(j)))))
        p1.save(img_buf)
        im = Image.open(img_buf)
    else:
        p1 = plotting.plot(func, show=False)
        p1.save(img_buf)
        im = Image.open(img_buf)
    bot.send_photo(message.chat.id, im)


# Handle '/maximum'
@bot.message_handler(commands=["maximum"])
def echo_message(message):
    '''
    Calculates the position x and the maximal value y of the given term
    :return: returns the x and y value via Textmessage
    '''
    args = extract_arg(message.text)[:]
    term = args[0]
    func = parse_expr(term, local_dict={'x': x}, transformations='all')
    if len(args) == 5:
        i, j = args[-3], args[-1]
        my = maximum(func, x, Interval(float(i), float(j)))
        answer = getAnswerXY(term, my)
    else:
        my = maximum(func, x)
        answer = getAnswerXY(term, my)
    bot.reply_to(message, answer)



# Handle '/minimum'
@bot.message_handler(commands=["minimum"])
def echo_message(message):
    '''
    Calculates the position x and the minimal value y of the given term
    :return: returns the x and y value via Textmessage
    '''
    args = extract_arg(message.text)[:]
    term = args[0]
    func = parse_expr(term, local_dict={'x': x}, transformations='all')
    if len(args) == 5:
        i, j = args[-3], args[-1]
        my = minimum(func, x, Interval(float(i), float(j)))
        answer = getAnswerXY(term, my)
    else:
        my = minimum(func, x)
        answer = getAnswerXY(term, my)
    bot.reply_to(message, answer)

@bot.message_handler(commands=["evaluate"])
def evaluate(message):
    '''
    Evaluates a term
    :param message:
    :return: A Number as solution of the equation
    '''
    args = extract_arg(message.text)[:]
    term = args[0]
    func = parse_expr(term, local_dict={'x': x}, transformations='all')
    m = func.evalf()
    bot.reply_to(message, m)

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    '''
    Sends a message if no command is not found
    :return: String 'command not found'
    '''
    bot.reply_to(message, 'command not found')


bot.infinity_polling()
