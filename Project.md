# Project scientific programming in Python

## Mathematics-Telegram-Bot 
from Robin Elias and Lara Ruschmeyer
## Goal of the Project
This Project is about to code an Telegram-Bot. It should take in mathematical expressions (eg „sin(x*2pi)“ ) and then perform some kind of action on it.
implementet actions should be: 
- „simplify“
- „derivate“
- „integrate“
- „plot“
- „maximum“ 
- „minimum“

The Bot should reply via text message if some Calculation is done or send a picture if a plot was requested.

## Required Steps
1. Create a Telegram-Bot
   1. Generate a API-token for the new Bot
   2. Write functions for the Bot so that he can react to different requests.
1. Take in an expression by parsing the input-string to an SymPy-function 
   1. Calculate the output for the requested operation

## Libraries to Use
- pyTelegramBotAPI (https://github.com/eternnoir/pyTelegramBotAPI) 
- SymPy (https://docs.sympy.org/latest/index.html)
- Matplotlib (https://matplotlib.org)
- SciPy (https://scipy.org)