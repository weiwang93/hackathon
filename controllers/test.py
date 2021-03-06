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
import tornado.web
import tornado.httpserver

from utils.base import check_blink
from config import config_instance

from controllers.BaseHandler import BaseHandler

class test(BaseHandler):
    def post(self):
        if config_instance.open_eye_rate == 0 or config_instance.close_eye_rate == 0:
            ret = {
                'result': 'failed',
                'msg': 'please post open eyes and close eyes pic first.'
            }
            self.finish(ret)
        ret = {'result': 'OK'}
        file_metas = self.request.files.get('file', None)  # 提取表单中‘name’为‘file’的文件元数据

        if not file_metas:
            ret['result'] = 'Invalid Args'
            return ret

        file_path = ''
        for meta in file_metas:
            filename = meta['filename']
            file_path = os.path.join('image', filename)

            with open(file_path, 'wb') as up:
                up.write(meta['body'])

        ret['rate'] = check_blink(file_path)
        self.write(json.dumps(ret))
