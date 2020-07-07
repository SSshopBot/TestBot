import telebot
from telebot import types

# import parser


TOKEN = "1268675939:AAEHvTZY-P0rhKnJWOKfZRDByzcTOK-_IDc"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):

    keyboard = types.InlineKeyboardMarkup();
    keyboard.row_width = 1;

    key_good_1 = types.InlineKeyboardButton(text="Товар 0,5", callback_data="0,5");
    key_good_2 = types.InlineKeyboardButton(text="Товар 1", callback_data="1");

    keyboard.add(key_good_1, key_good_2);

    bot.send_message(message.chat.id, "Выбирай, чем упороться:", reply_markup=keyboard);





bot.polling(none_stop=True)






