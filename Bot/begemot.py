import telebot
from config import TOKEN
import random

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('Угадай число')
    item2 = telebot.types.KeyboardButton('Кинь кость')
    item3 = telebot.types.KeyboardButton('Знак зодиака')
    item4 = telebot.types.KeyboardButton('Анекдот наугад')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Добро пожаловать. Выбери действие', reply_markup=markup)




@bot.message_handler(content_types=['text'])

def send_mess(message):
    if message.text == 'Угадай число':
        bot.send_message(message.chat.id, 'Напиши число от 1 до 10')
        bot.register_next_step_handler(message, guess_number)
    elif message.text == 'Кинь кость':
        n = random.randint(1,6)
        bot.send_message(message.chat.id, 'Твой результат: ' + str(n))
    elif message.text == 'Знак зодиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=4)
        but1 = telebot.types.InlineKeyboardButton('Овен', callback_data='Овен')
        but2 = telebot.types.InlineKeyboardButton('Телец', callback_data='Телец')
        but3 = telebot.types.InlineKeyboardButton('Близнец', callback_data='Близнец')
        but4 = telebot.types.InlineKeyboardButton('Рак', callback_data='Рак')
        but5 = telebot.types.InlineKeyboardButton('Лев', callback_data='Лев')
        but6 = telebot.types.InlineKeyboardButton('Дева', callback_data='Дева')
        but7 = telebot.types.InlineKeyboardButton('Весы', callback_data='Весы')
        but8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='Скорпион')
        but9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='Стрелец')
        but10 = telebot.types.InlineKeyboardButton('Козерог', callback_data='Козерог')
        but11 = telebot.types.InlineKeyboardButton('Водолей', callback_data='Водолей')
        but12 = telebot.types.InlineKeyboardButton('Рыба', callback_data='Рыба')
        markup.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10, but11, but12)

        bot.send_message(message.chat.id, 'Выберите знак зодиака', reply_markup=markup)
    elif message.text == 'Анекдот наугад':
        bot.send_message(message.chat.id, 'Вот анекдот: ')
        random_joke(message)
    else:
        bot.send_message(message.chat.id, 'Выбери кнопку!')

def randomiti():
    m = random.randint(1,10)
    return m

def guess_number(message):
    m = str(randomiti())
    n = message.text
    if n == m:
        bot.send_message(message.chat.id, 'Угадал')
    else:
        bot.send_message(message.chat.id, 'Попробуй ещё раз.')





def random_joke(m):
    with open('anegdot.txt', 'r') as data:
        somelist = list(data.readlines())
        some_el = somelist[random.randint(0, len(somelist)-1)]
        some_el = some_el.rstrip('\n')
        bot.send_message(m.chat.id, f'Вот: \n {some_el}')

@bot.callback_query_handler(func=lambda call: True)

def callback_inline(call):
    if call.data == 'Овен':
        sign = search_sign(call.data)
        bot.send_message(call.message.chat.id, sign)
    elif call.data == 'Телец':
        sign = search_sign(call.data)
        bot.send_message(call.message.chat.id, sign)
    elif call.data == 'Близнец':
        sign = search_sign(call.data)
        bot.send_message(call.message.chat.id, sign)
    elif call.data == 'Рак':
        sign = search_sign(call.data)
        bot.send_message(call.message.chat.id, sign)
    elif call.data == 'Лев':
        sign = search_sign(call.data)
        bot.send_message(call.message.chat.id, sign)
    elif call.data == 'Дева':
        sign = search_sign(call.data)
        bot.send_message(call.message.chat.id, sign)
    elif call.data == 'Весы':
        sign = search_sign(call.data)
        bot.send_message(call.message.chat.id, sign)
    elif call.data == 'Скорпион':
        sign = search_sign(call.data)
        bot.send_message(call.message.chat.id, sign)
    elif call.data == 'Стрелец':
        sign = search_sign(call.data)
        bot.send_message(call.message.chat.id, sign)
    elif call.data == 'Козерог':
        sign = search_sign(call.data)
        bot.send_message(call.message.chat.id, sign)
    elif call.data == 'Водолей':
        sign = search_sign(call.data)
        bot.send_message(call.message.chat.id, sign)
    elif call.data == 'Рыба':
        sign = search_sign(call.data)
        bot.send_message(call.message.chat.id, sign)

def search_sign(msg):
    with open('zodiac.txt', 'r') as data:
        for line in data:
            if msg in line:
                line = line.rstrip('\n')
                break
    return line


bot.polling(none_stop=True)