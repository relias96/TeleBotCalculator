import telebot

with open('API_token.txt') as f:
   API_TOKEN = f.readlines()

bot = telebot.TeleBot(API_TOKEN)
