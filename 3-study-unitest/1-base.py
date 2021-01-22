'''
TestCase：测试用例,完整的测试用例流程：测试前准备环境的搭建(setUp)，执行测试代码 (run)，以及测试后环境的还原(tearDown)，需要继承unittest.TestCase
TestSuite：测试套件，是多个测试用例的集合。
TestRunner：运行器，执行测试用例，通过Runner调用TestSuite执行测试
TestLoader：吧TestCase加载到TestSuite，
TestFixture：通过TestCase的setUp和tearDown实现一个测试用例环境的创建和销毁，前置条件、后置条件
TestReport：生成测试报告
'''

'''
self.assertEqual(a, b, msg)      a == b    msg为断言失败的提示信息，以下类似
self.assertNotEqual(a, b)        a != b
self.assertTrue(x)               bool(x) is True
self.assertFalse(x)              bool(x) is False
self.assertIs(a, b)              a is b
self.assertIsNot(a, b)           a is not b
self.assertIsNone(x)             x is None
self.assertIsNotNone(x)          x is not None
self.assertIn(a, b)              a in b
self.assertNotIn(a, b)           a not in b
self.assertIsInstance(a, b)      isinstance(a, b)
self.assertNotIsInstance(a, b)   not isinstance(a, b)
'''

import unittest


class WJFTestCase(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_2(self):
        print("test_2")

    def test_1(self):
        print("test_1")



    @unittest.skip
    def testNotRun(self):
        print("testNotRun")

    @unittest.skipIf(1 == 1, "不满足条件，不执行这个case")
    def test_RunIf(self):
        print("test_RunIf")

unittest.main()


'''
# 启动
1、这种方法，启动时会执行所有满足条件的测试用例，执行顺序为方法名字按照ASCII排序
unittest.main()
2、执行添加的测试用例，执行的顺序为添加的顺序
testSuite = unittest.TestSuite()
testCaseList = [WJFTestCase(methodName='test_1'), WJFTestCase(methodName='test_2')]
testSuite.addTests(testCaseList)
unittest.TextTestRunner().run(testSuite)
3、
suite = unittest.TestLoader().loadTestsFromTestCase(WJFTestCase)
testSuite = unittest.TestSuite(suite)
unittest.TextTestRunner().run(testSuite)
'''

'''
configerparser
'''
unittest.TestSuite.addTests()
s = "sss"
print(isinstance(s, type))
