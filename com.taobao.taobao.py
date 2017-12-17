#-*-coding:utf8-*-
from appium import webdriver
import time

class WechatTest():
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] ='4.4.2'
        desired_caps['deviceName']='Android Emulator'
        desired_caps['appPackage']='com.taobao.taobao'
        desired_caps['appActivity']='com.taobao.android.trade.cart.CartActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def quit(self):
        time.sleep(5)
        self.driver.quit()

    def test_login(self):
        time.sleep(35)
        self.driver.find_element_by_name(u'购物车').click()
        time.sleep(35)
        self.driver.find_element_by_name(u'LOVEHEYNEW').click()
        time.sleep(15)
        self.driver.find_element_by_name(u'微淘动态').click()
        time.sleep(10)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x / 2, y * 3 / 4, x / 2, y / 4, 150)
        time.sleep(10)
        self.driver.swipe(x / 2, y * 3 / 4, x / 2, y / 4, 150)
        time.sleep(5)

        self.driver.find_elements_by_class_name('android.view.View')[12].click()
        time.sleep(5)
        self.driver.find_element_by_name('回复楼主').send_keys("1")
        self.driver.find_elements_by_class_name('android.view.View')[3].click()
        time.sleep(5)





if __name__ == '__main__':

     wechat = WechatTest()
     wechat.test_login()
