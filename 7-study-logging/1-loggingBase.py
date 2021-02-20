# @Time    : 2021/2/17 15:56
# @Author  : Lizo
# @File    : 1-loggingBase.py

"""
日志器	Logger	    提供了应用程序可一直使用的接口
处理器	Handler	    将logger创建的日志记录发送到合适的目的输出
过滤器	Filter	    筛选需要输出的日志
格式器	Formatter	设置日志的输出格式

========Logger类=======
Logger.setLevel(logging.INFO)	    设置日志器的级别
Logger.addHandler()                 为该logger一个handler对象
Logger.removeHandler()	            为该logger移除handler对象
Logger.addFilter()                  为该logger添加一个filter对象
Logger.removeFilter()	            为该logger移除一个filter对象

Logger.debug(msg, *args, **kwargs)
Logger.info(msg, *args, **kwargs)
Logger.warning(msg, *args, **kwargs)
Logger.error(msg, *args, **kwargs)
Logger.critical(msg, *args, **kwargs)
Logger.log(level, msg, *args, **kwargs)

[logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,logging.CRITICAL]

logger = logging.getLogger(name)    # 获取一个名字为name的Logger

=====Handler类=======
Handler是一个基类，不应该直接实例化和使用Handler实例，可以使用一下子类
Handler.setLevel()	        设置handler将会处理的日志消息的最低严重级别
Handler.setFormatter()	    为handler设置一个格式器对象
Handler.addFilter()         为handler添加一个过滤器对象
Handler.removeFilter()	    为handler删除一个过滤器对象


logging.StreamHandler	                    将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象。
logging.FileHandler	                        将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
logging.handlers.RotatingFileHandler	    将日志消息发送到磁盘文件，并支持日志文件按大小切割
logging.handlers.TimedRotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按时间切割
logging.handlers.HTTPHandler	            将日志消息以GET或POST的方式发送给一个HTTP服务器
logging.handlers.SMTPHandler	            将日志消息发送给一个指定的email地址
logging.NullHandler	该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来避免'No handlers could be found for logger XXX'信息的出现。



filename    输出日志的文件名称前缀
when        日志切分的间隔时间单位:
            "S"：Second 秒
            "M"：Minutes 分钟
            "H"：Hour 小时
            "D"：Days 天
            "W"：Week day（0 = Monday）
            "midnight"：Roll over at midnight
interval    间隔时间单位的个数，指等待多少个 when 的时间后 Logger 会自动重建继续进行日志记录
backupCount 是保留日志的文件个数,默认是0，全部保留


=======Formatter类=======
fmt：指定消息格式化字符串，默认使用message的原始值
datefmt：指定日期格式字符串，默认使用"%Y-%m-%d %H:%M:%S"
style：可取值为 '%'、 '{'、 '$'，默认使用'%'
logging.Formatter.__init__(fmt=None, datefmt=None, style='%')


=======Filter类=======

"""
import time
import logging
from logging.handlers import TimedRotatingFileHandler


'''
1）所有级别的日志写入磁盘文件中
2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
4）要求all.log在每天凌晨进行日志切割
'''


class MyLogger:
    @staticmethod
    def getMyLogger():
        path = r"G:\Code\python workplace\StudyTest\log\\"
        fmt = "[%(asctime)s] [%(levelname)-8s] - %(message)s (%(filename)s:%(lineno)d)"
        # all.log记录所有的日志
        formatForAll = logging.Formatter(fmt=fmt, datefmt="%Y-%m-%d %H:%M:%S")
        handlerForAll = logging.FileHandler(filename=path+"all.log", mode="a", encoding="utf-8")
        handlerForAll.setLevel(logging.DEBUG)
        handlerForAll.setFormatter(fmt=formatForAll)

        # error.log记录ERROR的日志
        # handlerForError = TimedRotatingFileHandler(filename="all.log", when="midnight")
        handlerForError = TimedRotatingFileHandler(filename=path+"error.log", when="S")
        formatForError = logging.Formatter(fmt=fmt, datefmt="%Y-%m-%d %H:%M:%S")
        handlerForError.setLevel(logging.ERROR)
        handlerForError.setFormatter(fmt=formatForError)

        # 控制台输出
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)

        logger = logging.getLogger("myLogger")
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handlerForAll)
        logger.addHandler(handlerForError)
        logger.addHandler(consoleHandler)
        return logger


if __name__ == "__main__":
    mylogger = MyLogger.getMyLogger()
    for i in range(3):
        mylogger.log(logging.DEBUG, "this is DEBUG message")
        mylogger.log(logging.INFO, "this is INFO message")
        mylogger.log(logging.WARNING, "this is WARNING message")
        mylogger.log(logging.ERROR, "this is ERROR message")
        mylogger.log(logging.CRITICAL, "this is CRITICAL message")
        time.sleep(1)
