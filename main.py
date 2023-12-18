import telebot
from constants import TOKEN, COMANDS
from character import PERHOONA
from answers import ANSWERS

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
    bot.send_message(message.from_user.id, '''Ну разве не милашка?))''')


def music(message):
    audio = open(PERHOONA['music'], 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_audio')
    bot.send_audio(message.from_user.id, audio)
    audio.close()
    bot.send_message(message.from_user.id, '''Вот эта моя любимая)''')


def info(message):
    bot.send_message(message.from_user.id, '''
    Нуу... Зовут - Перона. Ляблю милых зверушек и сладости. Фрукт - Хоро-Хоро но ми(если это тебе что-либо говорит значит мы поладим)
    ''')


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
        bot.send_message(message.from_user.id, "Как дела?")
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
    elif 'тебе лет?' in message.text.lower():
        bot.send_message(message.from_user.id, '''У девушек такое не спрашивают вобще то (> n <)''')
    elif 'ответь' in message.text.lower() or 'ау' in message.text.lower():
        bot.send_message(message.from_user.id, '''Если не отвечаю, значит занята...''')
    else:
        for world in ANSWERS.keys():
            if world in message.text.lower():
                bot.send_message(message.from_user.id, ANSWERS[world])
                break
        else:
            bot.send_message(message.from_user.id, '''Прости, что?''')
            bot.send_message(message.from_user.id, '''O ^ O''')


bot.infinity_polling()
