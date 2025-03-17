import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

sect_movie = soup.find('div', attrs={'class':'sect-movie-chart'})
movies = sect_movie.find_all('li')

for movie in movies:
    title = movie.find('strong', attrs={'class':'title'}).get_text()
    link ='http://www.cgv.co.kr' + movie.find('a', attrs={'class':'link-reservation'})['href']
    #link 출력 결과에서 Ctrl + 클릭하면 예매사이트로 접속한다.
    print(title, link)