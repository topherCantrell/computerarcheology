import tornado.ioloop
import tornado.web
import os

root = os.path.dirname(__file__)

cont = os.path.join(root,'../../deploy')
print(cont)

handlers = [
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": cont, 'default_filename': 'index.html'})
]

app = tornado.web.Application(handlers)
app.listen(80)
tornado.ioloop.IOLoop.current().start()