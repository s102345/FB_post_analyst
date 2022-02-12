from selenium import webdriver #瀏覽器載體
from webdriver_manager.chrome import ChromeDriverManager #driver自動更新
from time import sleep #緩衝
import random
import json #開啟使用者資料

def loginAccount(driver):
    #目的：登入Facebook帳號 
    #輸入：瀏覽器載體
    #輸出：瀏覽器載體
    driver.maximize_window()
    driver.get('https://mobile.facebook.com/')

    with open(r'./data/user_data.json','r') as data:
        userData=json.load(data)

    myUserId=userData['myUserId']
    myPassword=userData['myUserPassword']

    userId=driver.find_element_by_name('email')
    userId.send_keys(myUserId)
    sleep(random.uniform(3, 5))
    password=driver.find_element_by_name('pass')
    password.send_keys(myPassword)
    sleep(random.uniform(3, 5))
    login=driver.find_element_by_name('login')
    login.click()
    sleep(random.uniform(3, 5))
    return driver

def initialize():
    #目的：整合登入與關閉通知功能，以達成初始化之效果
    #輸入：無
    #輸出：瀏覽器載體 
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = closeNotifyWindow(driver)
    driver = loginAccount(driver)
    return driver

if __name__=='__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = closeNotifyWindow(driver)
    driver = loginAccount(driver)

#Reference:
#https://selenium-python.readthedocs.io/locating-elements.html#locating-elements-by-class-name
#https://gist.github.com/HaoHsiu-Huang/f4a68bec77c17e0e118a6a5cb4dffed1