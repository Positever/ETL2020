# -*- coding: utf-8 -*-
# author: Positever
# project:ETL2020
# datetime:2020/8/24 0024 下午 14:55
# software: PyCharm


import logging
import logging.config
from os import path
import functools
import traceback
import pandas as pd

'''开发一个日志系统，既要把日志输出到控制台，还要写入日志文件'''
'''用字典保存日志级别'''
format_dict = {
    1 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    2 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    3 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    4 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    5 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
}

class Logger():
    def __init__(self,logger):
        '''
        指定保存日志的文件路径，日志级别，以及调用文件将日志存入到指定的文件中
        '''
        logging.config.fileConfig(r'configs/logging.conf')
        self.logger = logging.getLogger(logger)

    def getlog(self):
        return self.logger

def create_logger(name):
    logger = Logger(name).getlog()
    return logger

class ContextFilter(logging.Filter):
    func_name = 'main'
    def filter(self, record):
        record.func_name = self.func_name
        return True

def log(text):
    def log_exception(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            logger = create_logger(text)
            try:
                fn(*args, **kwargs)
            except Exception as e:
                logger.error(str(e) + ' ' + fn.__name__)
                logger.error(traceback.format_exc())
        return wrapper
    return log_exception