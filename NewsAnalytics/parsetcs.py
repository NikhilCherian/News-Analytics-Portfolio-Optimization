import urllib2
from bs4 import BeautifulSoup
import re


def headline_parser(div, f2):
    for i in div:
        for u in i.find_all('ul'):
            for l in u.find_all('li'):
                x = l.find_all('a')
                #print(x[0].getText())
                print >> f2,x[0].getText()

x = raw_input()
url= 'https://in.finance.yahoo.com/q/h?s='+x
f2=open(x+".csv", 'a')
print(url)

while 1:
    res= urllib2.urlopen(url)
    html= res.read()
    filename= "scrapetcsnews.html"
    file=open(filename,'w')
    print >>file, html
    file.close()
    f1= open("scrapetcsnews.html",'r')
    soup = BeautifulSoup(f1,'html.parser')

    div=soup.findAll('div', class_="mod yfi_quote_headline withsky")
    count = len(re.findall('ul',str(div[0])))
    if count != 0:
        headline_parser(div, f2)
    else:
        break
    links = soup.findAll('a')
    flag = False
    for link in links:
        if link.getText() == 'Older Headlines':
            next_link =  link['href']
            flag = True

    if flag == False:
        break

    next_link = "https://in.finance.yahoo.com"+next_link
    print next_link
    url = next_link
