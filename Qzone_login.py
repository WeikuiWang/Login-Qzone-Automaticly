# -*- coding: utf-8 -*-
from selenium import webdriver
# open the Firefox explore(打开火狐浏览器)
driver = webdriver.Firefox()
#maximize the window(浏览器窗口最大化)
driver.maximize_window()
#get the url （获取qq空间登录地址）
driver.get("http://qzone.qq.com")
#switch to the login frame(定位到登录面板)
driver.switch_to_frame("login_frame")
#login by account instead of scanning QR code(以账号方式登录)
driver.find_element_by_id("switcher_plogin").click()
#input your own qq account(该行最后双引号内改为自己的qq账号)
driver.find_element_by_id("u").send_keys("your qq account")
#input your password(该行最后双引号内改为自己的qq登录密码)
driver.find_element_by_id("p").send_keys("your password")
#click the login button(自动点击登录按钮)
driver.find_element_by_id("login_button").click()
