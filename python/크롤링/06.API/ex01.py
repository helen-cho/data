#http 요청을 보내고 응답을 받기 위한 패키지
import requests
import datetime
import json
import csv

def getNaver(url, query):
    #발급받은 ID, SECRET
    headers = {
        'X-Naver-Client-Id':'DSISkunI4gxjpwj6Yl6J',
        'X-Naver-Client-Secret':'CxLnF9_VmQ'
    }
    #검색어와 출력 데이터 수
    params = {
        'query':query,
        'display':100
    }
    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            #응답(response)결과를 JSON 형식으로 파싱
            data_json = response.json()
            data_csv = [['상품명', '가격', '브랜드', '메이커']]
            #JSON 데이터 중 'items' 배열 형식 데이터를 반복
            for item in data_json['items']:
                title = item['title']
                price = item['lprice']
                brand = item['brand']
                maker = item['maker']
                print(title, price, brand, maker)
                print('-' * 100)
                data_csv.append([title, price, brand, maker])
            #JSON, csv 형식의 데이터를 반환환
            return data_json['items'], data_csv
    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL : {url}')
        return None
    

if __name__ == '__main__':
     #검색 API 기본 URL 주소와 검색어
    query = '노트북'
    url = 'https://openapi.naver.com/v1/search/shop.json'
    data = getNaver(url, query)

    #검색결과를 json 파일로 저장
    with open(f'data/{query}.json', 'w', encoding='utf-8') as json_file:
        json.dump(data[0], json_file, ensure_ascii=False, indent=4)

    #검색결과를 csv 파일로 저장
    with open(f'data/{query}.csv', "w", encoding="utf-8-sig", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data[1])    