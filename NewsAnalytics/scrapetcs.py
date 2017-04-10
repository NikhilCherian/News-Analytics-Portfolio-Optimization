import urllib2
from bs4 import BeautifulSoup
import re


url= 'https://in.finance.yahoo.com/q/h?s=TCS.NS'
res= urllib2.urlopen(url)
html= res.read()

filename= "F:\FinanceProject\code\NewsAnalytics\scrapetcsnews.html"
file=open(filename,'wb')
print >>file, html
file.close()
