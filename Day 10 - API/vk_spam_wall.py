#https://oauth.vk.com/authorize?client_id=6109367&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos ,audio,video,docs,notes,pages,status,wall,groups,messages,notifications,offline&response_type=token


import requests

token = "TOKEN"
url = "https://api.vk.com/method/{0}?{1}&access_token={2}&v=5.67"


for i in range(20):
    result = requests.get(url.format("wall.post", "owner_id=157429953&message={0}".format("Пора начать учиться!!!!"), token))
    print(result.json())

