import telebot
import os
import sys
import io




from telebot import apihelper
from telebot.types import Message
from telebot import types
TOKEN = '1008865727:AAHTgEAI1P0cVAxEraqUzfI6el_p3aUHWEs'

apihelper.proxy = {'https':'socks5://14611055481:U777Vluhz8@orbtl.s5.opennetwork.cc:999'}
bot = telebot.TeleBot(TOKEN)


schet = ['10000', '10100', '10101', '10111', '10102', '10112', '10122', '10132', '10103', '10113', '10133', '10104',
        '10124', '10134', '10105', '10115', '10125', '10135', '10106', '10126', '10136', '10107', '10127', '10137',
        '10108', '10128', '10138', '10200', '10220', '10230', '10300', '10301', '10311', '10302', '10312', '10303',
        '10313', '10400', '10401', '10411', '10441', '10451', '10402', '10412', '10422', '10432', '10442', '10403',
        '10413', '10433', '10404', '10424', '10434', '10444', '10405', '10415', '10425', '10435', '10445', '10406',
        '10426', '10436', '10446', '10407', '10427', '10437', '10447', '10408', '10428', '10438', '10448', '10409',
        '10429', '10439', '10449', '10500', '10501', '10521', '10531', '10502', '10522', '10532', '10503', '10523',
        '10533', '10504', '10524', '10534', '10505', '10525', '10535', '10506', '10526', '10536', '10507', '10527',
        '10537', '10508', '10528', '10538', '10509', '10539', '10600', '10601', '10611', '10621', '10631', '10641',
        '10691', '10602', '10622', '10632', '10603', '10613', '10633', '10693', '10604', '10624', '10634', '10700',
        '10701', '10711', '10721', '10731', '10703', '10723', '10733', '10900', '10960', '10970', '10980', '10990',
        '11100', '11101', '11141', '11102', '11142', '11104', '11144', '11105', '11145', '11106', '11146', '11107',
        '11147', '11108', '11148', '11109', '11149', '11400', '11410', '11430', '11442', '11444', '11460', '20000',
        '20100', '20101', '20111', '20121', '20103', '20113', '20123', '20104', '20134', '20105', '20135', '20106',
        '20126', '20107', '20127', '20400', '20421', '20422', '20423', '20431', '20434', '20451', '20452', '20453',
        '20500', '20521', '20522', '20523', '20524', '20526', '20527', '20528', '20529', '2052K', '20531', '20532',
        '20533', '20535', '20541', '20544', '20545', '20552', '20553', '20554', '20555', '20562', '20565', '20571',
        '20572', '20573', '20574', '20575', '20581', '20589', '20600', '20611', '20612', '20613', '20614', '20621',
        '20622', '20623', '20624', '20625', '20626', '20627', '20628', '20629', '20631', '20632', '20633', '20634',
        '20641', '20642', '20643', '20644', '20645', '20646', '2064A', '2064B', '20652', '20653', '20662', '20663',
        '20664', '20666', '20667', '20681', '20696', '20697', '20698', '20700', '20704', '20800', '20811', '20812',
        '20813', '20814', '20821', '20822', '20823', '20824', '20825', '20826', '20827', '20828', '20829', '20831',
        '20832', '20834', '20862', '20863', '20864', '20865', '20866', '20867', '20891', '20893', '20895', '20896',
        '20897', '20900', '20930', '20940', '20971', '20972', '20973', '20974', '20981', '20982', '20989', '21000',
        '21010', '21500', '21003', '21005', '21006', '30000', '30100', '30104', '30101', '30102', '30200', '30211',
        '30212', '30213', '30214', '30221', '30222', '30223', '30224', '30225', '30226', '30227', '30228', '30229',
        '30231', '30232', '30233', '30234', '30241', '30242', '30243', '30244', '30245', '30246', '30249', '3024A',
        '3024B', '30252', '30253', '30261', '30262', '30263', '30264', '30265', '30266', '30267', '30273', '30275',
        '30281', '30293', '30295', '30296', '30297', '30298', '30300', '30301', '30302', '30303', '30304', '30305',
        '30306', '30307', '30308', '30309', '30310', '30311', '30312', '30313', '30400', '30401', '30402', '30403',
        '30404', '30406', '30484', '30486', '30494', '30496', '40000', '40100', '40110', '40118', '40119', '40120',
        '40128', '40129', '40130', '40140', '40150', '40160', '50000', '50200', '50210', '50220', '50230', '50240',
        '50290', '50400', '50410', '50420', '50430', '50440', '50490', '50600', '50610', '50620', '50690', '50700',
        '50710', '50720', '50730', '50740', '50790', '50800', '50810', '50820', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '20', '21', '22', '23', '24', '25', '26',
        '27', '29', '30', '31', '40', '117', '118']

