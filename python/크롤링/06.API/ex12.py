import requests
import json
import math
import csv

file = open('data/data_go_key.txt')
key = file.readlines()
enKey = key[0].strip()
deKey = key[1].strip()

#API 접속후 응답데이터 불러오기
def getRequests(year, page):
    url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
    params ={'serviceKey' : deKey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : page, 'year' : year, 'itemCode' : 'PM10' }

    response = requests.get(url, params=params)
    json_data = json.loads(response.content)
    return json_data

#json 데이터 중 items 데이터 구하기
def getItems(json_data):
    items = json_data['response']['body']['items']
    for index, item in enumerate(items):
        issueDate = item['issueDate'] #발령일
        issueTime = item['issueTime'] #발령시간
        districtName = item['districtName'] #발령지역
        moveName = item['moveName'] #발령권역
        issueVal = item['issueVal'] #발령시 미세먼지 농도(단위: ug/m3)
        clearDate = item['clearDate'] #해제 날짜
        clearTime = item['clearTime'] #해제 시간
        seq = (page-1) * 100 + index + 1
        data = [seq, issueDate, issueTime, districtName, moveName, issueVal, clearDate, clearTime]
        item_list.append(data)
        print(data)

if __name__=='__main__':
    year = input('미세먼지 경보 발령 현황:')
    page=1
    item_list = [['일련번호','발령일','발령시간','발령지역','발령권역','농도','해제날짜','해제시간']]
    
    json_data = getRequests(year, page)
    totalCount = json_data['response']['body']['totalCount']
    if totalCount > 0:
        getItems(json_data)

    #마지막 페이지구하기기
    lastPage = math.ceil(totalCount/100) 

    for page in range(2, lastPage+1):
        json_data = getRequests(year, page)
        getItems(json_data)
    
    #검색결과를 csv 파일로 저장
    with open(f'data/{year}년 미세먼지 경보 발령 현황.csv', "w", encoding="utf-8-sig", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(item_list)   