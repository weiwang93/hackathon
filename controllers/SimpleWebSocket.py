import tornado.ioloop
import tornado.web
import tornado.websocket
import redis
import time
from utils.redis import r
from utils.base import *
from config import config_instance
from multiprocessing import Process, Lock, Array
from collections import deque

class SimpleWebSocket(tornado.websocket.WebSocketHandler):

    def clear_all(self):
        self.eye_rate.clear()

    def open(self):
        config_instance.connections.add(self)
        self.eye_rate = deque(maxlen=40)
        self.error_num = 0
        # p = Process(target=handler, args=(config_instance.connections, ))
        # p.start()

    def on_message(self, message):
        res = check_blink_by_bin_face(message)
        #st = time.time()
        #res = check_blink_by_bin(message)
        #print(time.time() - st)
        if res == -1:
            self.error_num += 1
            if self.error_num > 5:
                self.clear_all()
        else:
            self.error_num = 0
            blink_status = handler_eye_rate(res['left_eye'], res['right_eye'], self.eye_rate)
            print(self.eye_rate)
            if blink_status == 1:
                [client.write_message('1') for client in config_instance.connections]

    def on_close(self):
        config_instance.connections.remove(self)

    def check_origin(self, origin):
        return True

