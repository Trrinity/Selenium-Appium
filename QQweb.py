
#-*-coding:utf8-*-
from selenium import webdriver
#运行chrome，打开浏览器
import time

import win32gui
import win32con

driver =webdriver.Chrome()
#设置浏览器窗口
driver.set_window_size(1080,800)

#设置全局操作时间
driver.implicitly_wait(10)

#打开网址
driver.get('http://qzone.qq.com/')
time.sleep(3)

# 登录
driver.switch_to_frame("login_frame")
driver.find_element_by_link_text(u'帐号密码登录').click()
driver.find_element_by_id("u").send_keys("648323821")
driver.find_element_by_id("p").send_keys("lyt520")
driver.find_element_by_id("login_button").click()
time.sleep(5)

# # 点赞
# while True:
#     for i in driver.find_elements_by_css_selector('#fct_648323821_311_0_1497097640_0_1 > div.f-single-foot > div.f-op-detail.f-detail > p > a.item.qz_like_btn_v3 > i'):
#         i.click()
#         # 将页面滚动条拖动
#         js = "var q=document.body.scrollTop=10000"
#         driver.execute_script(js)
#         time.sleep(3)

# # 发表动态
# e1=driver.find_element_by_class_name('qz-poster-bd')
# e2=e1.find_element_by_xpath('//*[@id="$1_substitutor_content"]')
# time.sleep(5)
# e2.send_keys("      hihi")
# time.sleep(5)
# driver.find_element_by_link_text(u'发表').click()

# # 上传图片
# driver.find_element_by_link_text(u'相册').click()
# time.sleep(5)
# e1=driver.find_element_by_class_name('app_canvas_frame')
# driver.switch_to_frame(e1)
# driver.find_element_by_css_selector('#js-album-opbar-container > div.mod-tool-op > div:nth-child(1) > a').click()
# driver.switch_to.parent_frame()
# time.sleep(10)
#
# # driver.switch_to_frame('container')     no such frame
# driver.switch_to_frame('uploadtool_Flash_802')
# driver.find_element_by_link_text(u'选择图片').click()

# e1=driver.find_element_by_class_name('qz_dialog_layer')
# driver.switch_to_frame(e1)
# driver.find_element_by_id('uploadtool_Flash_9728').click()
#
# driver.switch_to_frame("app_canvas_frame")
# e1=driver.find_elements_by_id('app_container')
# driver.find_element_by_id('js-oper-createAlbum').click()   //新建相册

# e1.find_element_by_xpath('//*[@id="js-album-opbar-container"]/div[1]/div[1]/a').click()
# e1.find_element_by_class_name('gb-btn j-uploadentry-photo').click()
# driver.find_element_by_link_text(u'上传照片').click()

# time.sleep(3)
#
# driver.find_element_by_css_selector('js-album-list-noraml > div > div > ul > li > div > div.album-ft > div > div > a')
# driver.find_elements_by_id('js-album-opbar-container').click()
# driver.find_element_by_class_name('photo-op-item').click()
# driver.find_element_by_css_selector("#js-album-opbar-container>div.mod-tool-op>div:nth-child(1)").click()
# driver.find_element_by_link_text(u'选择图片').click()



# 上传图片
driver.find_element_by_link_text(u'相册').click()
time.sleep(5)
e1=driver.find_element_by_class_name('app_canvas_frame')
driver.switch_to_frame(e1)
driver.find_element_by_css_selector('#js-album-opbar-container > div.mod-tool-op > div:nth-child(1) > a').click()
driver.switch_to.parent_frame()
time.sleep(15)

# 手动点击'上传图片按钮'

uploadwindowname = u'打开'  # CHROME窗口名称是打开
uploadwindow = win32gui.FindWindow('#32770', uploadwindowname)  # 定位“文件上传 窗口
print uploadwindow
# 最后输出，如果输出0说明定位失败了
parent = win32gui.FindWindowEx(uploadwindow, None, 'ComboBoxEx32', None)
Combobox_real = win32gui.FindWindowEx(parent, None, 'ComboBox', None)
Edit_box = win32gui.FindWindowEx(Combobox_real, None, 'Edit', None)
# 这段代码是先定位到最上层的父窗口，再逐层定位到输入框（chrome于FF有所不同，FF下可以直接定位）
win32gui.SetForegroundWindow(Edit_box)
time.sleep(1)
win32gui.SendMessage(Edit_box, win32con.WM_SETTEXT, None, r'1.jpg') # 自己电脑的默认路径下是D盘
openbuttonname = u'打开(&O)'
time.sleep(1)
openbutton = win32gui.FindWindowEx(uploadwindow, None, "Button", openbuttonname)  # 定位“保存”按钮
print openbutton
win32gui.PostMessage(openbutton, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
win32gui.PostMessage(openbutton, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)
#
# dialog = win32gui.FindWindow('#32770', None)
# print dialog
#
# ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
# ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
# Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
# button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
#
# # 跟上面示例的代码是一样的，只是这里传入的参数不同，如果愿意可以写一个上传函数把上传功能封装起来
# win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, '"d:\\1.jpg"')
# win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
