#!-*- coding:utf-8 -*-
import os
import requests
from io import BytesIO
from pyzbar import pyzbar
from PIL import Image, ImageEnhance
from selenium import webdriver
import sys
import datetime
import time
import calendar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def is_driver(no_ui=False):
    '''
    1、判断是在什么环境下运行
    2、no_ui win系统下默认为界面模式，无界面设为：True
    '''
    if 'linux' in sys.platform:
        option = webdriver.ChromeOptions()
        option.add_argument('headless') # 浏览器不提供可视化页面
        option.add_argument('no-sandbox') # 以最高权限运行
        option.add_argument('--start-maximized') # 最大化运行（全屏窗口）设置元素定位比较准确
        option.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
        # option.add_argument('--window-size=1920,1080') # 设置浏览器分辨率（窗口大小）
        driver = webdriver.Chrome(options=option)
    else:
        if no_ui:
            ''' win系统下无界面模式 '''
            option = webdriver.ChromeOptions()
            option.add_argument('headless') # 浏览器不提供可视化页面
            option.add_argument('--start-maximized') # 最大化运行（全屏窗口）设置元素定位比较准确
            driver = webdriver.Chrome(chrome_options=option)
        else:
            driver = webdriver.Chrome()
            driver.maximize_window() # 将浏览器最大化
    return driver
driver = is_driver()


img = Image.open('img-address')   #The QR Code on the seat.
txt_list = pyzbar.decode(img)

for txt in txt_list:
    barcodeData = txt.data.decode("utf-8")

driver.get(barcodeData)
# time.sleep(2)
# 在主页面点击登录按钮，进入登录页面
# driver.find_element("xpath", '//*[@id="username"]').click()
# 输入账号和密码
ele = WebDriverWait(driver, 60).until(lambda _: driver.find_element(By.XPATH, '//*[@id="username"]'))
ele.send_keys('username')
ele = WebDriverWait(driver, 60).until(lambda _: driver.find_element(By.XPATH, '//*[@id="password"]'))
ele.send_keys('password')
# 点击登录按钮(pation attention: no sleep!)
driver.find_element("xpath", '//*[@id="casLoginForm"]/div[4]/div/button').click()
#点击签到
ele = WebDriverWait(driver, 60).until(lambda _: driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[4]/button'))
ele.click()

requests.get('bark-api-key/OrderLibrary/The library study seat(124) has been successfully signed in!')
print("Workdone!")
