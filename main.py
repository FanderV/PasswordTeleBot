import hashlib
import telebot

bot = telebot.TeleBot("5991855005:AAEWyzlP-Kih9JugPZZsiOPm0m1EzPEF2Zs")

with open('password.txt', 'r') as file:
    password_hash = file.read().strip()


def plus(stroka):
    str2int = stroka.split("+")
    return int(str2int[0]) + int(str2int[1])


def logpass(password):
    with open('password.txt', 'r') as file:
        correct_password = file.read().strip()
    hp = hashlib.sha256(bytes(password, encoding ='UTF-8'))
    print("Введенный пароль:", password)
    print("Хеш введенного пароля:", hp.hexdigest())
    print("Хеш правильного пароля:", correct_password)
    if str(hp.hexdigest()) == str(correct_password):
        return "верно"
    else:
        return "не верно"



@bot.message_handler(commands=['start', 'help'])
def send_welcome1(message):
    bot.reply_to(message, "Привет, я тестовый бот ввода пароля")


@bot.message_handler(commands=['login'])
def send_welcome2(message):
    mes = bot.send_message(message.chat.id, text='Введите пароль, пожалуйста')
    bot.register_next_step_handler(mes, get_password)


def get_password(message):
    bot.reply_to(message, logpass(message.text))


bot.infinity_polling()