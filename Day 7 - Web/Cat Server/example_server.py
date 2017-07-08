import random

import tornado.ioloop
import tornado.web

cats = [
    {"name": "Микроскоп", "url": "http://kaifolog.ru/uploads/posts/2015-09/1443418003_051.jpg"},
    {"name": "Костыль", "url": "https://otvet.imgsmail.ru/download/284bc47836695e949efe303fd166d895_i-4.jpg"},
    {"name": "Оглобля", "url": "http://s.pikabu.ru/post_img/2013/11/05/8/1383650425_224341998.jpg"},
    {"name": "Мотыль", "url": "https://s00.yaplakal.com/pics/pics_original/8/1/4/4248418.jpg"}
]


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cat = random.choice(cats)
        self.render('cat.html', name=cat['name'], image=cat['url'])


routes = [
    (r'/', MainHandler),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
