# -*- coding:utf-8 -*-

import sys
import logging
from datetime import datetime

class Logger(object):
    def __init__(self, logger_name):
        self._logger = logging.getLogger(logger_name)
        # self.DEFAULT_LOG_FILENAME = 'debug_{0}{1}.log'.format('yilong_', datetime.now().strftime('%m%d'))
        self.formatter = logging.Formatter("[%(asctime)s] [%(name)10s:%(lineno)4s] [%(funcName)s] [%(levelname)s] [%(message)s]")
        # self._logger.addHandler(self._get_file_handler(self.DEFAULT_LOG_FILENAME))
        self._logger.addHandler(self._get_console_handler())
        self._logger.setLevel(logging.DEBUG)  # 默认等级
        self._logger.propagate = False
        print("New Logger logger_name {} {} {}".format(logger_name, self._logger, self._logger.handlers))

    # def _get_file_handler(self, filename):
    #     filehandler = logging.FileHandler(filename, encoding="utf-8")
    #     filehandler.setFormatter(self.formatter)
    #     return filehandler

    def _get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    @property
    def logger(self):
        return self._logger
