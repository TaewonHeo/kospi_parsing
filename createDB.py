# # -*- coding: utf-8 -*-
# import csv
# import pymysql
#
# list = dict
# print list
# b=[]
# c=[]
# with open('./Kospi_data.csv','r') as csvfile:
#     reader = csv.reader(csvfile)
#     for i, row in enumerate(reader):
#         b.append('KR'+row[0])
#         c.append(row[1])
#
# b.pop(0)
# c.pop(0)
# list = zip(b,c)
#
# con = pymysql.connect(host='localhost', user='root', password='apstinc',
#                       db="finance", charset='utf8')
# curs = con.cursor()
# for i in range(len(b)):
#     sql = """CREATE TABLE IF NOT EXISTS %s(
#     TimeStamp Date PRIMARY KEY,
#     Open INT,
#     Close INT,
#     UpDown INT,
#     UpDownRatio DOUBLE,
#     High INT,
#     Low INT,
#     Volume BIGINT,
#     InstVolume BIGINT,
#     ForeignVolume BIGINT,
#     ForeignPosses BIGINT,
#     PersonalVolume BIGINT,
#     ShortSale BIGINT)""" % b[i]
#     curs.execute(sql)
#         # print sql
# con.commit()
# curs.close()
#
# # -*- coding: utf-8 -*-
# import csv
# import pymysql
#
# list = dict
# print list
# b=[]
# c=[]
# with open('./Kospi_data.csv','r') as csvfile:
#     reader = csv.reader(csvfile)
#     for i, row in enumerate(reader):
#         b.append('KR'+row[0])
#         c.append(row[1])
#
# b.pop(0)
# c.pop(0)
# list = zip(b,c)
#
# con = pymysql.connect(host='localhost', user='root', password='apstinc',
#                       db="finance", charset='utf8')
# curs = con.cursor()
# for i in range(len(b)):
#     sql = """CREATE TABLE IF NOT EXISTS %s(
#     TimeStamp Date PRIMARY KEY,
#     Open INT,
#     Close INT,
#     UpDown INT,
#     UpDownRatio DOUBLE,
#     High INT,
#     Low INT,
#     Volume BIGINT,
#     InstVolume BIGINT,
#     ForeignVolume BIGINT,
#     ForeignPosses BIGINT,
#     PersonalVolume BIGINT,
#     ShortSale BIGINT)""" % b[i]
#     curs.execute(sql)
#         # print sql
# con.commit()
# curs.close()

# -*- coding: utf-8 -*-
import csv
import pymysql

list = dict
print list
b=[]
c=[]
tb = []
with open('./Kospi_data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        b.append(row[0])
        c.append(row[1])
        tb.append("kr" + row[0])
tb.pop(0)
b.pop(0)
c.pop(0)
print c
list = zip(b,c)

con = pymysql.connect(host='localhost', user='root', password='apstinc',
                      db="finance", charset='utf8')
curs = con.cursor()
# for i in range(len(b)):
sql = """CREATE TABLE Information(
Company VARCHAR(10) PRIMARY KEY,
CompanyCode INT,
PER DOUBLE,
PBR DOUBLE,
PCR DOUBLE,
Dividend DOUBLE,
NetProfit INT)"""
curs.execute(sql)
        # print sql
con.commit()
curs.close()