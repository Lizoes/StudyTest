# be careful the path with '\' not '/'
import os
from configparser import ConfigParser


# 从ini文件获取配置信息
if __name__ == "__main__":
    projectPath = os.path.abspath(os.path.join(os.getcwd(), ".."))
    config = ConfigParser()
    config.read(projectPath + r"\conf\config.ini", encoding='utf-8-sig')
    section, option = 'people', 'nationality'
    try:
        nationality = config.get(section=section, option=option)
        print(nationality)
    except Exception as e:
        print("获取值失败:section=%s,option=%s" % (section, option))
