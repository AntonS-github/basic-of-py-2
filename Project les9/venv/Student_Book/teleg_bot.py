'''Через бот в телеге. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.'''
#TOKEN = '5672950538:AAF2JfwgehwOZLtfLxC4hjYWkGHnouPk3P8'

import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import json, csv
import logging
import add_student, del_student, search_student
import os
TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot('5672950538:AAF2JfwgehwOZLtfLxC4hjYWkGHnouPk3P8')
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

buttons = ['Добавить студента', 'Поиск', 'Удалить студента']


@bot.message_handler(commands=['start'])
def start_message(m):
    bot.reply_to(m, f"Добро пожаловать в телефонный справочник студентов, {m.from_user.first_name}")
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Добавить студента', callback_data='add'))
    markup.add(telebot.types.InlineKeyboardButton(text='Поиск', callback_data='search'))
    markup.add(telebot.types.InlineKeyboardButton(text='Удалить студента', callback_data='del'))
    bot.send_message(chat_id=m.chat.id, reply_markup=markup, text="Выберите команду в меню: ")

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global choice
    choice = call.data
    if choice == 'add':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Для внесения новой строки в справочник ведите через запятую ФИО, телефон, "
                                   "факультет, № группы стедента:")
    elif choice == 'search':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Введите запрос для поиска по справочнику:")
    elif choice == 'del':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Введите запрос для удаления из справочника:")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if choice == 'add':
        add_student.get_input(message.text)
        logger.info(f'Добавление нового студента {message.text}')
    elif choice == 'search':
        search_student.searching(message.text)
        bot.send_message(chat_id=message.chat.id, text=search_student.searching(message.text))
        logger.info(f'Осуществлялся поиск {message.text}')
    elif choice == 'del':
        bot.send_message(chat_id=message.chat.id, text=del_student.del_student(message.text))
        logger.info(f'Удаление студента {message.text}')

bot.polling()
