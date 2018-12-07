import tornado.ioloop
import tornado.web
import os

root = os.path.dirname(__file__)

handlers = [
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": root+'/webroot', 'default_filename': 'index.html'})
]

app = tornado.web.Application(handlers)
app.listen(8080)
tornado.ioloop.IOLoop.current().start()