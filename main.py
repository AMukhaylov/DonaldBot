import random
import telebot
from telebot import types
import requests

bot = telebot.TeleBot('6052300940:AAHn52m9GZSqg7qRm-FkYpIStJkWGv9VYlA')


#   Приветсвенное сообщение и главное меню
@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name}!</b>"
    bot.send_message(message.chat.id, mess, parse_mode='html')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    weather = types.KeyboardButton('🌤 Погода')
    artur_work = types.KeyboardButton('❌ Что делает Артур?')
    course_currency = types.KeyboardButton('💲 Курсы валют')
    random_wow = types.KeyboardButton('🔸 Рандомное число')
    information = types.KeyboardButton('❗️ Информация')
    markup.add(weather, artur_work, course_currency, random_wow, information)

    bot.send_message(message.chat.id, "Что хочешь узнать? Выбирай:", reply_markup=markup)


#   API dog.ceo где мы берем случайное фото собаки из блока "Что в коробке?"
def get_dog():
    response = requests.get('https://dog.ceo/api/breeds/image/random').json()

    return response['message']


#   Кнопка "Погода"
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🌤 Погода':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            weather_kgs = types.KeyboardButton('🇰🇬 Погода в Чолпан-Ате')
            weather_perm = types.KeyboardButton('🇷🇺 Погода в Перми')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(weather_kgs, weather_perm, back)
            bot.send_message(message.chat.id, 'Выбери город:', reply_markup=markup)

        elif message.text == '🇰🇬 Погода в Чолпан-Ате':
            bot.send_message(message.chat.id, 'Я пока не умею такого!😢')

        elif message.text == '🇷🇺 Погода в Перми':
            bot.send_message(message.chat.id, 'Неее я пока только учусь и незнаю, как это передавать!🧐')

        #   Кнопка "Что делает Артур?"
        elif message.text == '❌ Что делает Артур?':
            photo = open('../../Pictures/Мои изображения/ArthurWork.jpg', "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Да работает он, всё как обычно!🤪')

        #   Кнопка "Рандомное число?"
        elif message.text == '🔸 Рандомное число':
            bot.send_message(message.chat.id, 'Ваше число: ' + str(random.randint(0, 1000)))

        #   Кнопка "Курсы валют"
        elif message.text == '💲 Курсы валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            course_dollar = types.KeyboardButton('💵 Курс Доллара')
            course_euro = types.KeyboardButton('💶 Курс Евро')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(course_dollar, course_euro, back)
            bot.send_message(message.chat.id, '💲 Курсы валют', reply_markup=markup)

        #   Кнопка "Информация"
        elif message.text == '❗️ Информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            course_dollar = types.KeyboardButton('🤖 О боте')
            course_euro = types.KeyboardButton('📦 Что в коробке?')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(course_dollar, course_euro, back)
            bot.send_message(message.chat.id, 'Что интересует?', reply_markup=markup)

        #   Кнопка "Назад"
        elif message.text == '🔙 Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            weather = types.KeyboardButton('🌤 Погода')
            artur_work = types.KeyboardButton('❌ Что делает Артур?')
            course_currency = types.KeyboardButton('💲 Курсы валют')
            random_wow = types.KeyboardButton('🔸 Рандомное число')
            information = types.KeyboardButton('❗️ Информация')

            markup.add(weather, artur_work, course_currency, random_wow, information)
            bot.send_message(message.chat.id, '🔙 Назад', reply_markup=markup)

        #   Кнопка "О боте"
        elif message.text == '🤖 О боте':
            bot.send_message(message.chat.id, f'Cоздан: 11.03.2023')
            bot.send_message(message.chat.id, f'Версия: 1.0')
            bot.send_message(message.chat.id, f'Автор: Мухайлов А.Р.')

        #   Кнопка "Что в коробке?"
        elif message.text == '📦 Что в коробке?':
            bot.send_photo(message.chat.id, photo=get_dog())


bot.polling(none_stop=True)
