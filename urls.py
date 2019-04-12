from config import config_instance
from controllers.test import test
from controllers.init_eye import initEye
from controllers.SimpleWebSocket import SimpleWebSocket
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop

class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

urls = [
    (r'/', IndexPageHandler),
    (r"/post_image", test),
    (r"/init_eye", initEye),
    (r"/ws", SimpleWebSocket),
]