import tornado.ioloop
import tornado.web
from bson import ObjectId
from pymongo import MongoClient


#создаем конекшн с бд
client = MongoClient("mongodb://user:password@ds153682.mlab.com:53682/gotoch")
database = client['gotoch']
posts_collection = database['posts']

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        posts = list(posts_collection.find())
        self.render("Imageboard.html", posts=posts)

    def post(self):
        #добавление новой записи
        title = self.get_argument("title")
        text = self.get_argument("text")
        post = {"title": title, "text": text, "likes": 0, "comments": []}

        posts_collection.insert(post)

        self.redirect('/')

class LikeHandler(tornado.web.RequestHandler):
    def get(self):
        _id = self.get_argument('id')
        post = posts_collection.find_one({'_id': ObjectId(_id)})
        post['likes'] += 1
        posts_collection.update({'_id': ObjectId(_id)}, post)
        self.redirect('/')

class CommentHandler(tornado.web.RequestHandler):
    def post(self):
        _id = self.get_argument('id')
        post = posts_collection.find_one({'_id': ObjectId(_id)})

        author = self.get_argument("author")
        text = self.get_argument("text")
        comment = {"author": author, "text": text}

        post['comments'].append(comment)

        posts_collection.update({'_id': ObjectId(_id)}, post)
        self.redirect('/')



routes = [
    (r'/', MainHandler),
    (r'/like', LikeHandler),
    (r'/comment', CommentHandler),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()