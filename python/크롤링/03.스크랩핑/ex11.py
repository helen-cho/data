import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

news = soup.find('div', attrs={'class':'news_area _replaceNewsLink'})
items = news.find_all('a')

for item in items:
    title = item.get_text()
    link = url + item['href']
    print('-' * 100)
    print(title)
    print(link)