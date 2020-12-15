import requests
from bs4 import BeautifulSoup
#html_data = requests.get('http://yahoo.com')
#soup = BeautifulSoup(html_data.text,"html.parser")
#print(soup.title)
nytimes_xml = requests.get('https://www.nytimes.com/interactive/2016/09/07/universal/ko/ways-to-be-a-better-person-korean.html')
naver_xml = requests.get('https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=015&aid=0004396470')
soup = BeautifulSoup(nytimes_xml.text,"html.parser")
nsoup = BeautifulSoup(naver_xml.text,"html.parser")
type(soup)
type(nsoup)
#print(soup.findAll('span'))
print(nsoup.findAll('span'))