import requests
from bs4 import BeautifulSoup
from datetime import datetime

file = open('data/data_go_key.txt')
key = file.readlines()
enKey = key[0].strip()
deKey = key[1].strip()

#[인천광역시_버스노선 조회]-[노선버스 목록조회]
def getBusInfo(busNo): #버스번호를 인자로 버스정보(버스ID, 첫차시간, 막차시간, 배차간격) 반환 함수
    url = 'http://apis.data.go.kr/6280000/busRouteService/getBusRouteNo'
    params ={'serviceKey' : deKey,'pageNo':1, 'numOfRows':10, 'routeNo' : busNo }

    response = requests.get(url, params=params)
    response.encoding='UTF-8'
    soup = BeautifulSoup(response.text, 'lxml-xml')
    items = soup.select('itemList')
    busInfo = ''
    for item in items:
        if busNo == item.find('ROUTENO').text:
            busId = item.find('ROUTEID').text
            datetime_format = '%H%M'
            firstTime = datetime.strptime(item.find('FBUS_DEPHMS').text, datetime_format)
            first = datetime.strftime(firstTime, '%H시%M분')
            lastTime =datetime.strptime(item.find('LBUS_DEPHMS').text, datetime_format)
            last = datetime.strftime(lastTime, '%H시%M분')
            gap = item.find('MAX_ALLOCGAP').text
            busInfo ={'busId':busId, 'first':first, 'last':last, 'gap':gap}
            break
    return busInfo

#[인천광역시_버스노선 조회]
def getBusRoute(busId): #버스ID를 인자로 정류장이름 목록을 반환하는 함수
    url = 'http://apis.data.go.kr/6280000/busRouteService/getBusRouteSectionList'
    params ={'serviceKey' : deKey, 'pageNo' : '1', 'numOfRows' : '200', 'routeId' : busId }
    response = requests.get(url, params=params)
    response.encoding='UTF-8'
    soup = BeautifulSoup(response.text, 'lxml-xml')
    items = soup.select('itemList')
    stop_list = []
    for item in items:
        stopName = item.find('BSTOPNM').text
        stop_list.append(stopName)
    return stop_list
    
if __name__=='__main__':
    busNo = input('조회할 버스번호를 입력하세요 :')
    busInfo = getBusInfo(busNo)
    if busInfo != '':
        print(f'첫차시간:{busInfo['first']} / 막차시간:{busInfo['last']} / 배차간격: {busInfo['gap']}분')
        stop_list = getBusRoute(busInfo['busId'])
        print(f'정차정거장:{stop_list[0:3]}~{stop_list[-3:]}')
        print('정거장수:', len(stop_list))
    else: print(f'{busNo}번 버스가 존재하지 않습니다.')