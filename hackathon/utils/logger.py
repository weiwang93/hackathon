'''
File: logger.py
Project: utils
File Created: 2018-09-03 2:26:56 pm
Author: wangwei (wangw11.thu@gmail.com)
-----
Last Modified: 2018-09-04 4:57:16 pm
Modified By: wangwei (wangw11.thu@gmail.com>)
'''

import logging
from logging.handlers import TimedRotatingFileHandler
import socket

import os
import sys
sys.path.append('../')
from config import config_instance

def initLogger():
    generalLogName = config_instance.log_name
    logDir  = os.path.join(config_instance.log_dir, generalLogName)
    if (not os.path.exists(logDir)):
        os.makedirs(logDir, exist_ok=True)

    # config logger for default logger

    loggers = {}

    for logName in [generalLogName, 'tornado.access', 'tornado.application', 'tornado.general']:
        logPath = os.path.join(logDir, logName + '-' + str(config_instance.port) + '.log')

        logger = logging.getLogger(logName)

        hdlr = TimedRotatingFileHandler(logPath, when="midnight", interval=1)
        hdlr.suffix = "%Y%m%d"
        hostname = socket.gethostname()
        formatter = logging.Formatter('{} %(asctime)s.%(msecs)03d [%(name)s-%(process)d] %(levelname)s %(filename)s.%(module)s.%(funcName)s[%(lineno)d] - %(message)s'.format(hostname),
                                      "%Y-%m-%d %H:%M:%S")
        hdlr.setFormatter(formatter)

        logger.addHandler(hdlr)
        logger.propagate = False
        if (config_instance.log_level == "debug"):
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)

        loggers[logName] = logger

    return loggers[generalLogName]

LOGGER = initLogger()