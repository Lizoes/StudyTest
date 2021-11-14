import unittest, os
import requests
from configparser import ConfigParser
from . import ddt


class WJFTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    @ddt.data("https://www.baidu.com/", "https://blog.csdn.net/")
    def test_getMethod(self, url):
        response = requests.get(url)
        print(response.url, response.text)

    def test_2(self):
        print("test_2")

    @unittest.skip("无条件跳过用例")
    def testNotRun(self):
        print("testNotRun")

    @unittest.skipIf(1 == 1, "条件=True时，执行这个case")
    def test_RunIf(self):
        print("test_RunIf")

    @unittest.skipUnless(1 == 1, "条件=False时，执行这个case")
    def test_RunUnless(self):
        print("test_RunUnless")

    @unittest.expectedFailure           # 当此用例未
    def test_expectedFailure(self):
        print("expectedFailure")

    @ddt.file_data()
    def ddd(self):
        pass


if __name__ == '__main__':
    unittest.main()



