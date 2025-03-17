import requests

file = open('data/data_go_key.txt')
key = file.readlines()
enKey = key[0].strip()
deKey = key[1].strip()

url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute'
params ={'serviceKey' : deKey, 'busRouteId' : '' }

response = requests.get(url, params=params)
print(response.content)