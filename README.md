

# TeleBotCalculator

Is a Telegram-Bot designed to work with 
real-valued functions like:

- Polynomial functions
- Exponential function
- Trigonometric functions
- etc.

# Installation

This Project uses the [Telegram-Bot-API](https://github.com/eternnoir/pyTelegramBotAPI) and [SymPy](https://docs.sympy.org/dev/index.html).

Install all requirements with:
```bash
$ pip install -r requierements.txt
```

# Usage
1. Run the Python Script PyBot.py with
````bash
python PyBot.py
````
2. Open Telegram and start a conversation with the [Bot](https://t.me/MathCalcultorBot) using the command '/start'. 

3. The Bot can answer via textmessage to following commands:
> - /simplify \<expression> 
>- /derivate \<expression > 
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
>>

> /simplify (x\*\*3+x\*\*2-x-1)/(x\*\*2+2\*x+1)
>>

> /plot x\*\*3-3*x\*\*2+2\*x
>>

> /maximum -x**2-2x+1
>>



