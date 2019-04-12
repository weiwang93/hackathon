'''
File: run.py
Project: quality
File Created: 2018-09-03 10:58:26 am
Author: wangwei (wangw11.thu@gmail.com)
-----
Last Modified: 2018-09-03 4:19:18 pm
Modified By: wangwei (wangw11.thu@gmail.com>)
'''

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from utils.logger import LOGGER
from config import config_instance
from urls import urls

def main():
    LOGGER.info('start')
    tornado.options.parse_command_line()
    app = tornado.web.Application(
            handlers=urls,
            debug=False)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config_instance.port)
    http_server.start(config_instance.process_num)

    #http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
