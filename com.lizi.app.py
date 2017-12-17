from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] ='4.4.2'
desired_caps['deviceName']='Android Emulator'
desired_caps['appPackage']='com.lizi.app'
desired_caps['appActivity']='com.lizi.app.activity.LiziSplash'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_id("com.lizi.app:id/tab_mylizi_tv").click()
driver.find_element_by_id("com.lizi.app:id/user_login_iv").click()
driver.find_element_by_id("com.lizi.app:id/zhanghao_edittext").send_keys("15017566304")
driver.find_element_by_id("com.lizi.app:id/password_edittext").send_keys("donghaoye")
driver.find_element_by_id("com.lizi.app:id/login_button").click()

# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] ='4.4.2'
# desired_caps['deviceName']='Android Emulator'
# desired_caps['appPackage']='com.example.helloworld'
# desired_caps['appActivity']='MainActivity'
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
# driver.find_element_by_id("com.example.calculator:id/button5").click()
# driver.find_element_by_id("com.example.calculator:id/button2").click()
# driver.find_element_by_id("com.example.calculator:id/zero").click()
# driver.find_element_by_id("com.example.calculator:id/qingchu").click()
# driver.find_element_by_id("com.example.calculator:id/button1").click()
# driver.find_element_by_id("com.example.calculator:id/doublezero").click()
#
# driver.find_element_by_id("com.example.calculator:id/jia").click()
#
# driver.find_element_by_id("com.example.calculator:id/button2").click()
# driver.find_element_by_id("com.example.calculator:id/doublezero").click()
#
# driver.find_element_by_id("com.example.calculator:id/deng").click()


