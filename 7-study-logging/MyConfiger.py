# @Time    : 2021/2/18 21:07
# @Author  : Lizo
# @File    : MyConfiger.py


import os
from configparser import ConfigParser


class MyConfigure(ConfigParser):
    def __init__(self, confPath):
        super().__init__()
        self.read(filenames=confPath, encoding='utf-8-sig')

    def getLogPath(self):
        return self.get(section="Log", option="path")


# 获取conf.ini的路径，生成一个MyConfigure
confPath = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\conf\config.ini"
myconfig = MyConfigure(confPath)
