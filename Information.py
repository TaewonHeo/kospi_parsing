# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import urllib.request
import pymysql

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
con = pymysql.connect(host='localhost', user='root', password='dlsgk8267',
                      db="finance", charset='utf8')
for i in range(len(b)):
    for p in range(1):
        try:
            # curs = con.cursor()
            # html = urllib.request.urlopen('http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A%s&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701'% b[i])
            html = urllib.request.urlopen('http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A%s&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701'% b[i])
            html2 = urllib.request.urlopen('http://comp.fnguide.com/SVO2/ASP/SVD_Invest.asp?pGB=1&gicode=A%s&cID=&MenuYn=Y&ReportGB=&NewMenuID=105&stkGb=701'% b[i])
            soup = bs(html, "html.parser")
            soup2 = bs(html2, "html.parser")
            table = b[i]

            tsw = soup.find("div", "corp_group2")
            prw = soup2.find_all("td", 'tdbg_y')
            net = soup.find_all("td", 'tdbg_b')
            # try:
            try:
                netp = float("".join(net[4].get_text().split(',')))
            except:
                netp = -1.0
            try:
                pcr = float(prw[35].get_text())
            except:
                pcr = -1.0
            # dd = tsw.find_all("dd")[1]
            try:
                per = float(tsw.find_all("dd")[1].get_text())
            except:
                per = -1.0
            try:
                pbr = float(tsw.find_all("dd")[7].get_text())
            except:
                pbr = -1.0
            try:
                divid = float(tsw.find_all("dd")[9].get_text())
                divid = divid.replace("%", '')
            except:
                divid = -1.0
            if per == "-":
                per = -1.0
            if divid == "-":
                divid = -1.0
            # print c[i], b[i], per, pbr, pcr, divid, netp
            # print type(c[i]), type(b[i]), type(per), type(pbr), type(pcr), type(divid), type(netp)
            # qr = "insert into Information (CompanyCode, PER, PBR, PCR, Dividend, NetProfit)\
            #  values ('%s', %f, %f, %f, %f, %f)" % (b[i].zfill(6), per, pbr, pcr, divid, netp)
            # print c[i], b[i], per, pbr, pcr, divid, netp
            # curs.execute(qr)
            # con.commit()
            # curs.close()
            # except:
            #     netp = 0
            #     pcr = float(prw[35].get_text())
            #     dd = tsw.find_all("dd")[1]
            #     per = tsw.find_all("dd")[1].get_text()
            #     pbr = float(tsw.find_all("dd")[7].get_text())
            #     divid = tsw.find_all("dd")[9].get_text()
            #     divid = divid.replace("%", '')
            #     if per == "-":
            #         per = -1
            #     if divid == "-":
            #         divid = -1
            #     print c[i], b[i], per, pbr, pcr, divid, netp
            #     qr = "insert into Information (Company, CompanyCode, PER, PBR, PCR, Dividend, NetProfit) \
            #     values ('%s', '%s', %0.2f, %0.2f, %0.2f, %0.2f, %d)" % (c[i], b[i], per, pbr, pcr, divid, netp)
            #     # curs.execute(qr)
            #     con.commit()
            #     curs.close()
        except:
            break

