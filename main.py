import random
import telebot
from telebot import types
import requests

bot = telebot.TeleBot('6052300940:AAHn52m9GZSqg7qRm-FkYpIStJkWGv9VYlA')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name}!</b>"
    bot.send_message(message.chat.id, mess, parse_mode='html')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    weather_kgs = types.KeyboardButton('🇰🇬 Погода в Чолпан-Ате')
    weather_perm = types.KeyboardButton('🇷🇺 Погода в Перми')
    artur_work = types.KeyboardButton('❌ Что делает Артур?')
    course_currency = types.KeyboardButton('💲 Курсы валют')
    random_wow = types.KeyboardButton('🔸 Рандомное число')
    information = types.KeyboardButton('❗️ Информация')
    markup.add(weather_kgs, weather_perm, artur_work, course_currency, random_wow, information)

    bot.send_message(message.chat.id, 'Что хочешь узнать? Выбирай:', reply_markup=markup)


def get_dog():
    response = requests.get('https://dog.ceo/api/breeds/image/random').json()

    return response['message']


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🇰🇬 Погода в Чолпан-Ате':
            bot.send_message(message.chat.id, 'Я пока не умею такого!😢')

        elif message.text == '🇷🇺 Погода в Перми':
            bot.send_message(message.chat.id, 'Неее я пока только учусь и незнаю, как это передавать!🧐')

        elif message.text == '❌ Что делает Артур?':
            photo = open('../../Pictures/Мои изображения/ArthurWork.jpg', "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Да работает он, всё как обычно!🤪')

        elif message.text == '🔸 Рандомное число':
            bot.send_message(message.chat.id, 'Ваше число: ' + str(random.randint(0, 1000)))

        elif message.text == '💲 Курсы валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            course_dollar = types.KeyboardButton('💵 Курс Доллара')
            course_euro = types.KeyboardButton('💶 Курс Евро')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(course_dollar, course_euro, back)
            bot.send_message(message.chat.id, '💲 Курсы валют', reply_markup=markup)

        elif message.text == '❗️ Информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            course_dollar = types.KeyboardButton('🤖 О боте')
            course_euro = types.KeyboardButton('📦 Что в коробке?')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(course_dollar, course_euro, back)
            bot.send_message(message.chat.id, 'Что интересует?', reply_markup=markup)

        elif message.text == '🔙 Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            weather_kgs = types.KeyboardButton('🇰🇬 Погода в Чолпан-Ате')
            weather_perm = types.KeyboardButton('🇷🇺 Погода в Перми')
            artur_work = types.KeyboardButton('❌ Что делает Артур?')
            course_currency = types.KeyboardButton('💲 Курсы валют')
            random_wow = types.KeyboardButton('🔸 Рандомное число')
            information = types.KeyboardButton('❗️ Информация')

            markup.add(weather_kgs, weather_perm, artur_work, course_currency, random_wow, information)
            bot.send_message(message.chat.id, '🔙 Назад', reply_markup=markup)

        elif message.text == '🤖 О боте':
            bot.send_message(message.chat.id, f'Cоздан бот: 11.03.2023')
            bot.send_message(message.chat.id, f'Автор: Мухайлов А.Р.')

        elif message.text == '📦 Что в коробке?':
            bot.send_photo(message.chat.id, photo=get_dog())


bot.polling(none_stop=True)
