import hashlib
import telebot

h = hashlib.sha256(b'meow123')
password_hash = h.hexdigest()

bot = telebot.TeleBot("5989044980:AAFXuN6EZcNDGhSKNgrNuPgdEVqp76yoUTs")


def plus(stroka):
    str2int = stroka.split("+")
    return int(str2int[0]) + int(str2int[1])


def logpass(password):
    hp = hashlib.sha256(bytes(password, encoding ='UTF-8'))
    if str(hp.hexdigest()) == str(password_hash):
        return "Welcome"
    else:
        return "Fuck You"


@bot.message_handler(commands=['start', 'help'])
def send_welcome1(message):
    bot.reply_to(message, "Привет, я тестовый бот ввода пароля")


@bot.message_handler(commands=['login'])
def send_welcome2(message):
    mes = bot.send_message(message.chat.id, text='Введите пароль, пожалуйста')
    bot.register_next_step_handler(mes, get_password)


def get_password(message):
    bot.reply_to(message, logpass(message.text))


print(password_hash)

bot.infinity_polling()
