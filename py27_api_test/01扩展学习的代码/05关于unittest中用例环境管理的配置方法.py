"""
============================
Author:柠檬班-木森
Time:2020/3/28   9:54
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        """每条用例执行之前都会执行"""
        print("-------1----setup-------")
        pass

    def tearDown(self):
        """每条用例执行之后都会执行"""
        print("-------2------teardown-----")
        pass

    @classmethod
    def setUpClass(cls):
        """该测试用例类中，所有的用例执行之前，会执行"""
        print("-------3-------setUpClass----")
        pass

    @classmethod
    def tearDownClass(cls):
        """该测试用例类中，所有的用例执行之后，会执行"""
        print("-------4-----tearDownClass------")
        pass

    def test_01(self):
        print("用例01正则执行")
        self.assertEqual(100, 100)

    def test_02(self):
        print("用例02正则执行")
        self.assertEqual(200, 200)


    def test_03(self):
        print("用例03正则执行")
        self.assertEqual(100, 100)

    def test_04(self):
        print("用例04正则执行")
        self.assertEqual(200, 200)