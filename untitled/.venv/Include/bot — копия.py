import datetime
import telebot
import serial
import os
import easygui

from telebot.types import Message
from telebot import apihelper
TOKEN = '1036114928:AAG_yhRzTMOOIPK6uXNGjCNd8WVNo3Uj3kk'
#PROXY = os.environ.get('PROXY')
#apihelper.proxy = {'https': PROXY}

bot = telebot.TeleBot(TOKEN)
# @bot.message_handler(commands=['pager'])
# def send_welcome(message):
#     bot.reply_to(message, 'Введите пароль')
#     bot.send_message(chat_id='119822851', text = 'хуй')
#     print(message)




ser=serial.Serial("COM10", 9600, timeout = 0.5, xonxoff=False, rtscts=False, dsrdtr=False)
ser.flushInput()
ser.flushOutput()
time = datetime.datetime.now()
now = time.strftime("%H:%M")

# myvar = easygui.enterbox(ser.writelines())
buf = ser.read(ser.inwaiting())
while buf == '':
    val = ser.readline(ser.inwaiting())
    print(val)


print(myvar)
s1 = b'#8e4c4f1'
s2 = b'#8e4c4f2'
s3 = b'#8e4c4f3'
s4 = b'#8e4c4f'
s5 = b'#8e4c4f4'
s6 = b'#8e4c4f5'
s7 = b'#8e4c4f6'
s8 = b'#8e4c4f7'
s9 = b'#8e4c4f8'
s10 = b'#8e4c4f9'
s11 = b'#8e4c4f10'
s12 = b'#8e4c4f11'
s13 = b'#8e4c4f12'
s14 = b'#8e4c4f13'
s15 = b'#8e4c4f14'
s16 = b'#8e4c4f15'
s17 = b'#8e4c4f16'
s18 = b'#8e4c4f17'
s19 = b'#8e4c4f18'
s20 = b'#8e4c4f19'
while True:
  data_raw = ser.readline()

  if data_raw != b'':
    if data_raw == s1:
       data_raw = ". Стол: 1й"
    if data_raw == s2:
       data_raw = ". Стол: 2й"
    if data_raw == s3:
       data_raw = ". Стол: 3й"
    if data_raw == s4:
       data_raw = ". Стол: 4й"
    if data_raw == s5:
       data_raw = ". Стол: 5й"
    if data_raw == s6:
       data_raw = ". Стол: 6й"
    if data_raw == s7:
       data_raw = ". Стол: 7й"
    if data_raw == s8:
       data_raw = ". Стол: 8й"
    if data_raw == s9:
       data_raw = ". Стол: 9й"
    if data_raw == s10:
       data_raw = ". Стол: 10й"
    if data_raw == s11:
       data_raw = ". Стол: 11й"
    if data_raw == s12:
       data_raw = ". Стол: 12й"
    if data_raw == s13:
       data_raw = ". Стол: 13й"
    if data_raw == s14:
       data_raw = ". Стол: 14й"
    if data_raw == s15:
       data_raw = ". Стол: 15й"
    if data_raw == s16:
       data_raw = ". Стол: 16й"
    if data_raw == s17:
       data_raw = ". Бар напитков"
    if data_raw == s18:
       data_raw = ". Кальян бар"
    if data_raw == s19:
       data_raw = ". Кухня"
    if data_raw == s19:
       data_raw = ". VIP кабинка"
    text1 = 'Вызов в '
    final_message = text1 + now + data_raw
    print(str('Вызов в'), now,  data_raw)

    @bot.message_handler(commands=['pager'])
    def send_welcome(message):
        bot.reply_to(message, 'Введите пароль')
        print(message)
    bot.send_message(chat_id='119822851', text=final_message)
    bot.send_message(chat_id='825546201', text=final_message)
    # bot.polling()