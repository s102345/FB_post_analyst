from modules.Login import initialize
from modules.CommentProcess import getAllCommentContent
from modules.ShareProcess import getShareAmount
from modules.ReactionProcess import getReactionInfo
from modules.CommentAnalysis import getAnalysisResult

def inputProcess(url):
    # 從嵌入程式碼裡抓取網址
    urlStartPoint = url.find('href=')
    tempUrl = ""
    for i in range (urlStartPoint + len('href='), len(url)):
        if(url[i] == '"' or url[i] == "&"):
            break
        tempUrl += url[i]   

    url = tempUrl
    #進一步抓取.com後文字
    urlStartPoint = url.find('.com')
    tempUrl = ""
    for i in range (urlStartPoint + len('.com'), len(url)):
        tempUrl += url[i]

    url = tempUrl
    #%2F 轉換
    tempUrl = ""
    ignoreRange = 0
    for i in range (0, len(url)):
        if url[i] == "%":
            ignoreRange = i + len('%2f')
            tempUrl += '/'
        elif i < ignoreRange:
            pass
        else:
            tempUrl += url[i]
            ignoreRange = 0
    url = tempUrl
    #加上手機版網址
    tempUrl = "https://mobile.facebook.com" + url 
    url = tempUrl

    return url

if __name__=='__main__':
    postUrl = input('請輸入欲查詢之貼文：')
    postUrl = inputProcess(postUrl)

    print('正在登入Facebook...')
    driver = initialize()
    allCommentContent = getAllCommentContent(driver, postUrl)
    shareAmount = getShareAmount(driver, postUrl)
    reactionInfo = getReactionInfo(driver, postUrl)
    driver.quit()

    analysisResult = getAnalysisResult(allCommentContent)

    print("\n反應資訊：", reactionInfo)
    print("\n分享數量：", shareAmount)
    print(analysisResult)
    
    input("Press Enter to end this program")
    #print("留言：", allCommentInfo)
    #print("\n分享數量：", shareAmount)
    #print("\n反應資訊：", reactionInfo)
