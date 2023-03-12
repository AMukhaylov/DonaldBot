import random
import config
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot(config.Token)


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

        #   Кнопка "Погода в Чолпан-Ате"
        elif message.text == '🇰🇬 Погода в Чолпан-Ате':
            r = requests.get('https://sinoptik.ua/погода-чолпон-ата')
            html = BS(r.content, 'html.parser')
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text
                bot.send_message(message.chat.id, "Погода на сегодня:\n" + t_min + ', ' + t_max + '.' + text)

        #   Кнопка "Погода в Перми"
        elif message.text == '🇷🇺 Погода в Перми':
            r = requests.get('https://sinoptik.ua/погода-пермь')
            html = BS(r.content, 'html.parser')
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text
                bot.send_message(message.chat.id, "Погода на сегодня:\n" + t_min + ', ' + t_max + '.' + text)

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
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            course_dollar = types.KeyboardButton('💵 Курс Доллара')
            course_som = types.KeyboardButton('💶 Курс Евро')
            course_euro = types.KeyboardButton('🇰🇬 Курс Сом')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(course_dollar, course_som, course_euro, back)
            bot.send_message(message.chat.id, 'Выбери вылюту:', reply_markup=markup)

        #   Кнопка "Курс Доллара"
        elif message.text == '💵 Курс Доллара':
            url = 'https://www.currency.me.uk/convert/usd/rub'
            r = requests.get(url)
            soup = BS(r.text, 'lxml')
            curs = soup.find("span", {"class": "mini ccyrate"}).text
            bot.send_message(message.chat.id, curs)

        #   Кнопка "Курс Евро"
        elif message.text == '💶 Курс Евро':
            url = 'https://www.currency.me.uk/convert/eur/rub'
            r = requests.get(url)
            soup = BS(r.text, 'lxml')
            curs = soup.find("span", {"class": "mini ccyrate"}).text
            bot.send_message(message.chat.id, curs)

        #   Кнопка "Курс Сом"
        elif message.text == '🇰🇬 Курс Сом':
            url = 'https://pokur.su/rub/kgs/1/'
            r = requests.get(url)
            soup = BS(r.text, 'lxml')
            curs = soup.find("div", {"class": "blockquote-classic"}).text
            bot.send_message(message.chat.id, curs)

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
