#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-05-24 10:10:50
# @Last Modified by:   anchen
# @Last Modified time: 2018-06-07 14:21:28

import time
from selenium import webdriver
import xlrd
from selenium.webdriver.common.keys import Keys

def count(n):
    starttime=time.time()
    data = xlrd.open_workbook('D:/ceshie.xlsx')
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    list = []
    for i in range(n,n+1):
        for j in range(4,13):#第N列
            if i==0:
                continue
            x=table.row_values(i)[j]
            if j==11:
                x=int(x)
            list.append(x)

    #运行chrome，打开浏览器
    driver =webdriver.Chrome()
    #设置浏览器窗口
    driver.set_window_size(1080,800)

    #设置全局操作时间
    driver.implicitly_wait(10)

    #打开网址
    driver.get('http://cmdb.sec.yooli.com/')
    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[1]/input").send_keys("LIYANTING")
    driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[2]/input").send_keys("miemie111")
    driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[2]/input").send_keys(Keys.ENTER)
    driver.find_element_by_xpath("/html/body/div/aside[1]/div/nav/ul/li[2]/a").send_keys(Keys.ENTER)
    driver.find_element_by_link_text(u'新增资产').click
    time.sleep(2)

    try:
        driver.find_element_by_xpath("//*[@id=\"ipinput\"]/input").send_keys(list[0])
        driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div[2]/div/div[2]/form/div[2]/input").send_keys(list[1])
        driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div[2]/div/div[2]/form/div[3]/input").send_keys(list[2])
        driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div[2]/div/div[2]/form/div[4]/input").send_keys(list[3])
        driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div[2]/div/div[2]/form/div[5]/input").send_keys(list[4])
        driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div[2]/div/div[2]/form/div[6]/input").send_keys(list[5])
        driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div[2]/div/div[2]/form/div[7]/input").send_keys(list[6])
        driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div[2]/div/div[2]/form/div[8]/input").send_keys(list[7]) #???/
        driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div[2]/div/div[2]/form/div[9]/input").send_keys(list[8])
        driver.find_element_by_xpath("/html/body/div/div/section[2]/div/div[2]/div/div[2]/form/button").send_keys(Keys.ENTER)
        usetime=time.time()-starttime
        print usetime
        print "success"

    catch:


if __name__ == '__main__':
    for i in range(101,106):
        count(i)
        print i