import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

popular = soup.find('div', attrs={'class':'aside_area aside_popular'})
items = popular.find_all('a')
for item in items:
    print(item.get_text())