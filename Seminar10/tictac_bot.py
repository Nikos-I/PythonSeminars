# import telebot

# tictac22_bot 5765994318:AAGHUasq8136GdCPOTFF3ukk8MXnZhzUaPU

# # Создаем экземпляр бота
# bot = telebot.TeleBot('5765994318:AAGHUasq8136GdCPOTFF3ukk8MXnZhzUaPU')
# # Функция, обрабатывающая команду /start
# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#     bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# # Запускаем бота
# bot.polling(none_stop=True, interval=0)


# import telebot, wikipedia, re
# # Создаем экземпляр бота
# bot = telebot.TeleBot('5765994318:AAGHUasq8136GdCPOTFF3ukk8MXnZhzUaPU')
# # Устанавливаем русский язык в Wikipedia
# wikipedia.set_lang("ru")
# # Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
# def getwiki(s):
#     try:
#         ny = wikipedia.page(s)
#         # Получаем первую тысячу символов
#         wikitext=ny.content[:1000]
#         # Разделяем по точкам
#         wikimas=wikitext.split('.')
#         # Отбрасываем всЕ после последней точки
#         wikimas = wikimas[:-1]
#         # Создаем пустую переменную для текста
#         wikitext2 = ''
#         # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
#         for x in wikimas:
#             if not('==' in x):
#                     # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
#                 if(len((x.strip()))>3):
#                    wikitext2=wikitext2+x+'.'
#             else:
#                 break
#         # Теперь при помощи регулярных выражений убираем разметку
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
#         # Возвращаем текстовую строку
#         return wikitext2
#     # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
#     except Exception as e:
#         return 'В энциклопедии нет информации об этом'
# # Функция, обрабатывающая команду /start
# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#     bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, getwiki(message.text))
# # Запускаем бота
# bot.polling(none_stop=True, interval=0)


# import telebot
# import random
# from telebot import types


# # Загружаем список интересных фактов
# f = open('data/facts.txt', 'r', encoding='UTF-8')
# facts = f.read().split('\n')
# f.close()
# # Загружаем список поговорок
# f = open('data/thinks.txt', 'r', encoding='UTF-8')
# thinks  = f.read().split('\n')
# f.close()
# # Создаем бота
# bot = telebot.TeleBot('5765994318:AAGHUasq8136GdCPOTFF3ukk8MXnZhzUaPU')
# # Команда start
# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#         # Добавляем две кнопки
#         markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item1=types.KeyboardButton("Факт")
#         item2=types.KeyboardButton("Поговорка")
#         markup.add(item1)
#         markup.add(item2)
#         bot.send_message(m.chat.id, 'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',  reply_markup=markup)
# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     # Если юзер прислал 1, выдаем ему случайный факт
#     if message.text.strip() == 'Факт' :
#             answer = random.choice(facts)
#     # Если юзер прислал 2, выдаем умную мысль
#     elif message.text.strip() == 'Поговорка':
#             answer = random.choice(thinks)
#     # Отсылаем юзеру сообщение в его чат
#     bot.send_message(message.chat.id, answer)
# # Запускаем бота

# bot.polling(none_stop=True, interval=0)

# # bot.updater.idle()


import telebot

# import config
import random

from telebot import types

bot = telebot.TeleBot('5765994318:AAGHUasq8136GdCPOTFF3ukk8MXnZhzUaPU')
item = {}


gameIsStart = False


gameGround = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]


CrossesOrToe = ["0", "X"]


playerSymbol = CrossesOrToe[random.randint(0, 1)]


botSymbol = ""
if (playerSymbol == "0"):
    botSymbol = "X"
else:
    botSymbol = "0"

print("Bot is start")

# lose/win

winbool = False

losebool = False


def clear():
    global gameGround
    gameGround = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " ", ]


def win(cell_1, cell_2, cell_3):
    if cell_1 == playerSymbol and cell_2 == playerSymbol and cell_3 == playerSymbol:
        print("win")
        global winbool
        winbool = True


def lose(cell_1, cell_2, cell_3):
    if cell_1 == botSymbol and cell_2 == botSymbol and cell_3 == botSymbol:
        print("lose")
        global losebool
        losebool = True


def defend(cell_1, cell_2, posDef):
    if cell_1 == playerSymbol and cell_2 == playerSymbol:
        posDef = botSymbol


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item[0] = types.KeyboardButton("Рандомное число")
    item[1] = types.KeyboardButton("Как дела?")
    item[2] = types.KeyboardButton("Крестики нолики")
    markup.add(item[0], item[1], item[2])

    if message.text == "/start":
        bot.send_message(message.chat.id,
                         "Привет,{0.first_name}!,я новый телеграм бот у меня есть всякие команды)".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    if message.chat.type == 'private':
        if message.text == "Рандомное число":
            bot.send_message(message.chat.id, str(random.randint(0, 10000)))
        elif message.text == "Как дела?":
            bot.send_message(message.chat.id, "Хорошо)")
        elif message.text == "Крестики нолики":
            global gameIsStart
            gameIsStart = True
        else:
            bot.send_message(message.chat.id, "Я не знаю таких слов :(")
    # game

    if gameIsStart == True:

        item = {}
        bot.send_message(message.chat.id, "Игра началась")

        global markup
        markup = types.InlineKeyboardMarkup(row_width=3)

        i = 0

        for i in range(9):
            item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])
        bot.send_message(message.chat.id, "Выбери клетку", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    if (call.message):

        # bot manager
        randomCell = random.randint(0, 8)
        if gameGround[randomCell] == playerSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == botSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == " ":
            gameGround[randomCell] = botSymbol
        # player manager
        for i in range(9):
            if call.data == str(i):
                if (gameGround[i] == " "):
                    gameGround[i] = playerSymbol

            # lose or win
            win(gameGround[0], gameGround[1], gameGround[2])
            win(gameGround[0], gameGround[4], gameGround[8])
            win(gameGround[6], gameGround[4], gameGround[2])
            win(gameGround[6], gameGround[7], gameGround[8])
            win(gameGround[0], gameGround[3], gameGround[6])
            lose(gameGround[0], gameGround[1], gameGround[2])
            lose(gameGround[0], gameGround[4], gameGround[8])
            lose(gameGround[6], gameGround[4], gameGround[2])
            lose(gameGround[6], gameGround[7], gameGround[8])
            lose(gameGround[0], gameGround[3], gameGround[6])

            item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Крестики нолики",
                              reply_markup=None)
        # update cells
        global  markup
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])

        bot.send_message(call.message.chat.id, "Выбери клетку", reply_markup=markup)
        global winbool
        if winbool:
            clear()
            bot.send_message(call.message.chat.id, "Я проиграл :(")

            winbool = False
            gameIsStart = False
        global losebool
        if losebool:
            clear()
            bot.send_message(call.message.chat.id, "Я выиграл!!")


            losebool = False
            gameIsStart = False


bot.polling(none_stop=True)
