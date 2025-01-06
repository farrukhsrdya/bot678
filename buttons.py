from telebot import types


def num_button():

    kk = types.ReplyKeyboardMarkup(resize_keyboard=True)

    num = types.KeyboardButton('Отправить номер', request_contact=True)

    kk.add(num)

    return kb