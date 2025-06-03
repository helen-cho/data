import requests
import json

file = open('data/data_go_key.txt')
key = file.readlines()
enKey = key[0].strip()
deKey = key[1].strip()

def getReauest(searchName):
    url = 'http://apis.data.go.kr/1613000/ExpBusInfoService/getExpBusTrminlList'
    params ={'serviceKey' : deKey, 'pageNo' : 1, 'numOfRows' : '10', '_type' : 'json', 'terminalNm':searchName}

    response = requests.get(url, params=params)
    json_data = json.loads(response.content)
    #print(json_data)
    return json_data
  
if __name__=='__main__':
    while True:
        searchName = input('검색할 터미널명 (종료:q):')
        if searchName == 'Q' or searchName == 'q':
            print('검색을 종료합니다.')
            break

        json_data = getReauest(searchName)

        totalCount = json_data['response']['body']['totalCount']
        if totalCount == 0:
            print('터미널이 존재하지 않습니다.')
        elif totalCount == 1:
            item = json_data['response']['body']['items']['item']
            id = item['terminalId']
            name = item['terminalNm']
            print(id, name)
        else:
            items = json_data['response']['body']['items']['item']
            for item in items:
                id = item['terminalId']
                name = item['terminalNm']
                print(id, name)