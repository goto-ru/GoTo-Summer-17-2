import telebot
token = "394519885:AAEDmLpGlKlCkJY68hJKEe-hfCC1c1D-yXQ"

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Howdy, how are you doing?")

@bot.message_handler(content_types=['text'])
def echo(message):
	if message.text.lower().find("почему") != -1:
		bot.send_message(message.chat.id, "Азазаз")
	else:
		bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)