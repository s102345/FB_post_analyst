from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import random

def shareCrawer(driver, postUrl):
    driver.get(postUrl)
    sleep(random.uniform(3, 5))
    htmlText=driver.page_source
    beautifulSoup=BeautifulSoup(htmlText,'html.parser')
    shareText=beautifulSoup.find_all('div',class_='_43lx _55wr')
    return shareText

def shareProcess(shareText):
    shareAmount = ""
    shareText = str(shareText)
    scriptFlag = False 

    #處理網頁標籤
    for i in range(0, len(shareText)):
            #Priority 1 '<'
            if shareText[i] == '<':
                scriptFlag = True

            #Priority 2 '>'
            elif shareText[i] == '>':
                scriptFlag = False
            
            #Priority 3 isIn "<>"
            elif scriptFlag:
                pass

            #Infomation collect
            else:
                shareAmount += shareText[i] 
    
    #取出數字
    strTemp = ""
    for i in range(0, len(shareAmount)):
        if shareAmount[i] <= '9' and shareAmount[i] >= '0':
            strTemp += shareAmount[i]

    shareAmount = strTemp
    return shareAmount

def getShareAmount(driver, postUrl):
    shareText = shareCrawer(driver, postUrl)
    shareAmount = shareProcess(shareText)
    return shareAmount