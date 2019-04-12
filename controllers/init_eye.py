'''
File: cityHandler.py
Project: controllers
File Created: 2019-01-28 10:59:03 am
Author: wangwei (wangw11.thu@gmail.com)
-----
Last Modified: 2019-01-28 5:30:54 pm
Modified By: wangwei (wangw11.thu@gmail.com>)
'''
import os
import sys
import time
import json
import requests
import traceback
import tornado.web
import tornado.httpserver

from utils.base import *

from config import config_instance
from controllers.BaseHandler import BaseHandler

class initEye(BaseHandler):
    def post(self):
        ret = {'result': 'OK'}
        try:
            file_metas = self.request.files.get('open_eye', None)  # 提取表单中‘name’为‘file’的文件元数据
            for meta in file_metas:
                filename = meta['filename']
                file_path = os.path.join('image', filename)

                with open(file_path, 'wb') as up:
                    up.write(meta['body'])

            # ret['open_eye_rate'] = check_blink_face(file_path)
            ret['open_eye_rate'] = check_blink(file_path)
            config_instance.open_eye_rate = ret['open_eye_rate']


            file_metas = self.request.files.get('close_eye', None)  # 提取表单中‘name’为‘file’的文件元数据

            for meta in file_metas:
                filename = meta['filename']
                file_path = os.path.join('image', filename)

                with open(file_path, 'wb') as up:
                    up.write(meta['body'])

            # ret['close_eye_rate'] = check_blink_face(file_path)
            ret['close_eye_rate'] = check_blink(file_path)
            config_instance.close_eye_rate = ret['close_eye_rate']

            if config_instance.close_eye_rate * 1.3 > config_instance.open_eye_rate:
                ret['message'] = 'error'
                self.finish(json.dumps(ret))
                return
            config_instance.eye_th = config_instance.close_eye_rate + (config_instance.open_eye_rate - config_instance.close_eye_rate) / 3
            print(config_instance.eye_th)
            self.finish(json.dumps(ret))
            return
        except Exception as e:
            ret['error_msg'] = str(e)
            traceback.print_exc()
            self.finish(json.dumps(ret))