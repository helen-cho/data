import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

sect_movie = soup.find('div', attrs={'class':'sect-movie-chart'})
movies = sect_movie.find_all('li')

total_percent = 0
for movie in movies:
    percent = movie.find('strong', attrs={'class':'percent'})
    percent = percent.span.get_text()
    value = percent.replace('%', '')
    total_percent += float(value)

print(f'평균 예매율:{total_percent / len(movies)}')