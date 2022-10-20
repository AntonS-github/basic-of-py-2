''' Работа через бот в телеграме. Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования'''

TOKEN = '5647781473:AAFdf4ho6NrMMVCpsk9VSDX6rMHK8vfu7UA'


import telebot
import re
import operations_calc as oc
import logging

bot = telebot.TeleBot(TOKEN)
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('someTestBot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, f"Добро пожаловать в калькулятор {message.from_user.first_name}")
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Сложение', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Вычитание', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Умножение', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Деление', callback_data=4))
    bot.send_message(message.chat.id, text="Выберите арифметическую операцию", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text=None)
    answer = ''
    if call.data == '1':
        answer = 'Вы выбрали сложение'
    elif call.data == '2':
        answer = 'Вы выбрали вычитание'
    elif call.data == '3':
        answer = 'Вы выбрали умножение'
    elif call.data == '4':
        answer = 'Вы выбрали деление'
    bot.send_message(call.message.chat.id, answer)

@bot.message_handler(content_types=['text'])
def calculator(message):
    global res
    numbers = re.split(r"[+|\-|*|/]", message.text)
    oper = [i for i in re.split(r"\d+", message.text) if i != '.' and i != '' and i != ' ']
    x = float(numbers[0])
    y = float(numbers[1])
    if oper[0] == '+':
        res = oc.summa(x, y)
    elif oper[0] == '-':
        res = oc.sub(x, y)
    elif oper[0] == '*':
        res = oc.mul(x, y)
    elif oper[0] == '/':
        res = oc.div(x, y)
    bot.send_message(message.chat.id, text=f'Результат вычислений {res}')
    logger.info(f'Calculation by User: {message.from_user.first_name}')

bot.infinity_polling()
