from email import message
from pdb import Restart
import matplotlib.pyplot as plt
from colorama import init, Fore, Back, Style
import numpy as np
import pandas as pd
import paramID
import pic
import telebot
import time
from scipy import stats
from telebot import types
from tokenforbot import Token1

bot = telebot.TeleBot(Token1)


def out(text):
    print('\033[1m\033[32m{}'.format(text))
def red_error():
    print('\033[1m\033[31m{}'.format(''))




Old_EndDate = ' '
Old_StartDate = ' '
yr = 0
m = 0
d = 0
year = None
mounth = None
day = None
global restart
restart = False


@bot.message_handler(commands=['start', 'restart'])
def send_welcome(message):
    
    out(f'Отправлено сообщение:\n {message.text}\t от\t{message.from_user.username}')
    red_error()
    start = types.ReplyKeyboardMarkup(row_width=1)
    btn_start = 'Начать'
    start.add(btn_start)
    bot.send_message(message.from_user.id, 'Привет, если хочешь получить данные о погоде - нажимай на кнопки',
                     reply_markup=start)

    global Old_EndDate, Old_StartDate, yr, m, d, year, mounth, day, restart
    Old_EndDate = ' '
    Old_StartDate = ' '
    yr = 0
    m = 0
    d = 0
    year = None
    mounth = None
    day = None


