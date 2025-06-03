import requests
from bs4 import BeautifulSoup
import csv

f = open('data/할리스.csv', "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

seq = 0
for page in range(1, 11):
    url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store='
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    tbody = soup.find('tbody')
    es = tbody.find_all('tr')
    print(f'========== {page} ==========')
    for index, e in enumerate(es):
        seq += 1
        store = e.find_all('td')
        store_name = store[1].get_text().strip()
        store_city = store[0].get_text().strip()
        store_address = store[3].get_text().strip().replace(' .', '')
        store_phone = store[5].get_text().strip()
        data = [seq, store_name, store_city, store_address, store_phone]
        writer.writerow(data)
        print(seq, store_name, store_city, store_address, store_phone)
