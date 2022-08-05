

# TeleBotCalculator

Is a Telegram-Bot designed to work with 
real-valued functions like:

- Polynomial functions
- Exponential function
- Trigonometric functions

# Installation

This Project uses the Telegram-Bot-API and SymPy.

Install all requirements with:
```bash
$ pip install -r requierements.txt
```

# Usage
1. Run the Python Script PyBot.py with
````bash
python PyBot.py
````
2. Open Telegram and start a conversation with the Bot (https://t.me/MathCalcultorBot) using the command '/start'. 

3. The Bot can answer via textmessage to following commands:
> - /simplify \<expression> 
>- /derivate \<expression> 
>- /integrate \<expression> 
>- /plot \<expression> from \<IntervallStart> to \<IntervallEnd> 
>- /maximum \<expression> (from \<IntervallStart> to \<IntervallEnd>) 
>- /minimum \<expression> (from \<IntervallStart> to \<IntervallEnd>)

Respect  the formatting of \<expression>:
- **Rule I**: Don't use whitespaces in the expression. 
- **Rule  II**: Only use 'x' as variable. 
- **Rule III**: Only use one variable.
    
### supported Operators:

| Item              | Symbol      |
|-------------------|-------------|
| decimal seperator | '.'         |
| sinus             | 'sin()'     |
| cosinus           | 'cos()'     |
| tangens           | 'tan()'     |
| square root       | 'sqrt()'    |
| power             | '**' or '^' |
| exponential       | 'exp()'     |
    
### Examples

> /simplify sin(x)\*\*2+cos(x)\*\*2

> /simplify (x\*\*3+x\*\*2-x-1)/(x\*\*2+2\*x+1)

> /derivate cos(x)

> /integrate log(x)**2

> /plot sin(x**2)

..* ![telegram-cloud-photo-size-2-5435895757724040965-x](https://user-images.githubusercontent.com/102993230/183138840-6a5e484e-484a-4898-ab25-1d1e5031340e.jpg)


> /maximum sin(x) from 1.44 to 1.99

> /minimum sin(x)*cos(x)


## Instructions for Usage
When you fulfil the requirements then you are ready to use the Telebot. You should make sure that the PyBot.py is 
running before you send a message to the TeleBot. You can send "/start" to the Telebot (https://t.me/MathCalcultorBot) 
to start. He will give you a short overview about what he can do. Then you can send a message with one of the 
supported commands. Important: you need to put a slash '/' in front of it. Eg.: /simplify 2*x+2*2+2*x−5*x  
If you need help then you can text him "/help" and he will send you a message with information about some 
important rules and allowed operators.