@bot.message_handler(func=lambda message: True)
def other_text(message):
    global Old_EndDate, Old_StartDate, yr, m, d, year, mounth, day, restart
    year = None
    mounth = None
    day = None

    # print(f'Отправлено сообщение:\n {message.text}\t от\t{message.from_user.username},\n message id: {message.id}')
    out(f'Отправлено сообщение:\n {message.text}\t от\t{message.from_user.username},\n message id: {message.id}')
    red_error()
    
    # bot.send_message(message.from_user.id, 'Ожидайте прогноз')
    x = []
    y = []
    if message.text != '2021' or message.text != '2012' and year == None:
        year = types.ReplyKeyboardMarkup(row_width=2)
        button_y1 = types.KeyboardButton('2021')
        button_y2 = types.KeyboardButton('2022')
        year.add(button_y1, button_y2)

    if message.text not in ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
                            'Октябрь', 'Ноябрь', 'Декабрь']:
        mounth = types.ReplyKeyboardMarkup(row_width=3)
        button_m1 = 'Январь'
        button_m2 = 'Февраль'
        button_m3 = 'Март'
        button_m4 = 'Апрель'
        button_m5 = 'Май'
        button_m6 = 'Июнь'
        button_m7 = 'Июль'
        button_m8 = 'Август'
        button_m9 = 'Сентябрь'
        button_m10 = 'Октябрь'
        button_m11 = 'Ноябрь'
        button_m12 = 'Декабрь'

        mounth.add(button_m1, button_m2, button_m3, button_m4, button_m5, button_m6, button_m7, button_m8, button_m9,
                   button_m10, button_m11, button_m12)
    if message.text not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25',
                            '26', '27', '28', '29', '30', '31']:
        day = types.ReplyKeyboardMarkup(row_width=6)
        btn_d1 = "1"
        btn_d2 = "2"
        btn_d3 = "3"
        btn_d4 = "4"
        btn_d5 = "5"
        btn_d6 = "6"
        btn_d7 = "7"
        btn_d8 = "8"
        btn_d9 = "9"
        btn_d10 = "10"
        btn_d11 = "11"
        btn_d12 = "12"
        btn_d13 = "13"
        btn_d14 = "14"
        btn_d15 = "15"
        btn_d16 = "16"
        btn_d17 = "17"
        btn_d18 = "18"
        btn_d19 = "19"
        btn_d20 = "20"
        btn_d21 = "21"
        btn_d22 = "22"
        btn_d23 = "23"
        btn_d24 = "24"
        btn_d25 = "25"
        btn_d26 = "26"
        btn_d27 = "27"
        btn_d28 = "28"
        btn_d29 = "29"
        btn_d30 = "30"
        btn_d31 = "31"
        day.add(btn_d1, btn_d2, btn_d3, btn_d4, btn_d5, btn_d6, btn_d7, btn_d8, btn_d9, btn_d10, btn_d11, btn_d12,
                btn_d13, btn_d14, btn_d15, btn_d16, btn_d17, btn_d18,
                btn_d19, btn_d20, btn_d21, btn_d22, btn_d23, btn_d24, btn_d25, btn_d26, btn_d27, btn_d28, btn_d29,
                btn_d30, btn_d31)
    if message.text == '2022': yr = 2022
    if message.text == '2021': yr = 2021
    if message.text == "Январь": m = 1
    if message.text == "Февраль": m = 2
    if message.text == "Март": m = 3
    if message.text == "Апрель": m = 4
    if message.text == "Май": m = 5
    if message.text == "Июнь": m = 6
    if message.text == "Июль": m = 7
    if message.text == "Август": m = 8
    if message.text == "Сентябрь": m = 9
    if message.text == "Октябрь": m = 10
    if message.text == "Ноябрь": m = 11
    if message.text == "Декабрь": m = 12
    if message.text == "1": d = 1
    if message.text == "2": d = 2
    if message.text == "3": d = 3
    if message.text == "4": d = 4
    if message.text == "5": d = 5
    if message.text == "6": d = 6
    if message.text == "7": d = 7
    if message.text == "8": d = 8
    if message.text == "9": d = 9
    if message.text == "10": d = 10
    if message.text == "11": d = 11
    if message.text == "12": d = 12
    if message.text == "13": d = 13
    if message.text == "14": d = 14
    if message.text == "15": d = 15
    if message.text == "16": d = 16
    if message.text == "17": d = 17
    if message.text == "18": d = 18
    if message.text == "19": d = 19
    if message.text == "20": d = 20
    if message.text == "21": d = 21
    if message.text == "22": d = 22
    if message.text == "24": d = 24
    if message.text == "25": d = 25
    if message.text == "26": d = 26
    if message.text == "27": d = 27
    if message.text == "28": d = 28
    if message.text == "29": d = 29
    if message.text == "30": d = 30
    if message.text == "31": d = 31

    out(f'----------------- {message.text} ---------------')
    red_error()

    reply_markup = year

    if 0 < d < 32:
        pass
    elif (yr == 0 and m == 0 and d == 0) or (d != 0 and yr != 0 and m != 0):
        bot.send_message(message.from_user.id, 'Выберете год', reply_markup=year)
    elif yr != 0 and m == 0 and d == 0:
        bot.send_message(message.from_user.id, 'Выберете месяц', reply_markup=mounth)
    elif d == 0 and yr != 0 and m != 0:
        bot.send_message(message.from_user.id, 'Выберете день', reply_markup=day)

    if d != 0 and m != 0 and yr != 0:
        # Вроде должно работать))
        New_StartDate, New_EndDate = paramID.Param_For_ID(d, m, yr)
        if ((New_StartDate != Old_StartDate) or (
                New_EndDate != Old_EndDate)) and New_StartDate != ' ' and New_EndDate != ' ':
            # Пихаем сюда отбор и запускаем функцию для отрисовки
            Old_EndDate = New_EndDate
            Old_StartDate = New_StartDate

            df = pd.read_csv(
                'https://gist.githubusercontent.com/IKrakovskii/c0c5f85e68471a26348a9ac12dcde0e8/raw/47a8f51dc1cf966caafb03550196be3fa2a52e4b/df_hacaton.csv')

            new_df = list((df.air_temperature[(df.created_at >= New_StartDate) & (df.created_at < New_EndDate)]))

            y = np.array(list(new_df))
            x = np.array([i for i in range(len(y))])
            # print('\033[36m{}'.format('\n'), f'X - {list(x)}\nY-{list(y)}', sep='')
            # red_error()
            if pic.do_picture(x, y) == False:
                bot.send_message(message.from_user.id, 'Извините, нет данных за этот период\nПопробуйте ввести данные от 04.08.2021')
                again = types.ReplyKeyboardMarkup(row_width=1)
                btn_again = '/again'
                again.add(btn_again)
                bot.send_message(message.from_user.id, 'Перезапустить',
                     reply_markup=again)
            else:
                photo = open('F:\\hackaton\\pythonBot_2.0\\pictures\\picture.png', 'rb')
                time.sleep(5)
                bot.send_photo(message.from_user.id, photo)
                restart = True
                time.sleep(5)
                photo.close()
                again = types.ReplyKeyboardMarkup(row_width=1)
                btn_again = '/again'
                again.add(btn_again)
                bot.send_message(message.from_user.id, 'Перезапустить',
                        reply_markup=again)
            yr = 0
            m = 0
            d = 0
            Old_EndDate = ' '
            Old_StartDate = ' '
            New_EndDate = ' '
            New_StartDate = ' '


@bot.message_handler(commands=['again'])
def fagain(message):
    again = types.ReplyKeyboardMarkup(row_width=1)
    btn_again = 'Ввести данные снова'
    again.add(btn_again)
    bot.send_message(message.from_user.id, 'Нужно получить новые данные?',
            reply_markup=again)

bot.infinity_polling()