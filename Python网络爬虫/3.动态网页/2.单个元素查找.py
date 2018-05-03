from selenium import webdriver
from selenium.webdriver.common.by import By

'''
下面这种方式是比较通用的一种方式：这里需要记住By模块所以需要导入
from selenium.webdriver.common.by import By
当然这种方法和上述的方式是通用的，browser.find_element(By.ID,"q")这里By.ID中的ID可以替换为其他几个
'''

browser = webdriver.Firefox()
browser.get("http://www.taobao.com")

input_first = browser.find_element(By.ID,"q")

print(input_first)

browser.close()

'''
# 这里我们通过三种不同的方式去获取响应的元素
# 第一种是通过id的方式
# 第二个中是CSS选择器
# 第三种是xpath选择器
# 结果都是相同的

input_first = browser.find_element_by_id("q")

input_second = browser.find_element_by_css_selector("#q")

input_third = browser.find_element_by_xpath('//*[@id="q"]')

print(input_first)
print(input_second)
print(input_third)

browser.close()

这里列举一下常用的查找元素方法：

find_element_by_name
find_element_by_id
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

'''