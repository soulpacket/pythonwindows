#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()#打开浏览器
driver.get("http://www.python.org")#打开url
assert "Python" in driver.title
elem = driver.find_element_by_name("q")#寻找搜索框
elem.send_keys("pycon")#像框中输入
driver.find_element_by_name("submit").click()#点击按钮go
#driver.back()#让页面后退/.forward()是让页面前进
#driver.switch_to_window("windowName")#一个浏览器肯定会有很多窗口，所以我们肯定要有方法来实现窗口的切换。切换窗口的方法如下
#elem.send_keys(Keys.RETURN)#点击回车
#driver.add_cookie(cookie)#添加cookie，是字典形式
#driver.get_cookies()#得到cookie
#elem.clear()#清空输入的文本
print driver.page_source