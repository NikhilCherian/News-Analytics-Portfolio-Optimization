import urllib2
from bs4 import BeautifulSoup
import re



x = raw_input()
url= 'https://in.finance.yahoo.com/quote/'+x+'?/p='+x
f2=open(x+".csv", 'a')
print(url)

res= urllib2.urlopen(url)
html= res.read()
filename= "scrapetcsnews.html"
file=open(filename,'w')
print >>file, html
file.close()
f1= open("scrapetcsnews.html",'r')
soup = BeautifulSoup(f1,'html.parser')

div=soup.findAll('div', class_="Fw(b) Fz(20px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 Pos(r) C(#000) C(#0078ff):h")
print len(div)
