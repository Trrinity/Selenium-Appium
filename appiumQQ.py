#-*-coding:utf8-*-
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

class WechatTest():
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] ='4.4.2'
        desired_caps['deviceName']='Android Emulator'
        desired_caps['appPackage']='com.tencent.mobileqq'
        desired_caps['appActivity']='.activity.LoginActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test(self):
        time.sleep(8)
        # 登录
        self.driver.find_element_by_id('com.tencent.mobileqq:id/input').send_keys("648323821")
        self.driver.find_element_by_id('com.tencent.mobileqq:id/password').send_keys("lyt520")
        self.driver.find_element_by_id('com.tencent.mobileqq:id/login').click()
        time.sleep(5)


        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print x, y

        while True:
            for i in self.driver.find_elements_by_class_name('android.widget.ImageView'):
                i.click()
                self.driver.find_elements_by_class_name('android.widget.ImageView')[2].click()
                self.driver.swipe(x / 2, y * 3 / 4, x / 2, y / 4, 150)
                time.sleep(2)


        # 加好友
        self.driver.find_element_by_id('com.tencent.mobileqq:id/et_search_keyword').send_keys("522268397")
        time.sleep(8)
        self.driver.find_element_by_id('com.tencent.mobileqq:id/image').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.tencent.mobileqq:id/txt').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.tencent.mobileqq:id/ivTitleBtnRightText').click()
        time.sleep(3)

        #
        # # 聊天
        # self.driver.find_element_by_id('com.tencent.mobileqq:id/relativeItem')
        # time.sleep(5)
        # self.driver.find_elements_by_class_name('android.widget.LinearLayout')[2].click()
        # time.sleep(5)
        # action1 = TouchAction(self.driver)
        # el = self.driver.find_element_by_class_name('android.widget.FrameLayout')
        # action1.long_press(el).wait(10000).perform()
        # time.sleep(5)


        # self.driver.swipe(x / 2, y * 3 / 4, x / 2, y / 4)
        # self.driver.find_element_by_name(u'转发').click()
        # time.sleep(5)
        # # question
        # self.driver.find_element_by_id('com.tencent.mobileqq:id/text1').click()

        # 空间说说
        self.driver.find_element_by_name(u'动态').click()
        time.sleep(5)
        self.driver.find_element_by_name(u'好友动态').click()
        time.sleep(5)
        self.driver.find_element_by_name(u'说说').click()
        time.sleep(5)
        self.driver.find_element_by_name(u'写说说').click()
        time.sleep(5)
        self.driver.find_elements_by_class_name('android.widget.EditText')[0].send_keys("hihi")
        time.sleep(3)
        self.driver.find_element_by_name(u'发表').click()
        time.sleep(3)

        # 空间点赞
        # self.driver.find_element_by_name(u'动态').click()
        # time.sleep(5)
        # self.driver.find_element_by_name(u'好友动态').click()
        # time.sleep(5)
        #
        # x = self.driver.get_window_size()['width']
        # y = self.driver.get_window_size()['height']
        # self.driver.swipe(x / 2, y * 3 / 4, x / 2, y / 4,150)
        # time.sleep(2)
        # self.driver.find_elements_by_class_name('android.widget.ImageView')[2].click()
        #
        # while True:
        #   for i in range(1,3):
        #       self.driver.find_elements_by_class_name('android.widget.ImageView')[2].click()
        #       self.driver.swipe(x / 2, y * 3 / 4, x / 2, y / 4, 150)
        #       time.sleep(2)



        # 图片上传
        #　self.driver.find_elements_by_class_name('android.widget.LinearLayout')[3].click()
        #　time.sleep(5)

if __name__ == '__main__':
     wechat = WechatTest()
     wechat.test()
