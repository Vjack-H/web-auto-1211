from selenium import webdriver
import unittest
from pages.login_page import LoginPage
from pages.add_bug_page import AddBugPage
import time
my_url = "http://127.0.0.1:82/zentao/my/"  # 用例里把参数放在代码最前面，即class外面

class AddBugCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()   # 将实例化跟登录放在setUpClass前置条件里
        cls.bug = AddBugPage(cls.driver)
        a = LoginPage(cls.driver)  # 在add bug用例中不会用到a实例，所以可以不用加cls,作为局部变量也可以
        a.login()

    def setUp(self):
        # 每个用例都在一个起点
        self.driver.get(my_url)

    def test_add_bug(self):
        '''添加BUG'''
        time_str = time.strftime("%Y_%m_%d %H_%M_%S")
        title = "测试bug标题"+time_str
        self.bug.add_bug(title)
        result = self.bug.is_add_bug_success(title)
        print(result)
        self.assertTrue(result) # 断言

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()