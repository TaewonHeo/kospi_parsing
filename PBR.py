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
c.pop(0)
list = zip(b,c)
con = pymysql.connect(host='localhost', user='root', password='apstinc',
                      db="finance", charset='utf8')
for i in range(len(b)):

    for p in range(1, 10, 1):
        try:
            curs = con.cursor()
            html = urllib.urlopen('http://finance.naver.com/item/sise_day.nhn?code=%s&page=%d' % (b[i], p))
            soup = bs(html, "html.parser")
            table = b[i]

            tsw = soup.find_all("span", 'tah p10 gray03')
            prw = soup.find_all("span", 'tah p11')
            for t in range(len(prw)-1, 0, -1):
                if int("".join(prw[t].get_text().split(','))) == 0:
                    del prw[t]
            for x in range(10):
                timestamp = str(tsw[x].get_text())
                ts = timestamp.replace('.', '-')
                close = int("".join(prw[x*5].get_text().split(',')))
                open = int("".join(prw[x*5+1].get_text().split(',')))
                high = int("".join(prw[x*5+2].get_text().split(',')))
                low = int("".join(prw[x*5+3].get_text().split(',')))
                volume = int("".join(prw[x*5+4].get_text().split(',')))
                qr = "update %s set Open = %d, Close = %d, High = %d, Low = %d, Volume = %d where TimeStamp = '%s' " % (
                tb[i], open, close, high, low, volume, ts)
                curs.execute(qr)
                con.commit()
            curs.close()
        except:
            break

