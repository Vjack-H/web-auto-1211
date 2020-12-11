import unittest

class Test1(unittest.TestCase):

    @classmethod    # 声明是类方法，用以区分实例方法setUp(self)
    def setUpClass(cls):   # 表示只需要打开一次浏览器，执行用例1、用例2，然后关闭浏览器
        print("用例前，只执行一次")

    @classmethod
    def tearDownClass(cls):   # 前置、后置条件是非必须的
        print("用例后，只调用一次")

    def test_01(self):  # test method names begin with 'test'
        '''用例说明：11111'''  # 加中文注释，用3个引号（'''）引起来，注释只能写一行，不能换行
        print("1111111111")
        a = "admin"    # 实际结果
        b = "admin"   # 预期结果
        # assert断言方法：判断实际结果与预期结果是否相等、包含等
        # self.assertIn(a,b)           # 传a,b两个参数，判断b是否包含a
        # self.assertNotIn(a,b)
        # self.assertEqual(a,b)      # 传a,b两个参数，判断是否相等
        # self.assertNotEqual(a,b)
        self.assertEqual(a, b)  # 判断括号内的表达式是否为真，如判断a和b是否相等
        # 因为该用例没有涉及到网页web的测试，截图是根据driver截的，所以断言失败后不会有截图

    def test_02(self):
        '''用例说明：22222'''
        print("2222222222")
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()