@bot.callback_query_handler(func=lambda call: True)
def choose_goods(call):
    #    bot.send_message(call.message.chat.id, text = "!!!!");
    if call.data == "1":
        bot.send_message(call.message.chat.id, text="У тебя здоровья на Меф не хватит!");
    if call.data == "2":
        bot.send_message(call.message.chat.id, text="Герыч для тебя дорого, малолетний еблан!");
    if call.data == "3":
        bot.send_message(call.message.chat.id, text="До этой ебулы ты еще не дорос!!!");