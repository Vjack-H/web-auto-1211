# coding:utf-8
from selenium import webdriver
from common.base import Base
import time


class AddBugPage(Base):  # 继承，继承相当于把Base类里面的所有方法copy过来,由于 Base里面已经有init初始化方法和其他方法了，所有这里不用重新定义init和实例化了

    # 添加bug
    loc_test = ("xpath", ".//*[@id='mainmenu']/ul/li[4]/a")  # 点测试tab
    loc_bug = ("xpath", ".//*[@id='modulemenu']/ul/li[2]/a")  # 点Bug
    loc_addbug = ("xpath", ".//*[@id='createActionMenu']/a")  # 点提Bug
    loc_trunk = ("xpath", ".//*[@id='openedBuild_chosen']/ul")  # 添加版本,点输入框
    loc_trunk_add = ("xpath", ".//*[@id='openedBuild_chosen']/div/ul/li")  # # 选择版本
    loc_input_title = ("id", "title") # 标题

    # 需要先切换到iframe上
    loc_input_body = ("class name", "article-content")  # 输入测试步骤
    loc_save = ("id", "submit")  # 点保存

    # bug新增列表
    loc_new = ("xpath", ".//*[@id='bugList']/tbody/tr/td[4]/a")

    def add_bug(self, title):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_trunk)
        self.click(self.loc_trunk_add)

        self.sendkeys(self.loc_input_title, title)
        # 输入body，先切换到iframe上
        frame = self.findElement(("class name", "ke-edit-iframe"))
        self.driver.switch_to.frame(frame)  # 通过页面上iframe的index定位,第一个是0
        # 富文本不能clear
        body = '''[预置条件]xxx
        [测试步骤]xxx
        [实际结果]xxx
        [预期结果]xxx
        '''
        self.sendkeys(self.loc_input_body, body)
        self.driver.switch_to.default_content()  # 切回主页面default_content

        self.click(self.loc_save)

    def is_add_bug_success(self, _text):
        '''返回bool值'''
        return self.is_text_in_element(self.loc_new, _text)


# 测试代码：测试流程能否跑的通
if __name__ == "__main__":
    driver = webdriver.Firefox()
    bug = AddBugPage(driver)

    from pages.login_page import LoginPage
    a = LoginPage(driver)
    a.login()

    time_str = time.strftime("%Y_%m_%d %H_%M_%S")
    title = "测试bug标题"+time_str
    bug.add_bug(title)
    result = bug.is_add_bug_success(title)
    print(result)






