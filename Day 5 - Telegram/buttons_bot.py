import telebot
from telebot import types

token = "394519885:AAEDmLpGlKlCkJY68hJKEe-hfCC1c1D-yXQ"

bot = telebot.TeleBot(token=token)

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Кнопка 1", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Кнопка 2", callback_data="button2")
    keyboard.add(button1)
    keyboard.add(button2)
    bot.send_message(message.chat.id, "Нажмите на кнопку", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "button1":
            bot.send_message(call.message.chat.id, "Вы нажали на кнопку 1")
        if call.data == "button2":
            bot.send_message(call.message.chat.id, "Вы нажали на кнопку 2")


bot.polling(none_stop=True)