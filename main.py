import telebot
from constants import TOKEN, COMANDS
from character import PERHOONA

bot = telebot.TeleBot(TOKEN)


# Обрабатывает все текстовые сообщения, содержащие команды «/start»
def start(message):
    bot.send_message(message.from_user.id,
                     f'''Приветствую! Ты новенький? Вот список просьб, которые я, {PERHOONA['name'][1]}, выполню:''')
    help_mi(message)


def help_mi(message):
    bot.send_message(message.from_user.id, f'''Конечно помогу))''')
    for c in COMANDS:
        bot.send_message(message.from_user.id, c)


def photo(message):
    with open(PERHOONA['photo'], 'rb') as photo:
        bot.send_photo(chat_id=message.chat.id, photo=photo)


def music(message):
    # with open(PERHOONA['music'], 'rb') as photo:
    #     bot.send_photo(chat_id=message.chat.id, photo=photo)
    pass


def info(message):
    pass


# Обрабатывает все отправленные документы и аудиофайлы
@bot.message_handler(content_types=['audio', ''])
def docs_audio(message):
    bot.send_message(message.from_user.id, '''...
Даже не знаю как на такое реагировать...
А можешь просто написать об этом?''')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Приветик)")
    elif 'help' in message.text:
        help_mi(message)
    elif 'start' in message.text:
        start(message)
    elif 'photo' in message.text:
        photo(message)
    elif 'music' in message.text:
        music(message)
    elif 'info' in message.text:
        info(message)
    elif 'тебе лет?' in message.text:
        bot.send_message(message.from_user.id, '''У девушек такое не спрашивают вобще то (> n <)''')
    elif 'ответь' in message.text or 'Ау' in message.text:
        bot.send_message(message.from_user.id, '''Если не отвечаю, значит занята...''')
    elif '' in message.text:
        pass
    elif '' in message.text:
        pass


bot.infinity_polling()
