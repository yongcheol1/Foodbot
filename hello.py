import requests
from bs4 import BeautifulSoup

import datetime
현재 = str(datetime.datetime.now()) 
#print (현재)    
날 = 현재[:4] + 현재[5:7] + 현재[8:10]
#print(날)

req = requests.get("http://school.cbe.go.kr/chungjuja-e/M01040504/list?ymd="+ "20210604")
#print(req.text)
soup = BeautifulSoup(req.text,"html.parser")
#print(soup)

atag = soup.find("a",href="/chungjuja-e/M01040504/list?ymd=20210604")
#print(atag)
li = atag.find_all('li')
#print(li)
식단 = ""

for i in li :
    식단 = 식단 + i.text + "\n"
#print(식단)

##웹크롤링 봇
import telegram
토큰 = "1854115469:AAHrPGRFJK2RlsuSmoAc8bHD6B9CG_0OjR4"
봇 = telegram.Bot(token=토큰)

#for i in 봇.getUpdates():
#    print(i.message)
봇.send_message(1413857253, 식단)   