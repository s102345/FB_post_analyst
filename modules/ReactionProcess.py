from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import random

def getIdentifierUrl(url):
    identifier = ""
    for i in range(url.find('posts'), len(url)):
        if(url[i] >= '0' and url[i] <= '9'):
            identifier += url[i]
    identifierUrl = "https://mobile.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=" + identifier
    
    return identifierUrl

def reactionCrawer(driver, postUrl):
    #postUrl = input('請輸入欲查詢的文章網址：')
    postUrl = getIdentifierUrl(postUrl)
    driver.get(postUrl)
    sleep(random.uniform(3, 5))
    htmlText = driver.page_source
    beautifulSoup = BeautifulSoup(htmlText,'html.parser')
    reactionText = beautifulSoup.find_all('div',class_='scrollAreaColumn')
    return reactionText

def reactionProcess(reactionText):
    scriptFlag = False 
    reactionAmount = []
    strTemp = ""
    reactionText = str(reactionText)
    #反應數量
    for i in range(1, len(reactionText)):
        #Priority 1 '<'
        if reactionText[i] == '<':
            #不為空
            if(strTemp != ""):
                reactionAmount.append(strTemp)

            strTemp = ""
            scriptFlag = True

        #Priority 2 '>'
        elif reactionText[i] == '>':
            scriptFlag = False
            
        #Priority 3 isIn "<>"
        elif scriptFlag:
            pass

        #Infomation collect
        else:
            if(reactionText[i] >= '0' and reactionText[i] <= '9'):
                strTemp += reactionText[i] 

    #反應符號 讚、怒
    reactionSymbol = ["all"]
    reactionPointer = 0

    while(reactionText.find('reactionType', reactionPointer + 1) != -1):
        reactionPointer = reactionText.find('reactionType', reactionPointer + 1)
        strTemp = ""
        for i in range(reactionPointer, len(reactionText)):
            if(reactionText[i] == '}'):
                break
            elif (reactionText[i] >= '0' and reactionText[i] <= '9'):
                strTemp += reactionText[i]
        
        if(strTemp != ""):
            reactionSymbol.append(strTemp)

    #弄成dict
    reactionInfo = dict()

    reactionNumToText = {'1': '讚', '16': '加油', '8': '怒', '4': '哈', '7': '嗚', '2': '大心', '3': '哇', 'all': '全部'}

    for i in range(0, min(len(reactionSymbol), len(reactionAmount))):
        reactionInfo[reactionNumToText[reactionSymbol[i]]] = reactionAmount[i]

    return reactionInfo

def getReactionInfo(driver, postUrl):
    reactionText = reactionCrawer(driver, postUrl)
    reactionInfo = reactionProcess(reactionText)
    return reactionInfo