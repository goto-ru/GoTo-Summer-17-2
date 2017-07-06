import telebot

token = "394519885:AAEDmLpGlKlCkJY68hJKEe-hfCC1c1D-yXQ"

bot = telebot.TeleBot(token=token)

names = {}


def dog_name_handler(message):
    name = message.text
    names[message.chat.id] = name
    answer = bot.send_message(message.chat.id, "Как зовут вашу собаку?")
    bot.register_next_step_handler(answer, final_handler)


def final_handler(message):
    dog_name = message.text
    name = names[message.chat.id]

    bot.send_message(message.chat.id,
                     "Вас зовут - {0}, а песика вашего - {1}. Главное - не перепутать!".format(dog_name, name))


@bot.message_handler(commands=['start'])
def name_handler(message):
    answer = bot.send_message(message.chat.id, "Как вас зовут?")
    bot.register_next_step_handler(answer, dog_name_handler)


bot.polling(none_stop=True)
