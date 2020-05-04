import datetime
import telebot
import serial
import os

from telebot.types import Message
from telebot import apihelper
TOKEN = '1058699352:AAHWPvsN3MYdxTdfDdfE4harYflkGjXIXo0'
#PROXY = os.environ.get('PROXY')
#apihelper.proxy = {'https': PROXY}

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start','help','pager'])
def send_welcome(message):
    bot.reply_to(message, 'Введите пароль')
    bot.send_message(chat_id='119822851', text = 'хуй')
    print(message)