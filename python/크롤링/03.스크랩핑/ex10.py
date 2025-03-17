import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

overseas = soup.find('div', attrs={'class':'aside_area aside_stock'})
items = overseas.find_all('a')

for item in items:
    title = item.get_text()
    link = url + item['href']
    print(title, link)