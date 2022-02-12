from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import random

def unfoldComment(driver):
    unfoldButtonList={'則回覆', '回覆了', '顯示先前的留言', '查看更多留言'}
    upperbound = 50
    for unfoldButton in unfoldButtonList:
        #最多點upperbound次
        for i in range(0, upperbound):
            try:
                unfoldElement= driver.find_element_by_partial_link_text(unfoldButton)
                unfoldElement.click()
                sleep(random.uniform(3, 5))
            except:
                break

def commentCrawer(driver, postUrl):
    #postUrl = input('請輸入欲查詢的文章網址：')
    driver.get(postUrl)
    sleep(random.uniform(3, 5))
    unfoldComment(driver)
    htmlText=driver.page_source
    beautifulSoup=BeautifulSoup(htmlText,'html.parser')
    comments=beautifulSoup.find_all('div',class_='_2b06')
    return comments

def commentProcess(comments):
    #擷取所有留言和人名
    allCommentInfo = []
    comments = list(comments)
    for comment in comments:
        scriptFlag = False 
        commentInfo = []
        strTemp = ""
        comment = str(comment)
        for i in range(0, len(comment)):
            #Priority 1 '<'
            if comment[i] == '<':
                #不為空
                if(strTemp != ""):
                    commentInfo.append(strTemp)

                strTemp = ""
                scriptFlag = True

            #Priority 2 '>'
            elif comment[i] == '>':
                scriptFlag = False
            
            #Priority 3 isIn "<>"
            elif scriptFlag:
                pass

            #Infomation collect
            else:
                strTemp += comment[i] 
       
        allCommentInfo.append(commentInfo)   
    
    allCommentContent = []
    commentContent = ""

    #去掉頭號粉絲&留言者
    for i in range(0, len(allCommentInfo)):
        commentContent = ""
        startPoint = 0
        if(allCommentInfo[i][startPoint] == "頭號粉絲"):
            startPoint = 1
        # +1 忽略人名
        for j in range(startPoint + 1, len(allCommentInfo[i])):
            commentContent += allCommentInfo[i][j]
        pass
        allCommentContent.append(commentContent)

    return allCommentContent 


def getAllCommentContent(driver, postUrl):
    comments = commentCrawer(driver, postUrl)
    allCommentContent = commentProcess(comments)
    return allCommentContent

   