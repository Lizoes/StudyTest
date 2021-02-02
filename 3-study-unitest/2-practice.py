import unittest, os
from configparser import ConfigParser


class WJFTest(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_1(self):
        print("test_1")

    def test_2(self):
        print("test_2")

    @unittest.skip
    def testNotRun(self):
        print("testNotRun")

    @unittest.skipIf(1 == 1, "不满足条件，不执行这个case")
    def test_RunIf(self):
        print("test_RunIf")


if __name__ == '__main__':
    # unittest.main()
    try:
        a = 1
    except:
        print("error")
    else:
        print("else")
    finally:
        print("finally")
    # 从ini文件获取配置信息
    projectPath = os.path.abspath(os.path.join(os.getcwd(), ".."))
    config = ConfigParser()
    config.read(projectPath + r"\conf\config.ini", encoding='utf-8-sig')
    print(type(config))
    section, option = 'people', 'nationality'
    try:
        nationality = config.get(section=section, option=option)
        print(nationality)
    except Exception as e:
        print("获取值失败:section=%s,option=%s" % (section, option))


