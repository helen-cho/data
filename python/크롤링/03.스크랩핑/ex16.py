import requests
from bs4 import BeautifulSoup

url = 'https://dportal.kdca.go.kr/pot/bbs/BD_selectBbsList.do?q_bbsSn=1008'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

soup = BeautifulSoup(res.text, 'lxml')
with open('data/kdca.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())