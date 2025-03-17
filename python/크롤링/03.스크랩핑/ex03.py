import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

print('1:', soup.title)
print('2:',soup.title.get_text())

#처음 발견되는 a element를 반환
print('3:', soup.a)

#a element의 속성들 정보 출력
print('4:', soup.a.attrs)

#a element의 href 속성 '값' 정보 출력
print('5:', soup.a['href'])