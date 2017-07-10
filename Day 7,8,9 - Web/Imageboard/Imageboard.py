import json

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #рендеринг страницы

        with open("posts.json") as file:
            data = file.read()
        posts = json.loads(data)

        self.render("Imageboard.html", posts=posts)
    def post(self):
        #добавление новой записи
        title = self.get_argument("title")
        text = self.get_argument("text")
        post = {"title": title, "text": text}

        with open("posts.json") as file:
            data = file.read()
        posts = json.loads(data)
        posts.append(post)

        data = json.dumps(posts)

        with open("posts.json", 'w') as file:
            file.write(data)

        self.redirect('/')



routes = [
    (r'/', MainHandler),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()