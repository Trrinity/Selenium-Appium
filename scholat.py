#-*-coding:utf8-*-
from selenium import webdriver
#运行chrome，打开浏览器
driver =webdriver.Chrome()
#设置浏览器窗口
driver.set_window_size(1080,800)

#设置全局操作时间
driver.implicitly_wait(10)

#打开网址
driver.get('http://www.scholat.com/login.html')
driver.find_element_by_css_selector("#j_username").send_keys("shannon")
driver.find_element_by_css_selector("#j_password_ext").send_keys("miemie111")
driver.find_element_by_id("login").click()
print("continue")



driver.find_element_by_css_selector("#t7 > p").click()
driver.find_element_by_css_selector("#toolpicList > li:nth-child(4) > a").click()



driver.find_element_by_id("ChineseName").send_keys(u"Mirajane")
driver.find_element_by_id("workUnit").send_keys("gdufe")
driver.find_element_by_id("workEmail").send_keys("522268397@qq.com")

driver.find_element_by_link_text("邀请好友注册")



