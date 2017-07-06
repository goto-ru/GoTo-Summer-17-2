import telebot

token = "394519885:AAEDmLpGlKlCkJY68hJKEe-hfCC1c1D-yXQ"

bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "This is Python eval bot")


@bot.message_handler(content_types=['text'])
def echo(message):
    text = message.text
    try:
        result = eval(text)
        bot.send_message(message.chat.id, result)
    except:
        bot.send_message(message.chat.id, "Чувак, ты вхлам офигел! :(")

bot.polling(none_stop=True)
