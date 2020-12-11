# coding:utf-8
from selenium import webdriver
from common.base import Base
import time

login_url = "http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html"

class LoginPage(Base):  # 继承，相当于把类里面的所有方法copy过来，Base里面已经有init初始化方法和其他方法了，所有这里不用重新定义init和实例化了
    # 定位登录
    loc_user = ("id", "account")
    loc_psw = ("css selector", "[name='password']")
    loc_keep = ("id", "keepLoginon")
    loc_button = ("id", "submit")
    loc_forget_psw = ("link text", "忘记密码")

    loc_get_user = ("css selector", "#userMenu>a")
    loc_forget_psw_page = ("xpath", "html/body/div[1]/div/div[2]/p/a")

    # 将页面上可能做的操作（如输入账号，输入密码，点登陆等一些行为事件）封装成单独的方法，设计用例时直接调用
    def input_user(self, text=""):
        self.sendkeys(self.loc_user, text)

    def input_psw(self, text=""):
        self.sendkeys(self.loc_psw, text)

    def click_keep_login(self):
        self.click(self.loc_keep)

    def click_login_button(self):
        self.click(self.loc_button)

    def forget_psw(self):
        self.click(self.loc_forget_psw)

    def get_login_name(self):
        user = self.get_text(self.loc_get_user)
        return user

    def get_login_result(self, user):
        '''返回bool值'''
        result = self.is_text_in_element(self.loc_get_user, user)
        return result

    def is_alert_exist(self):
        '''判断alert是不是在'''
        a = self.is_alert()
        if a:
            print(a.text)
            a.accept()

    def is_refresh_exit(self):
        '''判断忘记密码页，刷新按钮是否存在'''
        r = self.is_element_exit1(self.loc_forget_psw_page)
        return r

    # 登录流程对于一些登陆后的用例去调用非常有用，但对于登录页面的测试不太好，写死了
    def login(self, username="admin", psw="123456", keep_login=False):
        '''登录流程'''
        self.driver.get(login_url)
        self.input_user(username)
        self.input_psw(psw)
        if keep_login: self.click_keep_login()  # keep_login=False，默认为未勾选状态
        self.click_login_button()


if __name__ == "__main__":
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    # login_page.login(keep_login=True)

    driver.get(login_url)
    login_page.input_user("admin")
    login_page.input_psw("123456")
    login_page.click_keep_login()
    login_page.click_login_button()
    # login_page.forget_psw()
    login_page.get_login_name()