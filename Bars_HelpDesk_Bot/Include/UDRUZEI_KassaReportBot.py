import telebot
import os
import sys
import time

from telebot import apihelper
from telebot.types import Message
from telebot import types

TOKEN = '1048308590:AAHB-RxqKAlRl0iVaFl_udC8K0RM5_UOC_M'

apihelper.proxy = {'https': 'socks5://14611055481:U777Vluhz8@orbtl.s5.opennetwork.cc:999'}
bot = telebot.TeleBot(TOKEN)

# Пользователи

pin = ['0000;Газизов Дамир Абдулханович',
       '22293027;Марат',
       '1308;Ильдар',
       '1986;Хабибулина Анжела Игоревна',
       '5811;Газизова Алина Абдулхановна',
       '0901;Галяутдинова Радмила Гальфатовна',
       '9323;Васильева Вера Игоревна',
       '1301;Закирова Венера Ирсаловна',
       '1983;Цуканова Кристина Владимировна',
       '6654;Елена',
       '8942;Рахимзянова Регина Тагировна',
       '2509;Салимова Карина Эдуардовна',
       '0621;Исмаева Ландыш Робертовна',
       '4949;Ломоносова Наталья Юрьевна']

exit_chat = ['Отмена', "отмена", 'ОТМЕНА']
global market_name
market_name = ["РТС", "Ленина"]

@bot.message_handler(commands=['start'])
# Начало - Модуль приветсвия
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('РТС')
    btт2 = types.KeyboardButton('Ленина')
    markup.add(btn1, btт2)
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет. Я ответсвенный за формирование кассового отчета.'
                              '\nЧерез меня Вы сможете упрощенно сдать отчет по смене для руководителей.'
                              '\nДля начала я убежусь, что ты имеешь право на отправку отчета.')
    msg = bot.send_message(chat_id, 'Если хочешь начать, то выбери магазин для заполнения отчёта с помощью кнопок', reply_markup=markup)
    bot.register_next_step_handler(msg, market_choise)
    print(message)
# Конец - Модуль приветсвия

@bot.message_handler(content_types=['text'])

def market_choise(message):
    print('Модуль выбор магазина')
    chat_id = message.chat.id
    text_market = message.text
    global report_market
    try:
        if text_market in market_name and text_market not in exit_chat:
            msg = bot.send_message(chat_id, 'Введите пин-код пользователя\n(такой же как в кассовой программе)\n'
                                   'Если ты хочешь закончить не отправляя отчет, просто напиши слово - '
                                   'отмена')
            bot.register_next_step_handler(msg, users)
            report_market = text_market
        if text_market in exit_chat:
            msg = bot.send_message(chat_id,'Забываю все, что между нами было, сжигаю мосты и города. Начнём с нового листа....\nЕсли нужно запустить отчёт заново просто выбери магазин с помощью кнопок')
            bot.register_next_step_handler(msg, send_welcome)
        pass
    except Exception as e:
        msg = bot.send_message(chat_id,'Выберите строго из предложенных вариантов!')
        bot.register_next_step_handler(msg, market_choise)
# Конец - Модуль авторизации


# Начало - Модуль приветсвия пользователя
def users(message):
    global report_user
    print('Модуль проверки пинкода')
    chat_id = message.chat.id
    text_pin_to_username = message.text
    print(len(text_pin_to_username))
    if text_pin_to_username not in str(pin) and text_pin_to_username not in exit_chat or len(text_pin_to_username) < 4:
        msg = bot.send_message(chat_id,
                               'Такой пин-код не найден! Попробуйте еще раз!'
                               '\nПри нескольких неверных попытках я Вас '
                               'заблокирую!')
        bot.register_next_step_handler(msg, users)
    elif text_pin_to_username in str(pin) and len(text_pin_to_username) >= 4 and text_pin_to_username not in exit_chat:
        for line in pin:
            if text_pin_to_username in line:
                user_name = line.replace(text_pin_to_username + ';', '')
                bot.send_message(chat_id, 'Здравствуйте, ' + user_name + '!')
                msg = bot.send_message(chat_id, 'Укажите дату рабочей смены, в формате: '
                                                '\nдд.мм.гггг:')
                bot.register_next_step_handler(msg, data)
                report_user = user_name
    elif text_pin_to_username in exit_chat:
        msg = bot.send_message(chat_id, 'Забываю все, что между нами было, сжигаю мосты и города. Начнём с нового листа....\nЕсли нужно запустить отчёт заново просто выбери магазин с помощью кнопок')
        bot.register_next_step_handler(msg, send_welcome)

