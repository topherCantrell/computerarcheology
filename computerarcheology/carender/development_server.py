import sys

import tornado.ioloop
import tornado.web


if sys.platform == 'win32':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

handlers = [
    (r"/(.*)", tornado.web.StaticFileHandler, {'path': './deploy', 'default_filename': 'index.html'})
]

app = tornado.web.Application(handlers)
app.listen(8080)
tornado.ioloop.IOLoop.current().start()

# py -m computerarcheology.carender.development_server
