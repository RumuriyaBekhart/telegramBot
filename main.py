import telebot
from constants import TOKEN
from character import PERHOONA

bot = telebot.TeleBot(TOKEN)
COMANDS = [
    'start',
    'help_me',
    'photo',
    'music',
    'info'
]


# Обрабатывает все текстовые сообщения, содержащие команды «/start»
def start(message):
    bot.send_message(message.from_user.id, f'''Приветствую! Ты новенький?
    Вот список вопросов, которые я,{PERHOONA['name'][1]} , разрешаю мне задать:''')
    help_mi(message)


def help_mi(message):
    bot.send_message(message.from_user.id, *COMANDS)


def photo(message):
    with open(PERHOONA['photo'], 'rb') as photo:
        bot.spend_photo(chat_id=message.chat.id, photo=photo)


def music(message):
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
    elif '' in message.text:
        pass
    elif '' in message.text:
        pass
    elif '' in message.text:
        pass
    elif '' in message.text:
        pass
    elif '' in message.text:
        pass
    elif '' in message.text:
        pass
    elif '' in message.text:
        pass


bot.infinity_polling()
