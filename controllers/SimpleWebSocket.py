import tornado.ioloop
import tornado.web
import tornado.websocket
import redis
import time
from utils.redis import r
from utils.base import *
from utils.handler import handler
from config import config_instance
from multiprocessing import Process, Lock, Array

class SimpleWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        config_instance.connections.add(self)
        # p = Process(target=handler, args=(config_instance.connections, ))
        # p.start()

    def on_message(self, message):
        # r.set(time.time(), message, ex=3)
        #r.set(time.time(), message)
        res = check_blink_by_bin_face(message)
        [client.write_message(str(time.time()) + '     ' + str(res)) for client in config_instance.connections]

    def on_close(self):
        config_instance.connections.remove(self)

    def check_origin(self, origin):
        return True

