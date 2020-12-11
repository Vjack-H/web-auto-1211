from selenium import webdriver
import unittest
from pages.login_page import LoginPage, login_url
import ddt   # 导入ddt框架（unittest框架的补充）
from common.read_excel import ExcelUtil
import os  # 导入os模块

# 写用例的时候，操作哪个页面，就去调用哪个页面的方法

'''
1.输入账号："admin"，密码：123456，点击登录
2.输入账号："admin"，密码：为空，点击登录
3.输入账号："admin111"，密码：123456，点击登录
'''

# 测试数据（数据源）---全局参数，放在class外面
# testdata = [
#     {"user": "admin", "psw": "123456", "expect": "admin"},
#     {"user": "admin", "psw": "", "expect": ""},
#     {"user": "admin111", "psw": "123456", "expect": ""}
# ]

# 将测试数据存放到excel表格，然后定义一个方法将excel数据转换成dict并用list存储返回，然后调用该方法读取并获取测试数据
# 文件路径用参照物读取，以当前脚本为参照物来读取文件excel的路径
curpath = os.path.realpath(__file__)  # 获取当前脚本的真实路径
# # 获取当前脚本的上一层路径case
casepath = os.path.dirname(os.path.realpath(__file__) )
# # 获取case的上一层路径web_auto
propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 以web_auto为参照物，获取路径common/data.xlsx,join连接工程路径+common+data.xlsx
excelPath = os.path.join(propath, "common", "data.xlsx")
print(excelPath)

data = ExcelUtil(excelPath)
testdata = data.dict_data()
print(testdata)

@ddt.ddt
class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)
        cls.driver.get(login_url)

    # 预置条件
    def setUp(self):
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()  # 清空cookies，退出登录,回到登录页面
        self.driver.refresh()
        self.driver.get(login_url)

    # 定义一个登录用例的方法
    def login_case(self, user, psw, expect):
        self.loginp.login(user, psw)
        # self.loginp.input_user(user)
        # self.loginp.input_psw(psw)
        # self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        print("测试结果：%s" % result)
        self.assertTrue(result == expect)

    @ddt.data(*testdata)   # * + list ：把list数据分开传入
    def test_01(self, data):
        '''输入账号："admin"，密码：123456，点击登录'''
        print("------------测试开始-------------")
        print("测试数据：%s" % data)
        self.login_case(data["user"], data["psw"], data["expect"])
        print("------------测试结束-------------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__mian__":
    unittest.main()
