import unittest
from Test222 import Person

class Test(unittest.TestCase):

    def setUp(self):
        print("开始测试时，自动调用")

    def tearDown(self):
        print("结束测试时，自动调用")

    def test_init(self):
        p = Person("aaa",18)
        self.assertEqual(p.name,"aaa","属性赋值错误")

    def test_getVar(self):
        p = Person("aaa",18)
        self.assertEqual(p.getVar(),p.age,"getAge函数有误")


if __name__ == '__main__':
    unittest.main()