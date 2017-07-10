import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello, world</h1>")
        self.write("<p>Это походу наш сайт, и он даже работает.</p>")
        self.write("<img src='https://ic.pics.livejournal.com/drugoi/484155/797978/797978_original.jpg' width='500px' />")
        self.write("<p><a href='/page'>А вот тут про псов...</a></p>")
        self.write("<p><a href='/form'>Друтути...</a></p>")

class SecondHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("page.html")

class InputHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("form.html")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "EeOneGuy")
        description = self.get_argument("description", "")
        self.write("<h1>Хаю Хай, с вами {0}!</h1><p>{1}</p>".format(name, description))
    def post(self):
        name = self.get_argument("name", "EeOneGuy")
        description = self.get_argument("description", "")
        age = self.get_argument("age", "no")
        color = self.get_argument("color")
        self.write("<h1 align='center'>Это POST запрос</h1><h1>Хаю Хай, с вами {0}!</h1><p>{1}</p>".format(name, description))
        if age == "yes":
            self.write('<strong>Вы норм чувак</strong>')
        elif color=='other':
            self.write('<strong>Есть подозрение, что вы школоблоггер.</strong>')
        else:
            self.write('<strong>С вами все совсем плохо.</strong>')


routes = [
    (r'/', MainHandler),
    (r'/page', SecondHandler),
    (r'/hello', HelloHandler),
    (r'/form', InputHandler),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()