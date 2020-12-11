import unittest
from common import HTMLTestRunner_cn

# 用例的路径
casePath = "E:\web_auto\\case"
# 用例的匹配规则
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

# 执行测试用例时直接用TestRunner框架，可以生成html测试报告，html是HTMLTestRunner里面的

reportPath = "E:\web_auto\\report\\"+"result.html"   # 测试报告：路径+文件名

fp = open(reportPath,"wb")

runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                       title="报告的title",
                                       description="描述你的报告干什么用",
                                        retry=1)
                                       # 针对失败的用例retry重跑一次，通过的用例不重跑，失败可能是其他原因，如网络异常

runner.run(discover)
fp.close()  # 关闭测试报告，回收内存，否则代码多的时候会影响性能，要养成关闭的习惯


