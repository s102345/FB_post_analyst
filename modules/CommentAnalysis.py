from ckiptagger import WS, POS

def getKeyword(textList):
    ws = WS("./data")
    pos = POS("./data")

    keywordList = []

    for text in textList:
        #文字斷句
        ws_results = ws([text])
        #文字的詞性
        pos_results = pos(ws_results)
        #結果轉型成一維list
        ws_results = ws_results[0]
        pos_results = pos_results[0]

        #篩選
        for i in range (0, min(len(ws_results), len(pos_results))):
            #關於名詞
            if(str(pos_results[i]).find("Na") != -1):
                keywordList.append(ws_results[i])

        #print(ws_results)
        #print(pos_results)

    return keywordList
    #print("結果:", keyword)

#統計關鍵字出現次數
def getAnalysis(keywordList):
    analysisResult = dict()
    for keyword in keywordList:
        #重複關鍵字 + 1
        if keyword in analysisResult:
            analysisResult[keyword] += 1
        #關鍵字新增
        else:
            analysisResult[keyword] = 1

    return analysisResult

#針對關鍵字和次數進行排序
def dictSort(targetDict):
    tempDict = targetDict.items()
    tempDict = sorted(tempDict, key = lambda tempDict: tempDict[1])
    return tempDict

#回傳第N名以前的關鍵字
def getAnalysisResult(allCommentList, target = 5):
    keywordList = getKeyword(allCommentList)
    analysisResult = getAnalysis(keywordList)
    analysisResult = dictSort(analysisResult)
    temp = []

    for i in range(len(analysisResult) - 1, len(analysisResult) - 1 - target, -1):
        if(i < 0):
            break
        temp.append(analysisResult[i])

    analysisResult = temp

    return analysisResult


    
