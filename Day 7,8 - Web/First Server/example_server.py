import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello, world</h1>")
        self.write("<p>Это походу наш сайт, и он даже работает.</p>")
        self.write("<img src='https://ic.pics.livejournal.com/drugoi/484155/797978/797978_original.jpg' width='500px' />")
        self.write("<p><a href='/page'>А вот тут про псов...</a></p>")

class SecondHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("page.html")


routes = [
    (r'/', MainHandler),
    (r'/page', SecondHandler),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()