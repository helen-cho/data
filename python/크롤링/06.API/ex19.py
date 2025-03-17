import requests
from bs4 import BeautifulSoup

file = open('data/data_go_key.txt')
key = file.readlines()
enKey = key[0].strip()
deKey = key[1].strip()

#[인천광역시_정류소 조회]
def getStopName(stopName): #정류장명을 인자로 사용, 그 정류장명를 포함한 모든 정류장 목록을 반환하는 함수
    url = 'http://apis.data.go.kr/6280000/busStationService/getBusStationNmList'
    params ={'serviceKey' : deKey, 'pageNo' : '1', 'numOfRows' : '10', 'bstopNm' : stopName }

    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, 'lxml-xml')
    items = soup.find_all('itemList')
    stop_list = []
    for item in items:
        st_id = item.find('BSTOPID').text #정류장ID
        st_name = item.find('BSTOPNM').text #w정류장명
        #print(st_id, st_name)
        bus_list = getBusNo(st_id)
        stop_list.append({'st_id':st_id, 'st_name':st_name, 'bus_list':bus_list})
    return stop_list

#[인천광역시_정류소 조회]-[정류소경유노선 목록 조회]
def getBusNo(stopId): #정류소ID를 인자로로 그 정류소를 지나가는 버스노선 목록
    url = 'http://apis.data.go.kr/6280000/busStationService/getBusStationViaRouteList'
    params ={'serviceKey' : deKey, 'pageNo' : '1', 'numOfRows' : '10', 'bstopId' : stopId }
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, 'lxml-xml')
    items = soup.select('itemList')
    bus_list = []
    for item in items:
        busNo = item.find('ROUTENO').text
        bus_list.append(busNo)
    return bus_list

if __name__=='__main__':
    stopName = input('정류장명에 포함된 문자열:')
    stop_list = getStopName(stopName)
    for stop in stop_list:
        print(f'정류장ID:{stop['st_id']}, 정류장명:{stop['st_name']}, 경유버스목록:{stop['bus_list']}')