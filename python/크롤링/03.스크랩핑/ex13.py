import csv
import requests
from bs4 import BeautifulSoup
import re

filename = "data/시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N    종목명    현재가    전일비    등락률    액면가    시가총액    상장주식수    외국인비율    거래량    PER    ROE".split("\t")
writer.writerow(title)

for page in range(1, 5):
    url=f"https://finance.naver.com/sise/sise_market_sum.naver?&page={page}"
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        if len(columns) <= 1: 
            continue

        data=[re.sub("\t|\n|상승|하락|보합","", column.get_text()) for column in columns]
        writer.writerow(data)