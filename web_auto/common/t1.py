from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://sz.ganji.com/")

time.sleep(4)
# 滚动到底部
js = "window.scrollTo(0, document.body.scrollHeight)"   # js中的document.body.scrollHeight函数根据当前窗口自动计算出高度
driver.execute_script(js)

time.sleep(5)
# 回到顶部
js = "window.scrollTo(0, 0)"
driver.execute_script(js)

# 滚动到元素出现的位置，把元素放到当前屏幕的最上方
ele = driver.find_element_by_link_text("新车")
driver.execute_script("arguments[0].scrollIntoView();", ele)



