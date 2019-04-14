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
import json

class SimpleWebSocket(tornado.websocket.WebSocketHandler):

    def clear_all(self):
        # 眼睛比例
        self.eye_rate.clear()
        # 鼻子卸率
        self.noise_rate.clear()
        # 上嘴唇中间点
        self.top_lip.clear()

    def open(self):
        config_instance.connections.add(self)
        self.eye_rate = deque(maxlen=30)
        self.noise_rate = deque(maxlen=20)
        self.top_lip = deque(maxlen=20)
        self.error_num = 0
        # p = Process(target=handler, args=(config_instance.connections, ))
        # p.start()

    def on_message(self, message):
        st = time.time()
        res = check_blink_by_bin_face(message)
        print(time.time() - st)
        #res = check_blink_by_bin(message)
        #print(time.time() - st)
        if res == -1:
            self.error_num += 1
            if self.error_num > 9:
                self.clear_all()
        else:
            st = time.time()
            ret = {}
            self.error_num = 0
            blink_status = handler_eye_rate(res['left_eye'], res['right_eye'], self.eye_rate, self.noise_rate)
            shack_status = handle_shake(res['nose_bridge'], self.noise_rate, res['top_lip'], self.top_lip)
            print(self.noise_rate)
            print(time.time() - st)
            if blink_status == 1:
                ret['wink'] = 1
            if shack_status != 0:
                ret['shake'] = shack_status
            if(len(ret.keys())>0):
                [client.write_message(json.dumps(ret)) for client in config_instance.connections]

    def on_close(self):
        config_instance.connections.remove(self)

    def check_origin(self, origin):
        return True

