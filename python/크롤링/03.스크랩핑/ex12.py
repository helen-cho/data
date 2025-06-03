import csv
import requests
from bs4 import BeautifulSoup
import re

filename = "data/코스닥거래상위1-100.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

url = "https://finance.naver.com/sise/sise_quant.naver?sosok=1"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

rows = soup.find("table", attrs={"class":"type_2"}).find_all("tr")

for row in rows:
    columns = row.find_all("td")
    #<tr><td colspan="10"></td></tr>인 경우 skip
    if len(columns) <= 1:
        continue

    #re.sub(pattern, replace, text) : text 중 pattern에 해당하는 부분을 replace로 대체한다.
    data = [re.sub("\t|\n|상승|하락|보합", "", column.get_text()) for column in columns]
    writer.writerow(data)