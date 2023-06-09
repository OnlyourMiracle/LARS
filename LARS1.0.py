from selenium import webdriver
import sys
import datetime
import time
import calendar


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
year = int(year)
month = int(month)
cal = calendar.monthrange(year, month)
i = cal[0]
i = 7 - i
day = time.strftime("%d",time.localtime())
day = int(day)
day = day - i
r = day // 7 + 2
c = day % 7 + 1
timelocation = '/html/body/div[6]/table/tbody/tr[' + str(r) + ']/td[' + str(c) + ']/a'


#打开图书馆预约系统
driver.get('webaddress')
'''
考虑到网页打开的速度取决于每个人的电脑和网速，
使用time库sleep()方法，让程序睡眠5秒
'''
time.sleep(5)
#在主页面点击登录按钮，进入登录页面
#driver.find_element_by_xpath('//*[@id="username"]').click()
#输入账号和密码
driver.find_element_by_xpath('//*[@id="username"]').send_keys('username')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('password')
#点击登录按钮
driver.find_element_by_xpath('//*[@id="casLoginForm"]/div[4]/div/button').click()
time.sleep(5)
#选择楼层
driver.find_element_by_xpath('//*[@id="item_list"]/ul/li[2]/a').click()
time.sleep(2)
#选择自习室（206永远的神）
driver.find_element_by_xpath('//*[@id="item_list"]/ul/li[2]/ul/li[4]/a/span').click()
time.sleep(10)
#选择预约日期
driver.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/input').click()
time.sleep(1)
driver.find_element_by_xpath(timelocation).click()
time.sleep(2)
#选择座位（122永远的神）
driver.find_element_by_xpath('//*[@id]/div/div[2]/div[3]/div[122]').click()
time.sleep(5)
#选择具体预约时间（上午场）
driver.find_element_by_xpath('//*[@id]/form/div[1]/table/tbody[2]/tr[2]/td[2]/div/span[1]/select[1]/option[31]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id]/form/div[1]/table/tbody[2]/tr[2]/td[2]/div/span[3]/select/option[121]').click()
#提交预约信息
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[8]/div[2]/form/div[2]/input[1]').click()
time.sleep(2)
#返回
driver.find_element_by_xpath('/html/body/div[9]/div[3]/div/button[2]/span').click()
time.sleep(6)

#再次预约（下午场）
#选择预约日期
driver.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/input').click()
time.sleep(1)
driver.find_element_by_xpath(timelocation).click()
time.sleep(2)
#选择座位（122永远的神）
driver.find_element_by_xpath('//*[@id]/div/div[2]/div[3]/div[122]').click()
time.sleep(6)
#选择具体预约时间
driver.find_element_by_xpath('//*[@id]/form/div[1]/table/tbody[2]/tr[2]/td[2]/div/span[1]/select[1]/option[32]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id]/form/div[1]/table/tbody[2]/tr[2]/td[2]/div/span[3]/select/option[165]').click()
#提交预约信息
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[9]/div[2]/form/div[2]/input[1]').click()
time.sleep(2)
#返回
driver.find_element_by_xpath('/html/body/div[9]/div[3]/div/button[2]/span').click()
time.sleep(5)

#再次预约（夜晚场）
#选择预约日期
driver.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/input').click()
time.sleep(1)
driver.find_element_by_xpath(timelocation).click()
time.sleep(2)
#选择座位（122永远的神）
driver.find_element_by_xpath('//*[@id]/div/div[2]/div[3]/div[122]').click()
time.sleep(5)
#选择具体预约时间
driver.find_element_by_xpath('//*[@id]/form/div[1]/table/tbody[2]/tr[2]/td[2]/div/span[1]/select[1]/option[33]').click()
#提交预约信息
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[9]/div[2]/form/div[2]/input[1]').click()
time.sleep(2)
#返回
driver.find_element_by_xpath('/html/body/div[9]/div[3]/div/button[2]/span').click()

time.sleep(5)
endtime = datetime.datetime.now()
#计算程序运行的时间
print (endtime - starttime)
print("Workdone!")
