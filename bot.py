import telebot
import buttons, database



bot = telebot.TeleBot('7915137454:AAGxTF39CoY9xzzIamv7XXIPDQZYh9qjApc')



@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if database.check_user(user_id):
        bot.send_message(user_id, f'Добро пожаловать, @{message.from_user.username}!')
    else:
        bot.send_message(user_id, 'Привет Даввай начнем регистрацию\nНапиши свое имя',
                         reply_markup=telebot.types.ReplyKeyboardRemove())

        bot.register_next_step_handler(message, get_name)



@bot.message_handler(content_types=['text'])

def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, 'Отлично Тепер отправть свой номер',
                     reply_markup=buttons.num_button())

    bot.register_next_step_handler(message, get_num, user_name)



def get_num(message, user_name):
    user_id = message.from_user.id

    if message.contact:
        user_num = message.contact.phone_number

        database.register(user_id, user_name, user_num)
        bot.send_message(user_id, 'Регистрация прошла успешно!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())

    else:
        bot.send_message(user_id, 'Отправте кантакт по кнопке или через скрепку!')

        bot.register_next_step_handler(message, get_num, user_name)







