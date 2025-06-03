import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
res = requests.get(url)

res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

#CVG 전체 영화목록 출력
movies = soup.find_all('strong', attrs={'class':'title'})
for movie in movies:
    print(movie.get_text())  #movie.getText() 동일