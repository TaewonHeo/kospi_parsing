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
for i in range(len(b)):

    for p in range(1):
        try:
            curs = con.cursor()
            html = urllib.urlopen('http://paxnet.moneta.co.kr/stock/stockIntro/stockDimAnalysis/supDmdAnalysis01.jsp?code=%s&wlog_pip=T_supDmdAnalysis01'% b[i])
            soup = bs(html, "html.parser")
            table = b[i]

            tsw = soup.find_all("td", 'TB_tr01_cen')
            tsg = soup.find_all("td", 'TB_tr02_cen')
            prw = soup.find_all("td", 'TB_tr01_R2')
            prg = soup.find_all("td", 'TB_tr02_R2')
            try:
                for x in range(20):
                    timestamp = str(tsw[x].get_text())
                    ts = timestamp.replace('/', '-')
                    timestamp2 = str(tsg[x].get_text())
                    ts2 = timestamp2.replace('/', '-')
                    fr_vol = int("".join(prw[x*7+3].get_text().split(',')))
                    ins_vol = int("".join(prw[x*7+5].get_text().split(',')))
                    ps_vol = int("".join(prw[x*7+6].get_text().split(',')))
                    fr_vol2 = int("".join(prg[x * 7 + 3].get_text().split(',')))
                    ins_vol2 = int("".join(prg[x * 7 + 5].get_text().split(',')))
                    ps_vol2 = int("".join(prg[x * 7 + 6].get_text().split(',')))
                    # print timestamp, fr_vol, ins_vol, ps_vol

                    # qr = "update %s set InstVolume = %d, ForeignVolume = %d, PersonalVolume = %d where TimeStamp = '%s' " % (tb[i], ins_vol, fr_vol, ps_vol, ts)
                    qr = "insert into %s (TimeStamp, InstVolume, ForeignVolume, PersonalVolume) values ('%s', %d, %d, %d)" % (tb[i], ts, ins_vol, fr_vol, ps_vol)
                    qr2 = "insert into %s (TimeStamp, InstVolume, ForeignVolume, PersonalVolume) values ('%s', %d, %d, %d)" % (tb[i], ts2, ins_vol2, fr_vol2, ps_vol2)
                    # qr2 = "update %s set InstVolume = %d, ForeignVolume = %d, PersonalVolume = %d where TimeStamp = '%s' " % (tb[i], ins_vol2, fr_vol2, ps_vol2, ts2)
                    curs.execute(qr)
                    curs.execute(qr2)
                    con.commit()
            except:
                break
                # print tsg[x], prg[x*7+3], prg[x*7+5], prg[x*7+6]
                    # print pr[1*7+3], pr[1*7+5], pr[1*7+6]
                # for x in range(30):
                #     timestamp = str(titles[x * 6].get_text())
                #     ts = timestamp.replace('/', '-')
                #     shortsale = int("".join(titles[x * 6 + 4].get_text().split(',')))
                #     qr = "insert into %s (TimeStamp, ShortSale) values ('%s', '%d')" % (tb[i], ts, shortsale)
                #     curs.execute(qr)
                #     con.commit()
                # curs.close()

                # for x in range(30):
                #     timestamp = str(titles[x * 6].get_text())
                #     ts = timestamp.replace('/', '-')
                #     print ts
                #     shortsale = int("".join(titles[x * 6 + 4].get_text().split(',')))
                #     qr = "insert into %s (TimeStamp, ShortSale) values ('%s', '%d')" % (tb[i], ts, shortsale)
                #     print qr
                #     curs.execute(qr)
                #     con.commit()
                # curs.close()
            curs.close()
        except:
            break

