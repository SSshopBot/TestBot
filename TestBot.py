import telebot
from telebot import types

# import parser


TOKEN = "1268675939:AAEHvTZY-P0rhKnJWOKfZRDByzcTOK-_IDc"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Бонжур, епта!!!')

    keyboard = types.InlineKeyboardMarkup();
    keyboard.row_width = 1;

    key_good_1 = types.InlineKeyboardButton(text="Меф", callback_data="1");
    key_good_2 = types.InlineKeyboardButton(text="Герыч", callback_data="2");
    key_good_3 = types.InlineKeyboardButton(text="Еще какая-то ебула", callback_data="3");

    keyboard.add(key_good_1, key_good_2, key_good_3);

    # keyboard.add(key_good_1,key_good_2,key_good_3);
    bot.send_message(message.chat.id, "Выбирай, чем упороться:", reply_markup=keyboard);


@bot.callback_query_handler(func=lambda call: True)
def choose_goods(call):
    #    bot.send_message(call.message.chat.id, text = "!!!!");
    if call.data == "1":
        bot.send_message(call.message.chat.id, text="У тебя здоровья на Меф не хватит!");
    if call.data == "2":
        bot.send_message(call.message.chat.id, text="Герыч для тебя дорого, малолетний еблан!");
    if call.data == "3":
        bot.send_message(call.message.chat.id, text="До этой ебулы ты еще не дорос!!!");


bot.polling(none_stop=True)






