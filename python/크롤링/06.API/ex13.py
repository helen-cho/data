import requests
import json
import pprint
from datetime import datetime
import math

file = open('data/data_go_key.txt')
key = file.readlines()
enKey = key[0].strip()
deKey = key[1].strip()

def getReauest(page, depId, arrId, year_month):
    url = 'http://apis.data.go.kr/1613000/ExpBusInfoService/getStrtpntAlocFndExpbusInfo'
    params ={'serviceKey' : deKey, 'pageNo' : page, 'numOfRows' : '10', '_type' : 'json', 'depTerminalId' : depId, 'arrTerminalId' : '', 'depPlandTime' : year_month, 'busGradeId' : '1' }

    response = requests.get(url, params=params)
    json_data = json.loads(response.content)
    #pprint.pprint(json_data)
    return json_data

def getItems(json_data):
    items = json_data['response']['body']['items']['item']    
    
    for index, item in enumerate(items):
        routeId = item['routeId'] #노선ID
        gradeNm = item['gradeNm'] #버스등급

        datetime_format ='%Y%m%d%H%M'
        depPlandTime = datetime.strptime(str(item['depPlandTime']), datetime_format) #출발시간
        depfmt = depPlandTime.strftime('%Y-%m-%d %H:%M')
        
        arrPlandTime = datetime.strptime(str(item['arrPlandTime']), datetime_format) #도착시간
        arrfmt = arrPlandTime.strftime('%Y-%m-%d %H:%M')

        depPlaceNm = item['depPlaceNm'] #출발지
        arrPlaceNm = item['arrPlaceNm'] #도착지
        charge = item['charge'] #운임

        seq = (page-1) * 10 + index + 1
        data = [seq, routeId, gradeNm, depfmt, arrfmt, depPlaceNm, arrPlaceNm, charge]
        item_list.append(data)
        print(data)

if __name__=='__main__':
    page=1
    depId = 'NAEK010'
    arrId = 'NAEK300'
    year_month='20250130'

    item_list = []
    json_data = getReauest(page, depId, arrId, year_month)
    totalCount = json_data['response']['body']['totalCount']
    if totalCount > 0:
        getItems(json_data)

    lastPage = math.ceil(totalCount/10)
    for page in range(2, lastPage+1):
        json_data = getReauest(page, depId, arrId, year_month)
        getItems(json_data)
