from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Base():
    '''基于原生的selenium做二次封装'''
    # 这里的driver是一个形参，没有定义，所以需要映射(driver:webdriver.Firefox),相当于是webdriver.Firefox的这个类，那么继承过去的driver就能调用它里面的方法了（driver.）
    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElementNew(self, locator):
        '''定位到元素，返回元素对象，没定位到，抛Timeout异常'''
        if not isinstance(locator, tuple):  # 若locator不是tuple类型
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            print("正在定位元素信息：定位方式->%s,value->%s"%(locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return ele

    # 定位一个元素
    def findElement(self, locator):
        '''单数定位element，定位不到抛Timeout异常'''
        if not isinstance(locator, tuple):  # 若locator不是tuple类型
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            print("正在定位元素信息：定位方式->%s,value->%s"%(locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    # 定位一组元素
    def findElements(self, locator):
        '''复数定位elements，定位不到就返回空list，不会抛异常'''
        if not isinstance(locator, tuple):  # 若locator不是tuple类型
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                print("正在定位元素信息：定位方式->%s,value->%s"%(locator[0], locator[1]))
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
                return eles
            except:
                return []

    def sendkeys(self, locator, text):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

    def is_selected(self, locator):
        '''判断元素是否被选中,返回bool值'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def is_element_exit1(self, locator):
        '''判断元素是否存在,返回bool值（单数定位）'''
        try:
            ele = self.findElement(locator)
            return True
        except:
            return False

    def is_element_exit2(self, locator):
        '''判断元素是否存在,返回bool值（复数定位）'''
        eles = self.findElements(locator)  # 返回list
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True

    def is_title(self, _title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text):
        '''返回bool值'''
        if not isinstance(locator, tuple):  # 若locator不是tuple类型
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                print("正在定位元素信息：定位方式->%s,value->%s"%(locator[0], locator[1]))
                result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
                return result
            except:
                return False

    def is_value_in_element(self, locator, _value):
        '''返回bool值,value为空字符串，返回False'''
        if not isinstance(locator, tuple):  # 若locator不是tuple类型
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                print("正在定位元素信息：定位方式->%s,value->%s"%(locator[0], locator[1]))
                result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, _value))
                return result
            except:
                return False

    def is_alert(self):
        '''判断alert是否存在，存在返回alert对象，不存在返回False'''
        try:
            result = WebDriverWait(self.driver, 3, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_text(self, locator):
        '''获取文本'''
        if not isinstance(locator, tuple):  # 若locator不是tuple类型
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                print("正在定位元素信息：定位方式->%s,value->%s"%(locator[0], locator[1]))
                t = self.findElement(locator).text
                return t
            except:
                print("获取text失败，返回''")
                return ""

    def move_to_element(self, locator):
        '''鼠标悬停操作'''
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()

    def select_by_index(self, locator, index=0):
        '''通过索引定位，index是索引第几个，从0开始，默认选第一个'''
        ele = self.findElement(locator)  # 定位select这一栏，即select元素
        Select(ele).select_by_index(index)

    def select_by_value(self, locator, value):
        '''通过value属性定位'''
        ele = self.findElement(locator)  # 先定位元素
        Select(ele).select_by_value(value)  # 再操作方法

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        ele = self.findElement(locator)
        Select(ele).select_by_visible_text(text)

    def js_focus(self, locator):
        '''聚焦元素，滚动到元素出现的位置，把元素放到当前屏幕的最上方'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        '''滚动到底部'''
        js = "window.scrollTo(%s, document.body.scrollHeight)"%x  # js中的document.body.scrollHeight函数根据当前窗口自动计算出高度
        self.driver.execute_script(js)



if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html")
    # driver.get("https://www.baidu.com")
    zentao = Base(driver)

    # 定位方法
    # loc1 = (By.ID, "account")
    # loc2 = (By.CSS_SELECTOR, "[name='password']")
    # loc3 = (By.XPATH, "//*[@id='submit']")

    loc1 = ("id", "account")
    loc2 = ("css selector", "[name='password']")
    loc3 = ("xpath", "//*[@id='submit']")
    loc_settings = ("id", "s-usersetting-top")
    # 操作方法
    zentao.sendkeys(loc1, "admin")
    zentao.sendkeys(loc2, "123456")
    zentao.click(loc3)
    # zentao.move_to_element(loc_settings)

    # 如切换窗口，alert，iframe等还是调用原生的api方法，即用driver实例的方法
    # driver.switch_to.window()
    # driver.switch_to.alert
    # driver.switch_to.frame()
