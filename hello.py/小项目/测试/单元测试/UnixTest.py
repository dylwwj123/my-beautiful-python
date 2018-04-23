import unittest
from test111 import summm
from test111 import jiannnn

class Test(unittest.TestCase):

    def setUp(self):
        print("开始测试时，自动调用")

    def tearDown(self):
        print("结束测试时，自动调用")

    def test_summm(self):
        self.assertEqual(summm(1,2),3,"加法有误")

    def test_jiannn(self):
        self.assertEqual(jiannnn(5,2),3,"减法有误")


if __name__ == '__main__':
    unittest.main()