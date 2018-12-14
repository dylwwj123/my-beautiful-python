from selenium import webdriver

# 声明浏览器对象
driver = webdriver.Firefox()
driver.get("http://www.baidu.com/")
# 打印网页源代码
print(driver.page_source)
#关闭浏览器
driver.close()