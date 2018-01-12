#-*-coding:utf8-*-
import time
from selenium import webdriver

#运行chrome，打开浏览器
driver =webdriver.Chrome()
#设置浏览器窗口
driver.set_window_size(1080,800)

#设置全局操作时间
driver.implicitly_wait(10)

#打开网址
driver.get('https://kyfw.12306.cn/otn')
time.sleep(5)

driver.find_element_by_id("username").click()
driver.find_element_by_id("username").send_keys("522268397@qq.com")
driver.find_element_by_id("password").send_keys("lyt520")
print("continue")
time.sleep(15)

driver.find_element_by_link_text("车票预订").click()
time.sleep(5)
#出发地选择
driver.find_element_by_id("fromStationText").click()
# setTimeout(function(){debugger;}, 5000)
driver.find_element_by_css_selector(u"[title=广州]").click()

time.sleep(5)
#目的地选择
driver.find_element_by_id("toStationText").click()
driver.find_element_by_css_selector(u"[title=北京]").click()
time.sleep(5)

#出发日期选择
driver.find_element_by_id("train_date").click()
driver.find_element_by_css_selector("body > div.cal-wrap > div:nth-child(1) > div.cal-cm > div:nth-child(24) > div").click()
time.sleep(5)

#车型选择
driver.find_element_by_css_selector("#_ul_station_train_code > li:nth-child(1) > label").click()
time.sleep(5)

#查询

driver.find_element_by_id("query_ticket").click()
e=driver.find_element_by_id("SWZ_6i00000G8009")
time.sleep(5)
e.click()

print(e.text)

while True:
    try:
        driver.find_element_by_id("query_ticket").click()
        e=driver.find_element_by_id("SWZ_6i00000G8009")
        e.click()
        if e.text in [u'无','--']:
            print ("nono")
            time.sleep(1)
        else:
            print("yes")
    except:
        pass



    # def setUp(self):
    #     # 定义启动设备需要的参数
    #     desired_caps = {}
    #     # 设备系统
    #     desired_caps['platformName'] = 'Android'
    #     # 设备系统版本号
    #     desired_caps['platformVersion'] = '5.1.2'
    #     # 设备名称
    #     desired_caps['deviceName'] = 'MI 3'
    #     # 要测试的应用的地址
    #     desired_caps['app'] = '<span style="color:#ff0000;background-color: rgb(255, 0, 0);">C:\\Users\\Administrator\\Desktop\\123456\\moer.apk</span>'
    #     # 应用的包名
    #     # desired_caps['appPackage'] = 'com.moer.moerfinance'
    #     # desired_caps['appActivity'] = 'com.moer.moerfinance.advertisement.AdvertisementActivity'
    #     # 启动app
    #     self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
