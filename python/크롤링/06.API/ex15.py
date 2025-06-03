import requests
from bs4 import BeautifulSoup
import math
import csv

file = open('data/data_go_key.txt')
key = file.readlines()
enKey = key[0].strip()
deKey = key[1].strip()

def getRequests(gu_code, year_month, page):
    url = f'http://apis.data.go.kr/1613000/RTMSDataSvcAptRent/getRTMSDataSvcAptRent'
    params = {'serviceKey':deKey, 'LAWD_CD':gu_code, 'DEAL_YMD':{year_month},'pageNo':page,'numOfRows':10}
    response = requests.get(url, params=params)

    soup = BeautifulSoup(response.text, 'lxml-xml')
    #print(soup.prettify())
    return soup

if __name__=='__main__':
    gu_code = '28260'
    year_month = ['202410', '202411', '202412', '202501']

    row_list = []
    is_head = False
    for i in range(len(year_month)):
        page = 1
        soup = getRequests(gu_code, year_month[i], page)
        rows = soup.find_all('item')

        if is_head == False:
            columns = rows[0].find_all()
            name_list = [columns[k].name for k in range(len(columns))]
            row_list.append(name_list)
            is_head= True

        for j in range(len(rows)):
            columns = rows[j].find_all()
            col_list =[columns[k].text for k in range(len(columns))]
            row_list.append(col_list)

    #검색결과를 csv 파일로 저장
    with open(f'data/{gu_code}구 아파트 전월세.csv', "w", encoding="utf-8-sig", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(row_list)
    print(row_list)