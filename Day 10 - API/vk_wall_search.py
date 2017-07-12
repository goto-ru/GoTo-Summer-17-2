#https://oauth.vk.com/authorize?client_id=6109367&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos ,audio,video,docs,notes,pages,status,wall,groups,messages,notifications,offline&response_type=token


import requests

token = "TOKEN"
url = "https://api.vk.com/method/{0}?{1}&access_token={2}&v=5.67"


query = input("Что ищем? ")


result = requests.get(url.format("wall.search", "domain=kinopoisk&query={0}".format(query), token))
response = result.json()["response"]

for elem in response["items"]:
    print(elem["text"])
    print("-- "*6)

