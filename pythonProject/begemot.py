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
    item4 = telebot.types.KeyboardButton('Анекдот на угад')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Добро пожаловать. Выбери действие', reply_markup=markup)




@bot.message_handler(content_types=['text'])

def send_mess(message):
    if message.text == 'Угадай число':
        bot.send_message(message.chat.id, 'Напиши число от 1 до 10')
        bot.register_message_handler(message, guess_number())
    elif message.text == 'Кинь кость':
        n = random.randint(1,6)
        bot.send_message(message.chat.id, 'Твой результат: ' + str(n))
    elif message.text == 'Знак зодиака':
        bot.send_message(message.chat.id, 'Выбери знак')
        markup = telebot.types.InlineKeyboardMarkup(row_width=4)
        but1 = telebot.types.InlineKeyboardButton('Овен', callback_data=1)
        but2 = telebot.types.InlineKeyboardButton('Телец', callback_data=2)
        but3 = telebot.types.InlineKeyboardButton('Близнец', callback_data=3)
        but4 = telebot.types.InlineKeyboardButton('Рак', callback_data=4)
        but5 = telebot.types.InlineKeyboardButton('Лев', callback_data=5)
        but6 = telebot.types.InlineKeyboardButton('Дева', callback_data=6)
        but7 = telebot.types.InlineKeyboardButton('Весы', callback_data=7)
        but8 = telebot.types.InlineKeyboardButton('Сорпион', callback_data=8)
        but9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data=9)
        but10 = telebot.types.InlineKeyboardButton('Козерог', callback_data=10)
        but11 = telebot.types.InlineKeyboardButton('Водолей', callback_data=11)
        but12 = telebot.types.InlineKeyboardButton('Рыба', callback_data=12)
        markup.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10, but11, but12)

        bot.send_message(message.chat.id, 'Отлично, а у вас?', reply_markup=markup)

    elif message.text == 'Анекдот наугад':
        bot.send_message(message.chat.id, 'Вот анекдот')
    else:
        bot.send_message(message.chat.id, 'Выбери кнопку!')

def randomiti():
    m = random.randint(1,10)
    return m

def guess_number(message):
    m = str(randomiti())
    if message.text == m:
        bot.send_message(message.chat.id, 'Угадал')
    else:
        bot.send_message(message.chat.id, 'Попробуй ещё раз')



bot.polling(none_stop=True)