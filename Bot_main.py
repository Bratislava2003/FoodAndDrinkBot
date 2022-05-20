import telebot
import random
from telebot import types

Bot_API = '5078604639:AAG46KGuLk-do6kD_diezPWAHqoX4m2izD4'
bot = telebot.TeleBot(Bot_API)

Places = [
    'Греко Гирос и Сувлаки',
    'Ploveberry',
    'Суши маркет',
    'Теремок',
    'DimSum & Co.',
    'Burger King',
    'Франклинс Бургер',
    'Ciao Pizza',
    'Ливан Хаус',
    'PhoBo',
    'Макдоналдс',
    'KFC',
    'Gagawa',
    'Крошка Картошка',
    'Mr. Falafel',
    'Глютенутые',
    'Мидиитека',
    'Poke',
    'Три Правила',
    'Cofix',
    'Farш'
]

light =[
    "Пиво",
    "Сидр",
    "Перри"
]
middle = [
    "Вино",
    "Портвейн",
    "Вермут",
    "Саке",
    "Наливка",
    "Шампанское",
    "Мартини"
]
heavy = [
    "Абсент",
    "Водка",
    "Ликёр",
    "Коньяк",
    "Виски",
    "Аквавит",
    "Бурбон",
    "Джин",
    "Ром",
    "Чача"
]

Drinks = [
    light,
    middle,
    heavy
          ]

ans_st = [
    "Прекрсно. Я думаю ",
    "Ну что ж, в этом случае ",
    "Я думаю ",
    "Я тебя понял. Тогда ",
    "Окей, ",
    "Тогда ",
    "В таком случае "
]

ans_end = [
    " отлично скрасит твоё время!",
    " будет неплохим вариантом!",
    " будет твоим лучшим выбором в данной ситуации",
    ". Однозначно",
    ". Самое то для тебя",
    ". В прошлый раз было неплохо. Не помнишь? Неудивительно)))",
    ". Обязательно будет что забыть!"
]

markup = types.ReplyKeyboardMarkup()
Mitem = types.KeyboardButton('Хочу жрать!')
Mitem_2 = types.KeyboardButton('Хочу выпить!')
markup.add(Mitem, Mitem_2, row_width= 1)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я буду помогать тебе с выбором еды)', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == 'Хочу жрать!':
        answer = 'Тебе стоит сходить в ' + random.choice(Places)
        bot.send_message(message.chat.id, answer)
        lucky = random.randint(0, 999999)
        if lucky == 999999:
            bot.send_message(message.chat.id, "Это счастливое сообщение)")
    elif message.text.strip() == 'Хочу выпить!':
        Dr_markup = types.ReplyKeyboardMarkup()
        item_L = types.KeyboardButton('Полегче')
        item_M = types.KeyboardButton('Поинтереснее')
        item_H = types.KeyboardButton('Покрепче')
        item_R = types.KeyboardButton('Мне похую')
        Dr_markup.add(item_L, item_M, item_H, item_R, row_width=3)
        bot.send_message(message.chat.id, "Чего желаете?", reply_markup = Dr_markup)
        bot.register_next_step_handler(message, step2)

def step2(message):
    if message.text.strip() == "Полегче":
        DRL_Answer = random.choice(ans_st) + random.choice(light) +random.choice(ans_end)
        bot.send_message(message.chat.id, DRL_Answer, reply_markup=markup)
        handle_text(message)
    if message.text.strip() == "Поинтереснее":
            DRM_Answer = random.choice(ans_st) + random.choice(middle) + random.choice(ans_end)
            bot.send_message(message.chat.id, DRM_Answer, reply_markup=markup)
            handle_text(message)
    if message.text.strip() == "Покрепче":
            DRH_Answer = random.choice(ans_st) + random.choice(heavy) + random.choice(ans_end)
            bot.send_message(message.chat.id, DRH_Answer, reply_markup=markup)
            handle_text(message)
    if message.text.strip() == "Мне похую":
        DRR_Answer = random.choice(ans_st) + random.choice(random.choice(Drinks)) +random.choice(ans_end)
        bot.send_message(message.chat.id, DRR_Answer, reply_markup=markup)
        handle_text(message)



bot.polling(none_stop= True, interval= 0)
