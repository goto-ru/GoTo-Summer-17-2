import telebot
import time
from threading import Thread

token = "394519885:AAEDmLpGlKlCkJY68hJKEe-hfCC1c1D-yXQ"

bot = telebot.TeleBot(token=token)

users = set()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Напиши /spam!")
    bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=rdg4lkgsQ04")

@bot.message_handler(commands=['spam'])
def start_spam(message):
    bot.send_message(message.chat.id, "Берем сироп вишневый!")
    users.add(message.chat.id)

@bot.message_handler(commands=['stop'])
def start_spam(message):
    bot.send_message(message.chat.id, "Сироп - все!")
    users.remove(message.chat.id)

def spam():
    while True:
        for user in users:
            bot.send_message(user, "Затем сироп вишневый!")
        time.sleep(2)

def polling():
    bot.polling(none_stop=True)

polling_thread = Thread(target=polling)
spam_thread = Thread(target=spam)

polling_thread.start()
spam_thread.start()


