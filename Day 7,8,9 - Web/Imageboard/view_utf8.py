import json

with open('posts.json', 'rb') as file:
    data = file.read()

data = json.loads(data)

with open('text.txt', 'w') as file:
    file.write(str(data))