# Конец - Модуль приветсвия пользователя


# Начало - Модуль даты отчета
def data(message):
    print('Модуль указания даты')
    chat_id = message.chat.id
    text_date = message.text

    date_days = range(1, 31)
    date_mounts = range(1, 12)
    date_years = range(2020, 2030)
    global format_days, format_mounth, format_years, report_date

    if text_date == "0":
        text_date = "02.02.2020"

    if len(text_date) != 10 and text_date not in exit_chat:
        msg = bot.send_message(chat_id, 'Ваш ответ содержит недопустимые символы. Формат ответа должен быть'
                                        ': \nДД.ММ.ГГГГ')
        bot.register_next_step_handler(msg, data)
    elif len(text_date) == 10 and text_date not in exit_chat:
        text_to_str_list = list(text_date)
        for i in [2, 5]:
            text_to_str_list[i] = '.'
            text_date = ''.join(text_to_str_list)
        if int(text_date[0:2]) in date_days and int(text_date[3:5]) in date_mounts and int(
                text_date[6:10]) in date_years and text_date not in exit_chat:
            text_split = text_date.split('.')
            if text_split[0].isdigit() and text_split[1].isdigit() and text_split[
                2].isdigit() and text_date not in exit_chat:
                msg = bot.send_message(chat_id, 'Укажите сумму НАЛИЧНЫХ на НАЧАЛО смены:')
                bot.register_next_step_handler(msg, func_summa_na_nachalo)
                global report_date
                report_date = text_date
    elif text_date in exit_chat:
        msg = bot.send_message(chat_id,
                               'Забываю все, что между нами было, сжигаю мосты и города. Начнём с нового листа....\nЕсли нужно запустить отчёт заново просто выбери магазин с помощью кнопок')
        bot.register_next_step_handler(msg, send_welcome)
    else:
        msg = bot.send_message(chat_id, 'Ваш ответ содержит недопустимые символы. Формат ответа должен быть'
                                        ': \nДД.ММ.ГГГГ')
        bot.register_next_step_handler(msg, data)

    try:
        print('Ответственный кассовой смены: \n' + str(report_user) +
              '\nДата отчета: ' + str(report_date))
    except Exception as e:
        pass
# Конец - Модуль даты отчета


