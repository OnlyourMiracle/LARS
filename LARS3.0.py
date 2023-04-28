from selenium import webdriver
import sys
import datetime
import time
import calendar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import requests
from cnocr import CnOcr

starttime = datetime.datetime.now()
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


#获取时间戳
year = time.strftime("%Y",time.localtime())
month = time.strftime("%m",time.localtime())
day = time.strftime("%d", time.localtime())
year = int(year)
month = int(month)
day = int(day)
day = day + 1
date = str(year) + '-' + str(month) + '-' + str(day)
print(date)

driver.get('webaddress')

'''
考虑到网页打开的速度取决于每个人的电脑和网速，
使用time库sleep()方法，让程序睡眠5秒
'''
#time.sleep(2)
#在主页面点击登录按钮，进入登录页面
#driver.find_element("xpath", '//*[@id="username"]').click()
#输入账号和密码
ele = WebDriverWait(driver, 20).until(lambda _: driver.find_element(By.XPATH, '//*[@id="username"]'))
ele.send_keys('username')
ele = WebDriverWait(driver, 20).until(lambda _: driver.find_element(By.XPATH, '//*[@id="password"]'))
ele.send_keys('password')
#点击登录按钮(pation attention: no sleep!)
driver.find_element("xpath", '//*[@id="casLoginForm"]/div[4]/div/button').click()


#选择座位预约
ele = WebDriverWait(driver, 60).until(lambda _: driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[1]/ul/li[2]'))
time.sleep(1)
ele.click()

#选择校区
ele1 = WebDriverWait(driver, 15).until(lambda _: driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[1]/ul/li[2]/ul/div/li[1]'))
time.sleep(1)
ele1.click()

#选择楼层
ele1 = WebDriverWait(driver, 15).until(lambda _: driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[1]/ul/li[2]/ul/div/li[1]/ul/div/li[2]'))
time.sleep(1)
ele1.click()

#滚动页面至底部
js = "window.scrollTo(0,8000)"
driver.execute_script(js)

#选择自习室B206
ele1 = WebDriverWait(driver, 15).until(lambda _: driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[1]/ul/li[2]/ul/div/li[1]/ul/div/li[2]/ul/div/li[4]'))
time.sleep(1)
ele1.click()

#Morning
#选择预约日期
ele2 = WebDriverWait(driver, 15).until(lambda _: driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/section/div[1]/input'))
ele2.click()

ele = WebDriverWait(driver, 20).until(lambda _: driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/section/div[1]/input'))
ele.clear()
ele.send_keys(date)

#选择预约时间
ele2 = WebDriverWait(driver, 10).until(lambda _: driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/section/span/div[1]'))
time.sleep(1)
ele2.click()

ele4 = WebDriverWait(driver, 10).until(lambda _: driver.find_element(By.XPATH, '/html/body/div[@class="el-select-dropdown el-popper"]/div[1]/div[1]/ul/li[3]'))
time.sleep(1)
ele4.click()

#滚动页面至底部
js = "window.scrollTo(0,8000)"
driver.execute_script(js)

#选择座位（123)
ele5 = WebDriverWait(driver, 10).until(lambda _: driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[123]'))
time.sleep(1)
ele5.click()


#sleep
te = datetime.datetime.now().strftime("%H %M %S")
te = te.split()
if(int(te[0]) < 7):
  min = int(te[1])
  sec = int(te[2])
  sleeptime = (60 - min -1) * 60 + 60 - sec
  time.sleep(sleeptime)
  print(sleeptime)
  print(te)

#print submit time
te = datetime.datetime.now().strftime("%H %M %S")
te = te.split()
print(te)

driver.get_screenshot_as_file('/root/Python/OrderLibrary/1_0.png')

#提交预约信息
ele8 = WebDriverWait(driver, 10).until(lambda _: driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div/div[3]/span/button[1]'))
ele8.click()
driver.get_screenshot_as_file('/root/Python/OrderLibrary/1_1.png')
time.sleep(2)
driver.get_screenshot_as_file('/root/Python/OrderLibrary/1_2.png')

'''
#返回
ele9 = WebDriverWait(driver, 10).until(lambda _: driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[3]/div/div/div[3]/span/button[1]'))
time.sleep(2)
ele9.click()

driver.get_screenshot_as_file('/root/Python/OrderLibrary/1_2.png')
'''

ocr = CnOcr()
res = ocr.ocr('/root/Python/OrderLibrary/1_2.png')

for i in range(len(res)):
    if res[i]['text'] == "预约提交成功":
        requests.get('bark-api-key/OrderLibrary/The library study seat(123-A) has been successfully reserved for you!')

endtime = datetime.datetime.now()
#计算程序运行的时间
print (endtime - starttime)
print("Workdone!")
driver.quit()
