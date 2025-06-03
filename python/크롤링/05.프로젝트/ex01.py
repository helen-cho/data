import requests
from bs4 import BeautifulSoup

def scrap_weather():
    url ='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=오늘의 날씨'
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    #어제보다 1.1° 낮아요  비
    cast = soup.find('p', attrs={'class':'summary'}).get_text()

    #현재온도
    temp = soup.find('div', attrs={'class':'temperature_text'})
    curr_temp = temp.strong.contents[1]
    celsius = temp.strong.contents[2].get_text()
    curr_temp = curr_temp + celsius

    #최저온도 / 최고온도
    lowest = soup.find('span', attrs={'class':'lowest'}).contents[1]
    highest = soup.find('span', attrs={'class':'highest'}).contents[1]

    #오전 / 오후 강수확률
    rainfall = soup.find_all('span', attrs={'class':'weather_inner'})
    moring = rainfall[0].find('span', attrs={'class':'rainfall'}).get_text()
    afternoon = rainfall[1].find('span', attrs={'class':'rainfall'}).get_text()

    #미세먼지 / 초미세먼지
    chart = soup.find('ul', attrs={'class':'today_chart_list'})
    level = chart.find_all('li', attrs={'class':'item_today level1'})
    level0 = level[0].find('span', attrs={'class':'txt'}).get_text()
    level1 = level[1].find('span', attrs={'class':'txt'}).get_text()

    print('[오늘의 날씨]')
    print('-' * 50)
    print(cast)
    print(f'현재 {curr_temp} (최저 {lowest} /초고 {highest})')
    print(f'오전 강수확률 {moring} / 오후 강수확률 {afternoon}\n')
    print(f'미세먼지 {level0}')
    print(f'초미세먼지 {level1}')
    print('-' * 50)

if __name__ == '__main__':
    scrap_weather()