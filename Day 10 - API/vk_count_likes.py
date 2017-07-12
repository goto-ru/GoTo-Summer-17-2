import requests

token = "TOKEN"
url = "https://api.vk.com/method/{0}?{1}&access_token={2}&v=5.67"


posts = []

result = requests.get(url.format("wall.get", "domain=roctbb&count=1", token))
response = result.json()['response']
count = response['count']

for i in range(0, count, 100):
    print(i)
    result = requests.get(url.format("wall.get", "domain=roctbb&count=100&offset={0}".format(i), token))
    response = result.json()['response']
    posts += response['items']


print('downloaded: {0}'.format(len(response['items'])))

posts = sorted(posts, key=lambda x:x["likes"]["count"], reverse=True)

for post in posts[:100]:
    print(post['text'])
    if "attachments" in post:
        print(post['attachments'])
    print('likes: {0}'.format(post["likes"]["count"]))
    print('-- '*10)

    #157429953
