from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv

url='https://www.norangtongdak.co.kr/store/store.html'
browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(3) #3초 안에 웹페이지를 load하면 바로 넘어가거나 10초를 기다림

sido = browser.find_element(By.ID, 'sido')
sido = Select(sido)
sigugun = browser.find_element(By.ID, 'sigugun')
sigugun = Select(sigugun)
btn = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div[1]/div/div/form/div[2]/button')

seq = 1
name_list = []
add_list = []
tel_list = []
info_list = []
city = '인천'
for i in range(len(sido.options)):
    #print(sido.options[i].text)
    if sido.options[i].text == city:
        sido.select_by_index(i) #선택박스에 위치한 순서 값으로 선택한다.
        for j in range(len(sigugun.options)):
            #print(sigugun.options[j].text)
            if j != 0:
                sigugun.select_by_index(j)
            
                btn.click()
                time.sleep(1)

                info = browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[5]/div[1]/div/div/div')
                names = info.find_elements(By.CLASS_NAME, 'st2')
                tels = info.find_elements(By.CLASS_NAME, 'st3')
                adds = info.find_elements(By.CLASS_NAME, 'st5')
               
                for i in range(len(names)):
                    name= names[i].text
                    tel = tels[i].text
                    add = adds[i].text
                    
                    name_list.append(name)
                    tel_list.append(tel)
                    add_list.append(add)

                    print(seq, name, tel, add)
                    info_list.append([seq, name, tel, add])
                    seq += 1
        break

#검색결과를 파일에 저장
with open(f'data/노랑통닭{city}.csv', "w", encoding="utf-8-sig", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(info_list)

#주소와 Kakao API를 활용 위, 경도 수집
import requests
import pprint

file = open('data/data_kakao_key.txt')
key = file.readlines()
apiKey = key[0].strip()
lat_list = []
lng_list = []

for add in add_list:
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    params = {
        'query':add
    }
    headers = {
        'Authorization':f'KakaoAK {apiKey}'
    }
    response = requests.get(url, params=params, headers=headers)
    json_data = response.json()

    address = json_data['documents'][0]['address']
    lng_list.append(address['x']) #경도(longitude)
    lat_list.append(address['y']) #위도(latitude)

    time.sleep(0.5)

lat_lng = list(zip(lat_list, lng_list))
name_lat_lng = list(zip(name_list, lat_lng))
info = dict(name_lat_lng)
pprint.pprint(info)

#지도 출력
import folium
map = folium.Map(('37.5511225714939', '126.987867837993'), zoom_start=11) # 남산타워 기준

for i in range(len(name_list)) :
    location = (lat_list[i], lng_list[i])
    text = f'{name_list[i]}<br>{add_list[i]}<br>{tel_list[i]}<br>'
    popup = folium.Popup(text, min_width=50, max_width=200)

    folium.Marker(
        location, 
        popup, 
        icon=folium.Icon(color='pink', icon='glyphicon-road')
    ).add_to(map)

#지도를 HTML로 저장
map.save('data/map_노란통닭.html')