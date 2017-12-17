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
        desired_caps['appPackage']='com.tencent.mm'
        desired_caps['appActivity']='.ui.LauncherUI'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def quit(self):
        time.sleep(5)
        self.driver.quit()

    def test(self):
        # time.sleep(15)

        # 登录
        # el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("更多")')
        # el.click()
        # time.sleep(5)
        # el = self.driver.find_element_by_id('com.tencent.mm:id/fa')
        # el.click()
        # time.sleep(3)
        # el = self.driver.find_element_by_id('com.tencent.mm:id/brm')
        # el.send_keys('13763337544')
        # el = self.driver.find_element_by_id('com.tencent.mm:id/gr')
        # el.send_keys('lyt520')
        # el = self.driver.find_element_by_id('com.tencent.mm:id/aax')
        # el.click()
        # time.sleep(10)

        # 滑动
        time.sleep(15)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x / 2, y * 3 / 4, x / 2, y / 4, 150)
        time.sleep(3)
        self.driver.swipe(x / 2, y * 1 / 4, x / 2, y * 3 / 4, 150)
        time.sleep(3)
        self.driver.swipe(x * 3 / 4, y / 2, x / 4, y / 2, 150)
        time.sleep(3)
        self.driver.swipe(x / 4, y / 2, x * 3 / 4, y / 2, 150)
        time.sleep(3)

        # 加好友
        # el = self.driver.find_element_by_id('com.tencent.mm:id/f_').click()
        # el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("添加朋友")').click()
        # time.sleep(10)
        # el = self.driver.find_element_by_id('com.tencent.mm:id/gr').click()
        # time.sleep(5)
        # el = self.driver.find_element_by_id('com.tencent.mm:id/gr')
        # el.send_keys('13763337544')
        # time.sleep(5)
        # el = self.driver.find_element_by_id('com.tencent.mm:id/ho').click()
        # time.sleep(100)

        # 朋友圈点赞
        # self.driver.find_element_by_name(u'发现').click()
        # self.driver.find_element_by_name(u'朋友圈').click()
        # time.sleep(5)
        # while True:
        #     for i in self.driver.find_elements_by_id('com.tencent.mm:id/clj'):
        #         i.click()
        #         self.driver.find_element_by_id('com.tencent.mm:id/ckl').click()
        #         self.driver.swipe(x / 2, y * 3 / 4, x / 2, y / 4,150)
        #         time.sleep(2)

        # 群发消息
        # for i in range(0,4):
        #     self.driver.find_elements_by_id('com.tencent.mm:id/aft')[i].click()
        #     self.driver.find_element_by_class_name('android.widget.EditText').send_keys("test")
        #     self.driver.find_element_by_id('com.tencent.mm:id/a3h').click()
        #     self.driver.find_element_by_id('android:id/text1').click()

        # self.driver.find_elements_by_id('com.tencent.mm:id/aft')[2].send_keys('test')
        # self.driver.find_elements_by_id('com.tencent.mm:id/aft')[3].send_keys('test')
        # 群发消息
        self.driver.find_elements_by_id('com.tencent.mm:id/aft')[0].click()
        time.sleep(5)
        action1 = TouchAction(self.driver)
        el = self.driver.find_element_by_id('com.tencent.mm:id/if')
        action1.long_press(el).wait(10000).perform()
        time.sleep(5)
        self.driver.find_element_by_name(u'复制').click()
        time.sleep(5)
        self.driver.find_element_by_id('android:id/text1').click()
        self.driver.find_elements_by_id('com.tencent.mm:id/aft')[1].click()

        action2 = TouchAction(self.driver)
        el = self.driver.find_element_by_class_name('android.widget.EditText')
        action2.long_press(el).wait(10000).perform()
        time.sleep(1)
        #self.driver.find_element_by_id(u'粘贴').click()
        self.driver.find_elements_by_class_name('.tencent.mm:id/afu')[1].click()
        time.sleep(5)
        self.driver.find_element_by_id('com.tencent.mm:id/a3h').click()

if __name__ == '__main__':
     wechat = WechatTest()
     wechat.test()