provodka = ['Проводки 30211']

markup = types.ReplyKeyboardMarkup(row_width=1)
# markup = types.InlineKeyboardMarkup()

btn1 = types.KeyboardButton('Справочник счетов')
btn2 = types.KeyboardButton('Справочник проводок')
markup.add(btn1, btn2)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Привет. Я Бот-справочник.\n'
                          'Вы можете спрашивать меня про счета.\n'
                          'К примеру, напишите номер счета и я Вам расскажу о нем.\n'
                          'Если хотите перейти в начальное меню, напишите мне start\n'
                          'Начинаем. Выберите, что хотите уточнить:', reply_markup=markup)
    print(message)



@bot.message_handler(content_types=['text'])

def handle_text(message):
    chat_id = message.chat.id
    text = message.text
    if text == 'Справочник счетов':
        msg  = bot.send_message(chat_id, 'Отлично. Теперь можете написать код счета, а я подскажу его определение...')
        bot.register_next_step_handler(msg ,scheta)
    elif message.text == 'Справочник проводок':
        msg  = bot.send_message(chat_id, 'Отлично. Теперь можете написать код счета, а я Вам какие проводки по нему бывают...')
        bot.register_next_step_handler(msg, provodki)
    else:
        bot.send_message(chat_id, 'Мне не знакома эта команда, для начала сделайте выбор из предложенного.')



def scheta(message):
    chat_id = message.chat.id
    text = message.text
    try:
        if text == 'Справочник счетов':
            msg = bot.send_message(chat_id, 'Пробуем заново. Напишите код счета, а я подскажу его определение...')
            bot.register_next_step_handler(msg, scheta)
        elif text == 'Справочник проводок':
            msg = bot.send_message(chat_id, 'Мы перешли Справочник проводок по счетам. Напишите номер интересующего счета, а я Вам покажу какие проводки по нему бывают...')
            bot.register_next_step_handler(msg, provodki)
        elif text in str(schet):
            # print('Найден')
            chat_id = message.chat.id
            text = message.text
            # print(text)
            f = open('Счета-описание.txt', encoding='utf-8', mode='r')
            fread = f.readlines()
            for line in fread:
                if text in line:
                    # print('Найден2')
                    final = line.replace(text + ';', '')
                    # print(final)
                    msg = bot.send_message(chat_id, final)
                    bot.register_next_step_handler(msg, scheta)
            f.close()
        elif text == 'start':
            msg = bot.send_message(chat_id, 'Начинаем заново.')
            send_welcome(message)
        else:
            if  text != 'Справочник проводок':
                msg = bot.send_message(chat_id, 'Такого счёта нет! Проверь правильность ввода и не дури мне голову!')
                bot.register_next_step_handler(msg, scheta)
    except Exception as e:
        msg = bot.send_message(chat_id, 'Печальная печалька. Хорошо бы сделать скрин, после чего вышла у вас эта ошибка и отправить админу для решения.')
        bot.register_next_step_handler(msg, scheta)


def provodki(message):
    chat_id = message.chat.id
    text = message.text
    try:
        if text == 'Справочник счетов':
            msg = bot.send_message(chat_id, 'Мы перешли в Справочник счетов. Вы можете написать код счета, а я подскажу его определение...')
            bot.register_next_step_handler(msg, scheta)
        elif message.text == 'Справочник проводок':
            msg = bot.send_message(chat_id, 'Пробуем заново. Напишите код счета, а я Вам какие проводки по нему бывают...')
            bot.register_next_step_handler(msg, provodki)
        elif text in str(provodka):
            chat_id = message.chat.id
            text = message.text
            f = open('Проводки.txt', encoding='utf-8', mode='r')
            fread = f.readlines()
            for line in fread:
                if text in line:
                    pre_final = line.replace(text + ';', '')
                    final = str(pre_final.replace(';', '\n'))
                    msg = bot.send_message(chat_id, final)
                    bot.register_next_step_handler(msg, provodki)
            f.close()
        elif text == 'start':
            msg = bot.send_message(chat_id, 'Начинаем заново.')
            send_welcome(message)
        else:
            if  text != 'Справочник проводок':
                msg = bot.send_message(chat_id, 'Пока я знаю только проводки счета 30211. Сорян')
                bot.register_next_step_handler(msg, provodki)

    except Exception as e:
        msg = bot.send_message(chat_id, 'Печальная печалька. Хорошо бы сделать скрин, после чего вышла у вас эта ошибка и отправить админу для решения.')
        bot.register_next_step_handler(msg, provodki)






bot.polling()