import sys
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtWebKit import *
from bs4 import BeautifulSoup
import requests
import redis

r=redis.Redis("localhost")

class Client(QWebPage): #using pyside to load url instance

	def __init__(self,url):
		self.app=QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self.on_page_load)
		self.mainFrame().load(QUrl(url))
		self.app.exec_()

	def on_page_load(self):
		self.app.quit()

url="https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G" #Nifty50 Url to scrape
client_response=Client(url)
source=client_response.mainFrame().toHtml()


soup=BeautifulSoup(source,'html.parser')
test=soup.find_all('td')

r.delete('value')#used to deleted previous stored values in redis
r.delete('title')
#r.rpush('value','zero')
for i in test[:109]:#pushing scraped value into redis list
	print(i.text)
	if i.text!='':
		r.rpush('value',i.text)
	else:
		pass

#print("\n")
for tableheader in soup.find_all('th')[:10]: #gets scraped data table header
	print(tableheader.text)
	r.rpush("title",tableheader.text)




#---------------------code ends here--------------------------------------------------------------------------

"""import requests
from bs4 import BeautifulSoup


url="https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G"

r=requests.get(url)

soup=BeautifulSoup(r.content,"html.parser")

for tableheader in soup.find_all('th')[:10]:
	print(tableheader.text)
"""
