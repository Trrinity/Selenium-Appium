#-*-coding:utf8-*-
import time
from selenium import webdriver
driver =webdriver.Chrome()

#运行chrome，打开浏览器
driver =webdriver.Chrome()
#设置浏览器窗口
driver.set_window_size(1080,800)

#设置全局操作时间
driver.implicitly_wait(10)

#打开网址
driver.get('https://kyfw.12306.cn/otn')
driver.find_element_by_id("login_user").click()
driver.find_element_by_id("username").send_keys("522268397@qq.com")
driver.find_element_by_id("password").send_keys("lyt520")
print("continue")

time.sleep(5)

driver.find_element_by_link_text("车票预订").click()

#出发地选择
driver.find_element_by_id("fromStationText").click()
driver.find_element_by_css_selector(u"[title=广州]").click()


#目的地选择
driver.find_element_by_id("toStationText").click()
driver.find_element_by_css_selector(u"[title=北京]").click()

#出发日期选择
driver.find_element_by_id("train_date").click()
driver.find_element_by_css_selector("body > div.cal-wrap > div:nth-child(1) > div.cal-cm > div:nth-child(18) > div").click()



#车型选择
driver.find_element_by_css_selector("#_ul_station_train_code > li:nth-child(1) > label").click()

#查询

driver.find_element_by_id("query_ticket").click()
e=driver.find_element_by_id("SWZ_6c00000G680B")

e.click()
print(e.text)

#购票
driver.find_element_by_link_text("预订").click()

#乘车人选择
driver.find_element_by_css_selector("#normal_passenger_id > li:nth-child(1) > label").click()

#学生票确认（不是学生可去掉）
driver.find_element_by_link_text("确认").click()

#提交订单
driver.find_element_by_link_text("提交订单").click()

driver.find_element_by_link_text("确认").click()