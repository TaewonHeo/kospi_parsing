종목 목록 : Kospi_data.csv

## createDB.py
### 기업별 데이터 테이블 생성
Tb1 : Open, Close, UpDown, UpDownRatio, High, Low, Volume, InstVolume(기관거래량), ForeignVolume(외인거래량), ForignPosse(외인보유량), PersonalVolume(개인 거래량), shortsale(공매도)
```python
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
```
### Tb2 : PER PBR PCR 데이터를 Information 테이블에 한번에 정리.(분기별)
```python
sql = """CREATE TABLE Information(
Company VARCHAR(10) PRIMARY KEY,
CompanyCode INT,
PER DOUBLE,
PBR DOUBLE,
PCR DOUBLE,
Dividend DOUBLE,
NetProfit INT)"""
```
## FIP.py
Tb1 데이터 삽입을 위해 웹 크롤링(http://comp.fnguide.com/) mysql에 데이터 삽입

## Information.py
Tb2 데이터 삽입 코드

## openclose.py
open, close, high, low, volume 데이터 삽입

## PyService.py
위의 작업을 주기적으로 실행할 Window Services 생성 파일()
