# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import urllib
import pymysql
import datetime
import re
import time
import csv
b=[]
c=[]
tb = []
with open('./Kospi_data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        b.append(row[0])
        c.append(row[1])
        tb.append("kr"+row[0])

b.pop(0)
tb.pop(0)
# print tb
c.pop(0)
list = zip(b,c)
con = pymysql.connect(host='localhost', user='root', password='apstinc',
                      db="finance", charset='utf8')
curs = con.cursor()
for i in range(len(b)):

    for p in range(1, 10, 1):
        try:
            curs = con.cursor()
            html = urllib.urlopen('http://paxnet.moneta.co.kr/stock/stockIntro/shortSale/shortSaleList.jsp?code=%s&p_curr_page=%d ' % (b[i], p))
            print 'http://paxnet.moneta.co.kr/stock/stockIntro/shortSale/shortSaleList.jsp?code=%s&p_curr_page=%d'% (b[i], p)
            soup = bs(html, "html.parser")
            table = b[i]

            titles = soup.find_all("td")
            for x in range(30):
                timestamp = str(titles[x * 6].get_text())
                ts = timestamp.replace('/', '-')
                print ts
                shortsale = int("".join(titles[x * 6 + 4].get_text().split(',')))
                qr = "insert into %s (TimeStamp, ShortSale) values ('%s', '%d')" % (tb[i], ts, shortsale)
                print qr
                curs.execute(qr)
                con.commit()
            curs.close()

        except:
            break
# s = titles[0]
# print s.get_text()
# print s.get_text()
# m=re.search('title', titles[0])
