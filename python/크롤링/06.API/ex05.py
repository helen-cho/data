from ex04 import getInfo
import requests
import time
import pprint

file = open('data/data_kakao_key.txt')
key = file.readlines()
apiKey = key[0].strip()

def getLatLng():
    info, name_list, tel_list, add_list = getInfo()

    lat_list = [] #위도 리스트
    lng_list = [] #경도도 리스트
    for add in add_list:
        url = 'https://dapi.kakao.com/v2/local/search/address.json'
        params = {
            'query':add
        }
        headers = {
            'Authorization': f'KakaoAK {apiKey}'
        }

        response = requests.get(url, params=params, headers=headers)
        #응답결과를 json 타입으로 변경한다.
        json_data = response.json()

        #documents에 첫 번째 아이템
        address = json_data['documents'][0]['address']
        lng_list.append(address['x']) #경도(longitude)
        lat_list.append(address['y']) #위도(latitude)
        time.sleep(0.5) #0.5초 기다린다.

    lat_lng = list(zip(lat_list, lng_list))
    name_lat_lng = list(zip(name_list, lat_lng))
    info = dict(name_lat_lng)
    return name_list, tel_list, add_list, lat_list, lng_list

if __name__=='__main__':
    info = getLatLng()
    pprint.pprint(info)