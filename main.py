import telebot as tb
from telebot import types
import os.path
import scrapper

"""Эта функция проверяет наличие файла с записью токена, если его нет, то создаёт таковой"""


def token_create_check():
    if os.path.isfile('access_token.TXT'):
        pass
    else:
        with open(file='access_token.TXT', mode='w+', encoding='utf-8') as tk:
            my_token = tk.write(str(input('Введите ваш токен или скопируйте : ')))


token_create_check()
access_token = open(file='access_token.TXT').read()
bot = tb.TeleBot(token=access_token)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,
                         'Привет могу выдать тебе подборку фильмов или сериалов для просмотра, что будешь смотреть?')
        bot.register_next_step_handler(message.from_user.id, get_question)


def get_question(message):
    keyboard = tb.types.InlineKeyboardMarkup()
    key_tv = tb.types.InlineKeyboardButton(text='Сериал', callback_data='tv')
    key_movie = tb.types.InlineKeyboardButton(text='Фильм', callback_data='m')
    keyboard.add(key_movie, key_tv)
    bot.send_message(message.from_user.id, text='', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'tv':
        bot.send_message(call.message.chat.id, scrapper.scrapper_func('t'))
    elif call.data == 'm':
        bot.send_message(call.message.chat.id, scrapper.scrapper_func('m'))


bot.infinity_polling()
