from selenium import webdriver
import bs4
import pymysql
import csv
import time

class Main():
    def __init__(self):
        self.con = pymysql.connect(host='localhost', user='root', password='',
                              db="finance", charset='utf8')
        self.invalidCount = 0

    def LoadCompany(self):
        self.companyCode = []
        # self.companyName = []
        with open('./Kospi_data.csv','r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                self.companyCode.append(row[0])
                # self.companyName.append(row[1])

        self.companyCode.pop(0)
        self.comList = []
        for i, code in enumerate(self.companyCode):
            for digit in range(8):
                if len(list(code)) < 6:
                    code = "0" + code
                else:
                    break
            self.comList.append(code)
        # print(self.comList)
        # self.companyName.pop(0)
    def parsingException(self, url):
        dateList = "Delete Code"
        cont = "Delete Code"
        try:
            self.driver.quit()
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1920x1080')
            options.add_argument("disable-gpu")
            self.driver = webdriver.Chrome('E:\Chrome download\chromedriver_win32\chromedriver', chrome_options=options)
            self.driver.get(url)
            self.driver.refresh()
            time.sleep(3)
            self.driver.implicitly_wait(5)
            html1 = self.driver.page_source
            soup = bs4.BeautifulSoup(html1, 'html.parser')
            dates = str(soup.find_all('td', {"class": "a-center"})).split(',')
            cont = soup.find_all('td', {"class": "a-right"})
            dateList = [d.split('>')[1].split('<')[0] for d in dates]
        except:
            self.invalidCount += 1
            if self.invalidCount > 3:
                self.invalidCount = 0
                return "Delete Code", "Delete Code"
            self.parsingException(url)

        return dateList, cont

    def parsingException2(self, url):
        dateList = "Delete Code"
        cont = "Delete Code"
        try:
            self.driver2.quit()
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1920x1080')
            options.add_argument("disable-gpu")
            self.driver2 = webdriver.Chrome('E:\Chrome download\chromedriver_win32\chromedriver', chrome_options=options)
            self.driver2.get(url)
            self.driver2.refresh()
            time.sleep(3)
            self.driver2.implicitly_wait(5)
            html1 = self.driver2.page_source
            soup = bs4.BeautifulSoup(html1, 'html.parser')
            dates = str(soup.find_all('td', {"class": "a-center"})).split(',')
            cont = soup.find_all('td', {"class": "a-right"})
            dateList = [d.split('>')[1].split('<')[0] for d in dates]
        except:
            self.invalidCount += 1
            if self.invalidCount > 3:
                self.invalidCount = 0
                return "Delete Code", "Delete Code"
            self.parsingException(url)

        return dateList, cont

    def OpenChromeDriver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")

        self.driver = webdriver.Chrome('E:\Chrome download\chromedriver_win32\chromedriver', chrome_options=options)
        self.driver2 = webdriver.Chrome('E:\Chrome download\chromedriver_win32\chromedriver', chrome_options=options)

        for x in range(len(self.comList)):
            print(self.comList[x])
            url = 'http://paxnet.moneta.co.kr//stock/analysis/supplyDisclosure/supDmdAnalysis01?abbrSymbol={}'.format(self.comList[x])
            self.driver.get(url)
            self.driver.refresh()
            self.driver.implicitly_wait(3)
            html1 = self.driver.page_source
            soup = bs4.BeautifulSoup(html1, 'html.parser')
            dates = str(soup.find_all('td', {"class": "a-center"})).split(',')
            cont = soup.find_all('td', {"class": "a-right"})
            shortUrl2 = 'http://paxnet.moneta.co.kr/stock/analysis/selling?abbrSymbol={}'.format(self.comList[x])
            self.driver2.get(shortUrl2)
            self.driver2.refresh()
            self.driver2.implicitly_wait(3)
            html_short = self.driver2.page_source
            soup_short = bs4.BeautifulSoup(html_short, 'html.parser')
            try: #first url
                dateList = [d.split('>')[1].split('<')[0] for d in dates]
            except:
                dateList = self.parsingException(url)[0]
                cont = self.parsingException(url)[1]
            try: #second url(short selling)
                dates2 = str(soup_short.find_all('td', {"class": "a-center"})).split(',')
                dateList2 = [d.split('>')[1].split('<')[0] for d in dates2]
                cont_short = soup_short.find_all('td', {"class": "a-right"})
            except:
                dateList2 = self.parsingException2(shortUrl2)[0]
                cont_short = self.parsingException2(shortUrl2)[1]
            if dateList == 'Delete Code':
                f = open("./deleteList.txt", 'w')
                data = '{}'.format(self.comList[x])
                f.write(data)
                f.close()
            if dateList2 == 'Delete Code':
                f = open("./deleteList.txt", 'w')
                data = '{}'.format(self.comList[x])
                f.write(data)
                f.close()
            else:
                priceList = []
                RatioList = []
                ForeignList = []
                InstList = []
                PersonList = []
                ShortRatioList = []
                VolumeList = []
                for i, row in enumerate(cont):
                    if i % 7 == 0:
                        strPrice = str(row).split('>')[1].split('<')[0].split(',')
                        numPrice = ''.join(strPrice)
                        priceList.append(float(numPrice))
                    elif i % 7 == 2:
                        Ratio = str(row).split('>')[2].split('</span')[0].split('%')
                        numRaio = ''.join(Ratio)
                        RatioList.append(float(numRaio))
                    elif i % 7 == 3:
                        strForeign = str(row).split('>')[2].split('</span')[0].split(',')
                        numForeign = ''.join(strForeign)
                        ForeignList.append(float(numForeign))
                    elif i % 7 == 5:
                        strInst = str(row).split('>')[2].split('</span')[0].split(',')
                        numInst = ''.join(strInst)
                        InstList.append(float(numInst))
                    elif i % 7 == 6:
                        strPerson = str(row).split('>')[2].split('</span')[0].split(',')
                        numPerson = ''.join(strPerson)
                        PersonList.append(float(numPerson))
                for s, row_s in enumerate(cont_short):
                    if s % 5 == 1:
                        strvolume = str(row_s).split('>')[1].split('</')[0].split(',')
                        numVolume = ''.join(strvolume)
                        VolumeList.append(float(numVolume))
                    if s % 5 == 2:
                        ShortRatio = str(row_s).split('>')[1].split('</')[0].split('%')
                        numShortRaio = ''.join(ShortRatio)
                        ShortRatioList.append(float(numShortRaio))
                zipList = list(zip(dateList, priceList, RatioList, VolumeList, InstList,ForeignList,PersonList, ShortRatioList))
                zipListforUpdate = (str(dateList[0]), priceList[0], RatioList[0], VolumeList[0], InstList[0],ForeignList[0],PersonList[0], ShortRatioList[0])
                self.sqlinsert(self.comList[x], str(zipList))
                self.sqlupdate(self.comList[x], zipListforUpdate)
        self.driver.quit()

    def sqlinsert(self, companyCode, values):
        curs = self.con.cursor()
        try:
            insertQuery = "insert into t{} (TimeStamp, Close, UpDownRatio, Volume, InstVolume, ForeignVolume, PersonalVolume, ShortSale) values {}".format(companyCode, values[1:-1])
            curs.execute(insertQuery)
            self.con.commit()
        except:
            pass
        curs.close()

    def sqlupdate(self, companyCode, values):
        curs = self.con.cursor()
        try:
            updateQuery = "update t%s set Close=%d, UpDownRatio=%d, Volume=%d, InstVolume=%d, ForeignVolume=%d, PersonalVolume=%d, ShortSale=%d where TimeStamp='%s';"%(
                companyCode, values[1], values[2],values[3],values[4],values[5],values[6],values[7],values[0])
            curs.execute(updateQuery)
            self.con.commit()
        except:
            pass
        curs.close()

    def createTable(self):
        for i in range(len(self.comList)):
            curs = self.con.cursor()
            sql = """CREATE TABLE IF NOT EXISTS t{}(
                TimeStamp Date PRIMARY KEY,
                Open INT,
                Close INT,  
                UpDownRatio DOUBLE,
                Volume BIGINT,
                InstVolume BIGINT,
                ForeignVolume BIGINT,
                PersonalVolume BIGINT,
                ShortSale DOUBLE)""" .format(self.comList[i])
            curs.execute(sql)
            self.con.commit()
            curs.close()
main = Main()
main.LoadCompany()
# main.createTable()
main.OpenChromeDriver()
