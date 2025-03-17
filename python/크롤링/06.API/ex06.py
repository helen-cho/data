from ex05 import getLatLng
import folium #folium은 파이썬에서 사용할 수 있는 지도 시각화 라이브러리

#지도출력
def getMap():
    name_list, tel_list, add_list,  lat_list, lng_list = getLatLng()

    #남산타워 기준
    lat = 37.5511225714939
    lng = 126.987867837993
    map = folium.Map((lat, lng), zoom_start=12, width=750, height=500)
    for i in range(len(name_list)):
        location = (lat_list[i], lng_list[i])
        text = f'{i}.{name_list[i]}<br>{add_list[i]}<br>{tel_list[i]}<br>'
        popup = folium.Popup(text, max_width=200)
        folium.Marker(
            location,
            popup,
            icon=folium.Icon(color='blue', icon='glyphicon-road') #https://getbootstrap.com/docs/3.3/components/
        ).add_to(map)

    #지정한 위경도 위치에 원을 지도 해상도에 맞춰서 그려줌(원 그기가 변경됨됨)
    folium.CircleMarker(
        [lat_list[18], lng_list[18]],
        radius=100, #반경 100미터
        color='yellow',
        fill_color='yellow',
        popup='Circle',
        tooltip='tooltip'
    ).add_to(map)
    #지도를 HTML로 저장
    map.save('data/map_식신로드.html')

if __name__ == '__main__':
    getMap()