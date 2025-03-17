import requests
import pprint
import json

file = open('data/data_go_key.txt')
key = file.readlines()
enKey = key[0].strip()
deKey = key[1].strip()

url = 'http://apis.data.go.kr/5690000/sjSpeedBump/sj_00000170'
params ={'serviceKey' : deKey, 'pageIndex' : '1', 'pageUnit' : '20', 'dataTy' : 'json', 'searchCondition' : 'ovrspd_Prvn_Stlese', 'searchKeyword' : '1' }

response = requests.get(url, params=params)
json_data = json.loads(response.content)
items = json_data['body']['items']
#pprint.pprint(items)

import folium

map = folium.Map(('36.5007', '127.2579'), zoom_start=15) #세종 어진동
for item in items:
    add = item['addr']
    tel = item['telno']
    lat = item['la']
    lng = item['lo']
    print(add, lat, lng)

    location = (lat, lng)
    text = f'{add}<br>{tel}<br>'
    popup = folium.Popup(text, max_width=200)

    #마커 생성
    folium.Marker(
        location,
        popup,
        icon=folium.Icon(color='red', icon='glyphicon-exclamation-sign')
    ).add_to(map)

#지도를 HTML로 저장
map.save('data/세종시과속방지턱.html')