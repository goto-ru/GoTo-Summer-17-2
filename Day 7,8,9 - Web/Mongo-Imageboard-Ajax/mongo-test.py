from bson import ObjectId
from pymongo import MongoClient

#создаем конекшн с бд
client = MongoClient("mongodb://user:password@ds153682.mlab.com:53682/gotoch")

#выбираем бд
database = client['gotoch']

#выбираем коллекцию
posts_collection = database['posts']

#добавляем посты
post = {"title": "Берем сироп вишневый", "text": "Тут короч детальный мануал как это делать"}
posts_collection.insert(post)

#получение документов из бд
posts = list(posts_collection.find())
print(posts)

#получение конкретного
print(list(posts_collection.find({'_id': ObjectId('596343e3551f20202ce7f02f')})))

#удаление
posts_collection.remove({'_id': ObjectId('596343e3551f20202ce7f02f')})

#обновление
post = posts_collection.find_one({'_id': ObjectId('5963438e551f20201ba46c7b')})
post['text'] = "Затем сироп вишневый"
posts_collection.update({'_id': ObjectId('5963438e551f20201ba46c7b')}, post)



