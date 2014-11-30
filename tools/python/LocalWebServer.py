import tornado.httpserver
import tornado.ioloop
import tornado.web 
import mimetypes
import sys

import logging
logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)-15s %(levelname)-8s %(name)-8s %(message)s')

# Directory for "index.html" and "SNAP.js"
STATIC_PATH = "../../deploy" # Current working directory

# The HTTP port being served
WEBPORT = 80
        
def main():            
    # Initialize tornado web server
    ioloop = tornado.ioloop.IOLoop.instance()                                                                                        
    application = tornado.web.Application([        
        (r'/(.*)', tornado.web.StaticFileHandler,  {'path': STATIC_PATH, 'default_filename': 'index.html'})
    ])                                                                                                                              
    http_server = tornado.httpserver.HTTPServer(application)                                                                        
    http_server.listen(WEBPORT)     
                                                                                                        
    ioloop.start()   

if __name__ == "__main__":
    main()