# Начало - Сумма на начало дня
def func_summa_na_nachalo(message):
    print('Модуль ввода суммы на начало')
    global report_summa_na_nachalo
    chat_id = message.chat.id
    text_summa_na_nachalo = message.text
    text_summa_na_nachalo = text_summa_na_nachalo.replace(',', '.')
    try:
        if type(text_summa_na_nachalo) == str and text_summa_na_nachalo not in exit_chat:
            text_summa_na_nachalo = float(text_summa_na_nachalo)
    except ValueError:
        print('Ошибка преобразования в float')
        msg = bot.send_message(chat_id,
                               'Модуль денег "на начало дня". \n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_na_nachalo)
        pass
    try:
        if type(text_summa_na_nachalo) == int and text_summa_na_nachalo not in exit_chat:
            text_summa_na_nachalo == float(text_summa_na_nachalo)
            msg = bot.send_message(chat_id, 'Введите СУММУ ПРОДАЖ НАЛИЧНЫМИ (данные компьютера):')
            bot.register_next_step_handler(msg, func_summa_prodaj_nalichnie_kassa)
            report_summa_na_nachalo = text_summa_na_nachalo
            pass
        elif type(text_summa_na_nachalo) == float and text_summa_na_nachalo not in exit_chat:
            text_summa_na_nachalo = float(text_summa_na_nachalo)
            msg = bot.send_message(chat_id, 'Введите СУММУ ПРОДАЖ НАЛИЧНЫМИ (данные компьютера):')
            bot.register_next_step_handler(msg, func_summa_prodaj_nalichnie_kassa)
            report_summa_na_nachalo = text_summa_na_nachalo
            pass
        elif text_summa_na_nachalo in exit_chat:
            msg = bot.send_message(chat_id,
                                   'Забываю все, что между нами было, сжигаю мосты и города. Начнём с нового листа....\nЕсли нужно запустить отчёт заново просто выбери магазин с помощью кнопок')
            bot.register_next_step_handler(msg, send_welcome)

    except Exception as e:
        msg = bot.send_message(chat_id,
                               'Модуль денег "на начало дня". \n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_na_nachalo)

    try:
        print('Ответсвтвенный за кассу: ' + str(report_user) +
              '\nДата отчета: ' + str(report_date) +
              '\nНаличные на начало: ' + str(report_summa_na_nachalo))
    except Exception as e:
        pass
# Конец - Сумма на конец дня


# Начало - Модуль наличные по данным кассы
def func_summa_prodaj_nalichnie_kassa(message):
    print('Модуль суммы продаж наличными')
    global report_summa_prodaji_nalichnie_kassa
    chat_id = message.chat.id
    text_summa_nalichnimi_kassa = message.text
    text1 = text_summa_nalichnimi_kassa.replace(',', '.')
    try:
        if type(text1) == str:
            text1 = float(text1)
    except ValueError:
        print('Ошибка преобразования в float')
        msg = bot.send_message(chat_id,
                               'Модуль "Наличные" по данным КАССЫ. \n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_prodaj_nalichnie_kassa)
        pass

    try:
        if type(text1) == int and text1 not in exit_chat:
            text1 == float(text1)
            msg = bot.send_message(chat_id, 'Введите СУММУ ПРОДАЖ БЕЗНАЛИЧНЫМИ (данные компьютера):')
            bot.register_next_step_handler(msg, func_summa_beznalichnie_kassa)
            report_summa_prodaji_nalichnie_kassa = text1
            pass
        elif type(text1) == float and text1 not in exit_chat:
            text1 = float(text1)
            msg = bot.send_message(chat_id, 'Введите СУММУ ПРОДАЖ БЕЗНАЛИЧНЫМИ (данные компьютера):')
            bot.register_next_step_handler(msg, func_summa_beznalichnie_kassa)
            report_summa_prodaji_nalichnie_kassa = text1
            pass
        elif text_summa_nalichnimi_kassa in exit_chat:
            msg = bot.send_message(chat_id,
                                   'Забываю все, что между нами было, сжигаю мосты и города. Начнём с нового листа....\nЕсли нужно запустить отчёт заново просто выбери магазин с помощью кнопок')
            bot.register_next_step_handler(msg, send_welcome)

    except Exception as e:
        msg = bot.send_message(chat_id,
                               'Модуль "Наличные" по данным кассы.\n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_prodaj_nalichnie_kassa)

    try:
        print('Ответсвтвенный за кассу: ' + str(report_user) +
              '\nДата отчета: ' + str(report_date) +
              '\nНаличные на начало: ' + str(report_summa_na_nachalo) +
              '\nCумма наличными (по данным кассы): ' + str(report_summa_prodaji_nalichnie_kassa) + ' руб.')
    except Exception as e:
        pass
# Конец - Модуль наличные по данным кассы


# Начало - Модуль безналичные по данным кассы
def func_summa_beznalichnie_kassa(message):
    print('Модуль продажи безнал-касса')
    chat_id = message.chat.id
    text_summa_beznalichnie_kassa = message.text.replace(',', '.')
    global report_summa_beznalichnie_kassa

    try:
        if type(text_summa_beznalichnie_kassa) == str:
            text_summa_beznalichnie_kassa = float(text_summa_beznalichnie_kassa)
    except ValueError:
        print('Ошибка преобразования в float')
        msg = bot.send_message(chat_id,
                               'Модуль "Безналичные"  по данным КАССЫ.\n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_beznalichnie_kassa)
        pass

    try:
        if type(text_summa_beznalichnie_kassa) == int and text_summa_beznalichnie_kassa not in exit_chat:
            text_summa_beznalichnie_kassa = float(text_summa_beznalichnie_kassa)
            msg = bot.send_message(chat_id, 'Введите СУММУ ПРОДАЖ БЕЗНАЛИЧНЫМИ (данные терминала):')
            bot.register_next_step_handler(msg, func_summa_beznalichnie_pinpad)
            report_summa_beznalichnie_kassa = text_summa_beznalichnie_kassa
            pass
        elif type(text_summa_beznalichnie_kassa) == float and text_summa_beznalichnie_kassa not in exit_chat:
            text_summa_beznalichnie_kassa = float(text_summa_beznalichnie_kassa)
            msg = bot.send_message(chat_id, 'Введите СУММУ ПРОДАЖ БЕЗНАЛИЧНЫМИ (данные терминала):')
            bot.register_next_step_handler(msg, func_summa_beznalichnie_pinpad)
            report_summa_beznalichnie_kassa = text_summa_beznalichnie_kassa
            pass
        elif text_summa_beznalichnie_kassa in exit_chat:
            msg = bot.send_message(chat_id,
                                   'Забываю все, что между нами было, сжигаю мосты и города. Начнём с нового листа....\nЕсли нужно запустить отчёт заново просто выбери магазин с помощью кнопок')
            bot.register_next_step_handler(msg, send_welcome)
            pass
    except Exception as e:
        msg = bot.send_message(chat_id,
                               'Модуль "Безналичные"  по данным КАССЫ.\n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_beznalichnie_kassa)

    try:
        print('Ответсвтвенный за кассу: ' + str(report_user) +
              '\nДата отчета: ' + str(report_date) +
              '\nНаличные на начало: ' + str(report_summa_na_nachalo) +
              '\nCумма наличными (по данным кассы): ' + str(report_summa_prodaji_nalichnie_kassa) + ' руб.'
              '\nCумма безналичными (по данным кассы): ' + str(report_summa_beznalichnie_kassa) + ' руб.')
    except Exception as e:
        pass
# Конец - Модуль безналичные по данным кассы

# Начало - Модуль безналичные по данным ПИНПАДА
def func_summa_beznalichnie_pinpad(message):
    print('Модуль продажи безнал-терминал')
    chat_id = message.chat.id
    text_summa_beznalichnie_pinpad = message.text.replace(',', '.')


    global report_summa_beznalichnie_pinpad

    try:
        text_summa_beznalichnie_pinpad = float(text_summa_beznalichnie_pinpad)
    except ValueError:
        print('Ошибка преобразования в float')
        msg = bot.send_message(chat_id,
                               '111Модуль "Безналичные"  по данным ПИНПАДА.\n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_beznalichnie_pinpad)
        pass

    try:
        if float(text_summa_beznalichnie_pinpad) > float(report_summa_beznalichnie_kassa) and text_summa_beznalichnie_pinpad not in exit_chat:
            raznica_summ_pinpad = float(text_summa_beznalichnie_pinpad) - float(report_summa_beznalichnie_kassa)
            bot.send_message(chat_id,'Cумма безналичных по данным ТЕРМИНАЛА больше, чем по данным КОМПЬЮТЕРА!')
            bot.send_message(chat_id,'ИЗЛИШЕК: ' + str(round(raznica_summ_pinpad,2)) +' руб.')
            bot.send_message(chat_id,'Это недопустимо! Требуется объяснительная!')
            msg = bot.send_message(chat_id, 'Введите СУММУ ИЗЪЯТИЯ  (если не было, укажите 0:')
            bot.register_next_step_handler(msg, func_summa_izyatiya)
            report_summa_beznalichnie_pinpad = text_summa_beznalichnie_pinpad
            pass
        elif float(text_summa_beznalichnie_pinpad) < float(report_summa_beznalichnie_kassa) and text_summa_beznalichnie_pinpad not in exit_chat:
            raznica_summ_pinpad = float(report_summa_beznalichnie_kassa) - float(text_summa_beznalichnie_pinpad)
            bot.send_message(chat_id,'Cумма безналичных по данным ТЕРМИНАЛА меньше, чем по данным КОМПЬЮТЕРА!')
            bot.send_message(chat_id,'НЕДОСТАЧА: ' + str(round(raznica_summ_pinpad,2)) +' руб.')
            bot.send_message(chat_id,'Это недопустимо! Требуется объяснительная!')
            msg = bot.send_message(chat_id, 'Введите СУММУ ИЗЪЯТИЯ  (если не было, укажите 0:')
            bot.register_next_step_handler(msg, func_summa_izyatiya)
            report_summa_beznalichnie_pinpad = text_summa_beznalichnie_pinpad
            pass
        elif float(text_summa_beznalichnie_pinpad) == float(report_summa_beznalichnie_kassa) and text_summa_beznalichnie_pinpad not in exit_chat:
            bot.send_message(chat_id, 'Отлично! Cумма безналичных по данным ТЕРМИНАЛА совпадает с данными КОМПЬЮТЕРА!')
            msg = bot.send_message(chat_id, 'Введите СУММУ ИЗЪЯТИЯ  (если не было, укажите 0:')
            bot.register_next_step_handler(msg, func_summa_izyatiya)
            report_summa_beznalichnie_pinpad = text_summa_beznalichnie_pinpad
            pass

        elif text_summa_beznalichnie_pinpad in exit_chat:
            msg = bot.send_message(chat_id,
                                   'Забываю все, что между нами было, сжигаю мосты и города. Начнём с нового листа....\nЕсли нужно запустить отчёт заново просто выбери магазин с помощью кнопок')
            bot.register_next_step_handler(msg, send_welcome)

    except Exception as e:
        msg = bot.send_message(chat_id,
                               '222Модуль "Безналичные"  по данным ПИНПАДА.\n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_beznalichnie_pinpad)

    try:
        print('Ответсвтвенный за кассу: ' + str(report_user) +
              '\nДата отчета: ' + str(report_date) +
              '\nНаличные на начало: ' + str(report_summa_na_nachalo) +
              '\nCумма наличными (по данным кассы): ' + str(report_summa_prodaji_nalichnie_kassa) + ' руб.'
              '\nCумма безналичными (по данным кассы): ' + str(report_summa_beznalichnie_kassa) + ' руб.'
              '\nCумма безналичным (по данным ПИНПАДА): ' + str(report_summa_beznalichnie_pinpad) + ' руб.')
    except Exception as e:
        pass
# Конец - Модуль безналичные по данным ПИНПАДА

# Начало - Модуль изъятия денежных средств
def func_summa_izyatiya(message):
    print('Модуль изъятий')
    chat_id = message.chat.id
    text_summa_izyatiya = message.text.replace(',', '.')
    global report_izyatiya

    try:
        if type(text_summa_izyatiya) == str or type(text_summa_izyatiya) == float or type(text_summa_izyatiya) == int:
            text_summa_izyatiya = float(text_summa_izyatiya)
    except ValueError:
        print('Ошибка преобразования в float')
        msg = bot.send_message(chat_id,
                               'Модуль "Изъятия из кассы". \n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_izyatiya)
        pass

    try:
        if type(text_summa_izyatiya) == int or type(text_summa_izyatiya) == float and text_summa_izyatiya not in exit_chat:
            text_summa_izyatiya == float(text_summa_izyatiya)
            msg = bot.send_message(chat_id, 'Введите сумму ВНЕСЕНИЙ:')
            bot.register_next_step_handler(msg, func_summa_vnesenie)
            report_izyatiya = text_summa_izyatiya
            pass
        elif text_summa_izyatiya in exit_chat:
            msg = bot.send_message(chat_id,
                                   'Забываю все, что между нами было, сжигаю мосты и города. Начнём с нового листа....\nЕсли нужно запустить отчёт заново просто выбери магазин с помощью кнопок')
            bot.register_next_step_handler(msg, send_welcome)

    except Exception as e:
        msg = bot.send_message(chat_id,
                               'Модуль "Изъятия из кассы". \n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_izyatiya)

    try:
        print('Ответсвтвенный за кассу: ' + str(report_user) +
              '\nДата отчета: ' + str(report_date) +
              '\nНаличные на начало: ' + str(report_summa_na_nachalo) +
              '\nCумма наличными (по данным кассы): ' + str(report_summa_prodaji_nalichnie_kassa) + ' руб.'
              '\nCумма безналичными (по данным кассы): ' + str(report_summa_beznalichnie_kassa) + ' руб.'
              '\nCумма безналичным (по данным ПИНПАДА): ' + str(report_summa_beznalichnie_pinpad) + ' руб.'
              '\nCумма изъятия из кассы: ' + str(report_izyatiya) + ' руб.')
    except Exception as e:
        pass
# Конец - Модуль изъятия денежных средств

def func_summa_vnesenie(message):
    print('Модуль внесений')
    chat_id = message.chat.id
    text_summa_vneseniya = message.text.replace(',', '.')
    global report_vneseniya

    try:
        if type(text_summa_vneseniya) == str:
            text_summa_vneseniya = float(text_summa_vneseniya)
    except ValueError:
        print('Ошибка преобразования в float')
        msg = bot.send_message(chat_id,
                               'Модуль "Изъятия из кассы". \n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_vnesenie)
        pass

    try:
        if type(text_summa_vneseniya) == int or type(text_summa_vneseniya) == float and text_summa_vneseniya not in exit_chat:
            text_summa_vneseniya == float(text_summa_vneseniya)
            msg = bot.send_message(chat_id, 'Посчитайте и укажите количество ВСЕХ НАЛИЧНЫХ ДЕНЕГ в кассе: ')
            bot.register_next_step_handler(msg, func_summa_nalichnie_kassa_fact)
            report_vneseniya = text_summa_vneseniya
            pass
        elif text_summa_vneseniya in exit_chat:
            msg = bot.send_message(chat_id,
                                   'Забываю все, что между нами было, сжигаю мосты и города. Начнём с нового листа....\nЕсли нужно запустить отчёт заново просто выбери магазин с помощью кнопок')
            bot.register_next_step_handler(msg, send_welcome)

    except Exception as e:
        msg = bot.send_message(chat_id,
                               'Модуль "Внесения в кассу". \n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_vnesenie)

    try:
        print('Ответсвтвенный за кассу: ' + str(report_user) +
              '\nДата отчета: ' + str(report_date) +
              '\nНаличные на начало: ' + str(report_summa_na_nachalo) +
              '\nCумма наличными (по данным кассы): ' + str(report_summa_prodaji_nalichnie_kassa) + ' руб.'
              '\nCумма безналичными (по данным кассы): ' + str(report_summa_beznalichnie_kassa) + ' руб.'
              '\nCумма безналичным (по данным ПИНПАДА): ' + str(report_summa_beznalichnie_pinpad) + ' руб.'
              '\nCумма изъятия из кассы: ' + str(report_izyatiya) + ' руб.'
              '\nCумма внесения в кассу: ' + str(report_vneseniya) + ' руб.')
    except Exception as e:
        pass

# Начало - Модуль наличные фактически в кассе
def func_summa_nalichnie_kassa_fact(message):
    print('Модуль фактических денег в кассе')
    chat_id = message.chat.id
    text_summa_nalichnimi_fact = message.text.replace(',', '.')
    global report_summa_nalichnie_fact
    global summa_itog
    summa_itog = float(report_summa_na_nachalo) + float (report_vneseniya) + float(report_summa_prodaji_nalichnie_kassa) - float(report_izyatiya)

    try:
        if type(text_summa_nalichnimi_fact) == str or type(text_summa_nalichnimi_fact) == int:
            text_summa_nalichnimi_fact = float(text_summa_nalichnimi_fact)
    except ValueError:
        print('Ошибка преобразования в float')
        msg = bot.send_message(chat_id,
                               '111Модуль "Наличные" фактически в кассе. \n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_prodaj_nalichnie_kassa)
        pass
    print(type(text_summa_nalichnimi_fact))
    try:
        if type(text_summa_nalichnimi_fact) == int or type(text_summa_nalichnimi_fact) == float and text_summa_nalichnimi_fact not in exit_chat:
            if float(text_summa_nalichnimi_fact) > float(summa_itog):
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
                btn1 = types.KeyboardButton('Завершить')
                markup.add(btn1)
                raznica_nalkass_nalfact = float(text_summa_nalichnimi_fact) - float(report_summa_na_nachalo) - float (report_vneseniya) + float(report_summa_prodaji_nalichnie_kassa) - float(report_izyatiya)
                bot.send_message(chat_id,'Сумма НАЛИЧНЫХ в денежном ящике БОЛЬШЕ, чем должно быть по данным компьютера!')
                bot.send_message(chat_id,'ИЗЛИШКИ: ' + str(round(raznica_nalkass_nalfact,2)) + ' руб.')
                msg = bot.send_message(chat_id,'Это недопустимо! (возможно Вы не отразили продажу или внесение денежных средств)',reply_markup=markup)
                bot.register_next_step_handler(msg, func_final_report)
                report_summa_nalichnie_fact = text_summa_nalichnimi_fact
                pass
            if float(text_summa_nalichnimi_fact) < float(summa_itog):
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
                btn1 = types.KeyboardButton('Завершить')
                markup.add(btn1)
                raznica_nalkass_nalfact = float(report_summa_na_nachalo) + float(report_vneseniya) + float(report_summa_prodaji_nalichnie_kassa) - float(report_izyatiya) - float(text_summa_nalichnimi_fact)
                bot.send_message(chat_id,'Сумма НАЛИЧНЫХ в денежном ящике МЕНЬШЕ, чем должно быть по данным компьютера!')
                bot.send_message(chat_id,'НЕДОСТАЧА: ' + str(round(raznica_nalkass_nalfact,2)) + ' руб.')
                msg = bot.send_message(chat_id, 'Это недопустимо! (возможно Вы не отразили изъятие денежных средств).',reply_markup=markup)
                bot.register_next_step_handler(msg, func_final_report)
                report_summa_nalichnie_fact = text_summa_nalichnimi_fact
                pass
            if float(text_summa_nalichnimi_fact) == float(summa_itog):
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
                btn1 = types.KeyboardButton('Завершить')
                markup.add(btn1)
                msg = bot.send_message(chat_id, 'Суммы полностью совпадают. Вы молодец :)' ,reply_markup=markup)
                bot.register_next_step_handler(msg, func_final_report)
                report_summa_nalichnie_fact = text_summa_nalichnimi_fact

                pass
        elif text_summa_nalichnimi_fact in exit_chat:
            msg = bot.send_message(chat_id,
                                   'Забываю все, что между нами было, сжигаю мосты и города. Начнём с нового листа....\nЕсли нужно запустить отчёт заново просто выбери магазин с помощью кнопок')
            bot.register_next_step_handler(msg, send_welcome)

    except Exception as e:
        msg = bot.send_message(chat_id,
                               'Модуль "Наличные" фактически в кассе. \n'
                               'Проверьте верность вводимых символов. Похоже, что у вас вместо цифр - и текст и цифры.\n'
                               'Пример заполнения для целого и дробного числа: 100 или 100.50')
        bot.register_next_step_handler(msg, func_summa_nalichnie_kassa_fact)

    try:
        print('Ответсвтвенный за кассу: ' + str(report_user) +
              '\nДата отчета: ' + str(report_date) +
              '\nНаличные на начало: ' + str(report_summa_na_nachalo) +
              '\nCумма наличными (по данным кассы): ' + str(report_summa_prodaji_nalichnie_kassa) + ' руб.'
              '\nCумма безналичными (по данным кассы): ' + str(report_summa_beznalichnie_kassa) + ' руб.'
              '\nCумма безналичным (по данным ПИНПАДА): ' + str(report_summa_beznalichnie_pinpad) + ' руб.'
              '\nCумма изъятия из кассы: ' + str(report_izyatiya) + ' руб.'
              '\nCумма внесения в кассу: ' + str(report_vneseniya) + ' руб.'
              '\nСумма налиными (фактически): ' + str(report_summa_nalichnie_fact) + ' руб.')
    except Exception as e:
        pass
# Конец - Модуль наличные фактически в кассе

def func_final_report(message):
    print('Модуль финального отчета')
    chat_id = message.chat.id
    text = message.text
    raznica = float(summa_itog) - float(report_summa_nalichnie_fact)
    bot.send_message(chat_id,
              report_market +
              '\n•••••••••••••••••••••••••••••'
              '\nОтветственный смены: \n' + str(report_user) +
              '\n•••••••••••••••••••••••••••••'
              '\nДата смены: ' + str(report_date) +
              '\n•••••••••••••••••••••••••••••'
              '\nСумма наличных на начало: ' + str(report_summa_na_nachalo) + ' руб.'
              '\n•••••••••••••••••••••••••••••'
              '\nCумма продаж наличными (по данным кассы): ' + str(report_summa_prodaji_nalichnie_kassa) +' руб.'
              '\n•••••••••••••••••••••••••••••'
              '\nCумма безналичных продаж (касса): ' + str(report_summa_beznalichnie_kassa) + ' руб.'
              '\nCумма безналичных продаж (терминал): ' + str(report_summa_beznalichnie_pinpad) + ' руб.'
              '\n•••••••••••••••••••••••••••••'
              '\nCумма внесений в кассу: ' + str(report_vneseniya) + ' руб.'
              '\nCумма изъятий из кассы: ' + str(report_izyatiya) + ' руб.'
              '\n•••••••••••••••••••••••••••••'
              '\nИтого наличных на конец (по факту): ' + str(report_summa_nalichnie_fact) + ' руб.'
              '\n•••••••••••••••••••••••••••••'
              '\n\nОжидалось наличных на конец смены: ' + str(summa_itog) + ' руб.')

    boss_id = 119822851
    bot.send_message(boss_id,
              report_market +
              '\n•••••••••••••••••••••••••••••'
              '\nОтветственный смены: \n' + str(report_user) +
              '\n•••••••••••••••••••••••••••••'
              '\nДата смены: ' + str(report_date) +
              '\n•••••••••••••••••••••••••••••'
              '\nСумма наличных на начало: ' + str(report_summa_na_nachalo) + ' руб.'
              '\n•••••••••••••••••••••••••••••'
              '\nCумма продаж наличными (по данным кассы): ' + str(report_summa_prodaji_nalichnie_kassa) +' руб.'
              '\n•••••••••••••••••••••••••••••'
              '\nCумма безналичных продаж (касса): ' + str(report_summa_beznalichnie_kassa) + ' руб.'
              '\nCумма безналичных продаж (терминал): ' + str(report_summa_beznalichnie_pinpad) + ' руб.'
              '\n•••••••••••••••••••••••••••••'
              '\nCумма внесений в кассу: ' + str(report_vneseniya) + ' руб.'
              '\nCумма изъятий из кассы: ' + str(report_izyatiya) + ' руб.'
              '\n•••••••••••••••••••••••••••••'
              '\nИтого наличных на конец (по факту): ' + str(report_summa_nalichnie_fact) + ' руб.'
              '\n•••••••••••••••••••••••••••••'
              '\n\nОжидалось наличных на конец смены: ' + str(summa_itog) + ' руб.')

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('РТС')
    btт2 = types.KeyboardButton('Ленина')
    markup.add(btn1, btт2)
    msg = bot.send_message(chat_id, 'ТЕСТ ОКОНЧЕН', reply_markup=markup)



    if text in exit_chat:
        msg = bot.send_message(chat_id,
                               'Забываю все, что между нами было, сжигаю мосты и города. Начнём с нового листа....\nЕсли нужно запустить отчёт заново просто выбери магазин с помощью кнопок')
        bot.register_next_step_handler(msg, send_welcome)


bot.polling()
