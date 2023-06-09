from selenium import webdriver
import sys
import datetime
import time
import calendar
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



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
day = time.strftime("%d",time.localtime())
day = int(day)
flag = False
if (day == cal[1]):
  flag = True  
  r = 1
  month += 1
  cal = calendar.monthrange(year, month)
  c = cal[0] + 1
  timelocation = '/html/body/div[6]/table/tbody/tr[' + str(r) + ']/td[' + str(c) + ']/a'
else:
  if(day > (7 - i)):
    i = 7 - i
    day = day - i
    r = day // 7 + 2
    c = day % 7 + 1
  elif(day == (7-i)):
    r = 2
    c = 1
  else:
    r = 1
    c = i + day + 1
  timelocation = '/html/body/div[6]/table/tbody/tr[' + str(r) + ']/td[' + str(c) + ']/a'


#open图书馆预约系统
driver.get('webaddress')
'''
考虑到网页打开的速度取决于每个人的电脑和网速，
使用time库sleep()方法，让程序睡眠5秒
'''


#在主页面点击登录按钮，进入登录页面
#driver.find_element_by_xpath('//*[@id="username"]').click()
#输入账号和密码
login_btn=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
login_btn.send_keys('username')
login_btn=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
login_btn.send_keys('password')
#点击登录按钮
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="casLoginForm"]/div[4]/div/button'))).click()
#选择楼层
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item_list"]/ul/li[4]/a'))).click()

#选择自习室（206永远的神）

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item_list"]/ul/li[4]/ul/li/a/span'))).click()
#选择预约日期

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/input'))).click()

if (flag == True):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/a[2]/span'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, timelocation))).click()


#choice time
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/span[2]/input[1]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[2]/dl/dd[2]/div/select'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-datepicker-div"]/div[2]/dl/dd[2]/div/select/option[2]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-datepicker-div"]/div[3]/button[2]'))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/span[2]/input[2]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[2]/dl/dd[2]/div/select'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-datepicker-div"]/div[2]/dl/dd[2]/div/select/option[8]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-datepicker-div"]/div[3]/button[2]'))).click()



#选择座位（122永远的神）

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/div[3]/div[60]'))).click()
#选择具体预约时间（上午场）

'''select_loc = (By.XPATH, '//select[@name="ft"]')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(select_loc))
ele = driver.find_element(*select_loc)


element = driver.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/span[2]/input[1]')
webdriver.ActionChains(driver).move_to_element(element).click().perform()

Select(driver.find_element_by_class_name("ui-timepicker-select")).select_by_value("8")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-datepicker-div"]/div[3]/button[2]'))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/span[2]/input[2]')))
element = driver.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/span[2]/input[2]')
webdriver.ActionChains(driver).move_to_element(element).click().perform()


Select(driver.find_element_by_class_name("ui-timepicker-select")).select_by_value("14")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-datepicker-div"]/div[3]/button[2]'))).click()'''
#提交预约信息
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[2]/form/div[2]/input[1]'))).click()


#返回
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[3]/div/button[2]/span'))).click()


'''
#再次预约（下午场）
#选择预约日期
driver.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/input').click()

if (flag == True):
    driver.find_element_by_xpath('/html/body/div[6]/div/a[2]/span').click()
driver.find_element_by_xpath(timelocation).click()


#选择座位（122永远的神）
driver.find_element_by_xpath('//*[@id]/div/div[2]/div[3]/div[6]').click()

#选择具体预约时间
driver.find_element_by_xpath('//*[@id]/form/div[1]/table/tbody[2]/tr[2]/td[2]/div/span[1]/select[1]/option[32]').click()

driver.find_element_by_xpath('//*[@id]/form/div[1]/table/tbody[2]/tr[2]/td[2]/div/span[3]/select/option[165]').click()
#提交预约信息

driver.find_element_by_xpath('/html/body/div[9]/div[2]/form/div[2]/input[1]').click()

#返回
driver.find_element_by_xpath('/html/body/div[9]/div[3]/div/button[2]/span').click()



#再次预约（夜晚场）
#选择预约日期
driver.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/input').click()

if (flag == True):
    driver.find_element_by_xpath('/html/body/div[6]/div/a[2]/span').click()
driver.find_element_by_xpath(timelocation).click()


#选择座位（122永远的神）
driver.find_element_by_xpath('//*[@id]/div/div[2]/div[3]/div[6]').click()

#选择具体预约时间
driver.find_element_by_xpath('//*[@id]/form/div[1]/table/tbody[2]/tr[2]/td[2]/div/span[1]/select[1]/option[33]').click()
#提交预约信息

driver.find_element_by_xpath('/html/body/div[9]/div[2]/form/div[2]/input[1]').click()

#返回
driver.find_element_by_xpath('/html/body/div[9]/div[3]/div/button[2]/span').click()
'''



endtime = datetime.datetime.now()
#计算程序运行的时间
print (endtime - starttime)
diff = endtime - starttime    
print("Workdone!")
driver.quit()
