'''
File: config.py
Project: quality
File Created: 2018-09-04 5:01:27 pm
Author: wangwei (wangw11.thu@gmail.com)
-----
Last Modified: 2018-09-04 5:03:35 pm
Modified By: wangwei (wangw11.thu@gmail.com>)
'''
class Config:

    def __init__(self):
        self.VERSION = 'v1'
        self.process_num = 1
        self.port = 8887

        ## log
        self.log_name = 'mp-content-location-judge'
        self.log_level = 'debug'
        self.log_dir = 'logs/'

        ## threshold
        self.open_eye_rate = 0
        self.close_eye_rate = 0
        self.eye_th = 0

        self.connections = set()

config_instance = Config()
