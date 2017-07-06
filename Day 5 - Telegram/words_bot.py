import telebot

token = "394519885:AAEDmLpGlKlCkJY68hJKEe-hfCC1c1D-yXQ"

bot = telebot.TeleBot(token=token)

users = {}

@bot.message_handler(content_types=['text'])
def words(message):
    id = message.chat.id
    #пользователь ни разу не писал, его id нет в словаре
    if id not in users:
        users[id] = ""
        bot.send_message(id, "Чувак, говори первое слово!")
        return
    #пользователь уже добавился, но еще не прислал первое слово
    if users[id] == "":
        text = message.text.lower()
        users[id] = text
        bot.send_message(id, "ОК, второму бандиту на {0}:".format(text[-1].upper()))
        return
    #пользователь уже играет, он прислал слово
    else:
        new_word = message.text.lower()
        if new_word[0] == users[id][-1]:
            users[id] = new_word
            bot.send_message(id, "ОК, второму бандиту на {0}:".format(new_word[-1].upper()))
        else:
            bot.send_message(id, "Не не, это вообще не катит((")



bot.polling(none_stop=True)