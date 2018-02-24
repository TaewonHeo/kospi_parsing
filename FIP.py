# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import urllib.request
import pymysql
import csv
class Main():
    def LoadCompany(self):
        self.companyCode = []
        # self.companyName = []
        with open('./Kospi_data.csv','r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                self.companyCode.append(row[0])
                # self.companyName.append(row[1])

        self.companyCode.pop(0)
        # self.companyName.pop(0)

    def openMysqlConnection(self):
        self.con = pymysql.connect(host='192.168.68.130', user='root', password='dlsgk8267',db="finance", charset='utf8')

    def createTable(self):
        curs = self.con.cursor()
        for i in range(len(self.companyCode)):
            sql = """CREATE TABLE IF NOT EXISTS %s(
            TimeStamp Date PRIMARY KEY,
            Open INT,
            Close INT,
            UpDown INT,
            UpDownRatio DOUBLE,
            High INT,
            Low INT,
            Volume BIGINT,
            InstVolume BIGINT,
            ForeignVolume BIGINT,
            ForeignPosses BIGINT,
            PersonalVolume BIGINT,
            ShortSale BIGINT)""" % b[i]
            curs.execute(sql)
        self.con.commit()
        curs.close()

    def insertVolume(self):
        for i in range(len(self.companyCode)):
            for p in range(1):
                curs = self.con.cursor()
                html = urllib.request.urlopen('http://paxnet.moneta.co.kr/stock/stockIntro/stockDimAnalysis/supDmdAnalysis01.jsp?code=%s&wlog_pip=T_supDmdAnalysis01'% b[i])
                soup = bs(html, "html.parser")

                tsw = soup.find_all("td", 'TB_tr01_cen')
                tsg = soup.find_all("td", 'TB_tr02_cen')
                prw = soup.find_all("td", 'TB_tr01_R2')
                prg = soup.find_all("td", 'TB_tr02_R2')

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
                    try:
                        qr = "insert into %s (TimeStamp, InstVolume, ForeignVolume, PersonalVolume) values ('KR%s', %d, %d, %d)" % (str(self.companyCode[i]), ts, ins_vol, fr_vol, ps_vol)
                        qr2 = "insert into %s (TimeStamp, InstVolume, ForeignVolume, PersonalVolume) values ('KR%s', %d, %d, %d)" % (str(self.companyCode[i]), ts2, ins_vol2, fr_vol2, ps_vol2)
                        curs.execute(qr)
                        curs.execute(qr2)
                        self.con.commit()
                    except:
                        qr = "update %s set InstVolume = %d, ForeignVolume = %d, PersonalVolume = %d where TimeStamp = '%s' " % (
                            str(self.companyCode[i]), ins_vol, fr_vol, ps_vol, ts)
                        qr2 = "update %s set InstVolume = %d, ForeignVolume = %d, PersonalVolume = %d where TimeStamp = '%s' " % (str(self.companyCode[i]), ins_vol2, fr_vol2, ps_vol2, ts2)
                        curs.execute(qr)
                        curs.execute(qr2)
                        self.con.commit()
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


if __name__ == '__main__':
    parsing = Main()
    parsing.LoadCompany()
    parsing.createTable()
    parsing.openMysqlConnection()
    parsing.insertVolume()
