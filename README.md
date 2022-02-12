# FB_post_analyst
## 介紹
大一下大數據程式設計導論的期末專題。  
該程式可能因為FB修改網頁標籤或API停止更新而失效。
## 如何使用
一、在想要分析的貼文選擇右上角三個點->嵌入->複製代碼  
二、到資料夾中的 data/user_data.json 輸入自己的 facebook 帳號密碼  
三、複製代碼後執行程式，並依照指示輸入剛剛複製的內容  
四、從指定貼文爬取資料（執行的動作有：登入、爬取留言、獲得反應數量）    
五、取得留言資料後使用中研院提供開源自然語言（中文）斷句 model 來進行關鍵字截取    
## 程式使用到的外部函式庫
### Gdown
Gdown 這個套件可以從 google drive 下載模型檔。這個套件只是用來下載中研院開發的模型，並不會實際運用。使用前須先透過 pip 下載。
### Tensorflow
Tensorflow 是一個開源軟體庫，用於各種感知和語言理解任務的機器學習。  在這個專題中不會實際應用，僅用於下載和使用模型。使用前須先透過 pip 下載。
### Ckiptagger
Ckiptagger 是中研院開發的中文處理工具，他支援中文斷句、詞性分類、以及提供使用者自訂詞典功能。使用前要先透過 gdown 套件和一段程式碼下載模型，下載完就可以將程式碼刪除：
> from ckiptagger import data_utils  
> data_utils.download_data_gdown("./") #引號中的路徑為模型下載路徑   

要使用斷句功能前，必須先引用該函式庫底下的兩個 class：
> from ckiptagger import WS, POS
### Bs4
Beautiful soup 是一個外部套件，他可以讓開發者透過少少的程式碼來解析網頁的 html 碼並提供有用的資訊。使用前需先透過 pip 安裝套件。使用時需引入：
> from bs4 import BeautifulSoup
### Selenium
Selennium 是一個外部套件，他可以模擬真人瀏覽網頁的狀態，常用於讀取request 無法讀取的動態網頁如：Facebook, Instagram。使用前需先透過 pip 安裝套件。使用時需引入：
> from selenium import webdriver
### ChromeDriverManager
ChromeDriverManager 是一個外部套件，通常搭配上面的 selenium 使用，他的功能是安裝 chromedDriver。可以透過這個來隨時更新 driver 到最新版本。使用前需先透過 pip 安裝套件。使用時需引入：
> from webdriver_manager.chrome import ChromeDriverManager
## 示範
為防止程式無預期掛點，放一些影片來證明這個程式真的可執行。  
1. https://www.youtube.com/watch?v=MasW-WClehs
2. https://www.youtube.com/watch?v=lrYj-gyzvXg
## 備註
在學會git後才將檔案上傳上來。  


