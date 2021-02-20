# @Time    : 2021/2/18 20:50
# @Author  : Lizo
# @File    : MyLogger.py


import logging
from logging.handlers import TimedRotatingFileHandler
from .MyConfiger import myconfig


class MyLogger:
    def __init__(self, fmt=None, level=None):
        self.fmt = fmt if fmt else "[%(asctime)s] [%(levelname)-8s] - %(message)s (%(filename)s:%(lineno)d)"
        self.level = level if level else logging.DEBUG

    def createMyLogger(self, logPath, name="all.log"):
        # 日志的格式
        myFormat = logging.Formatter(fmt=self.fmt, datefmt="%Y-%m-%d %H:%M:%S")
        # all.log记录所有的日志
        handlerForAll = logging.FileHandler(filename=logPath + name, mode="a", encoding="utf-8")
        handlerForAll.setLevel(self.level)
        handlerForAll.setFormatter(fmt=myFormat)
        # error.log记录ERROR以上的日志
        handlerForError = TimedRotatingFileHandler(filename=logPath + "error.log", when="midnight")
        handlerForError.setLevel(logging.ERROR)
        handlerForError.setFormatter(fmt=myFormat)
        # 控制台输出
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)

        logger = logging.getLogger("myLogger")
        return logger


logPath = myconfig.getLogPath()
mylogger = MyLogger().createMyLogger(logPath)
