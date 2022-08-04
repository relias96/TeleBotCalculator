# TeleBotCalculator

For more information about the Telegram-Bot-API follow the link:
  https://pytba.readthedocs.io/en/latest/index.html

The Bot has the Name: https://t.me/MathCalcultorBot


## Goal of the Project

This Project is about to code an Telegram-Bot. It should take as input mathematical expressions (eg. „sin(x*2pi)“ ) and then perform some kind of action on it, depending on the given command.

### Supported commands will be: 

- /simplify <expression> 
- /derivate <expression> 
- /integrate < expression> 
- /plot <expression> from <IntervallStart> to <IntervallEnd> 
- /maximum <expression> (from <IntervallStart> to <IntervallEnd>) 
- /minimum <expression> (from <IntervallStart> to <IntervallEnd>)

The Bot replies via text message if some calculation is done or send a photo if a plot was requested.


## Instructions for Usage
When you fulfil the requirements then you are ready to use the Telebot. You shold make sure that the PyBot.py is running before you send a message to the TeleBot. You can send "/start" to the Telebot (https://t.me/MathCalcultorBot) to start. He will give you a short overwiew about what he can do. Then you can send a message with one of the supported commands. Important: you need to put a slash '/' infront of it. Eg.: /simplify 2*x+2*2+2*x−5*x  
If you need help then you can text him "/help" and he will send you a message with information about some important rules and allowed operators.


## Requirements to Use the TeleBot

- pyTelegramBotAPI (https://github.com/eternnoir/pyTelegramBotAPI) 
- SymPy (https://docs.sympy.org/latest/index.html)
- Matplotlib (https://matplotlib.org)
- SciPy (https://scipy.org)

