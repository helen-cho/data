import requests
from bs4 import BeautifulSoup
import os

url='https://www.hollys.co.kr/menu/espresso.do'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

ul = soup.find('ul', attrs={'class':'menu_list01 mar_t_40'})
es = ul.find_all('img')

if not os.path.exists("hollys"):
    os.mkdir("hollys")

for index, e in enumerate(es):
    url = 'http:' + e['src']

    res_image = requests.get(url)
    res_image.raise_for_status()
    with open("hollys/menu{}.jpg".format(index + 1), "wb") as f:
        f.write(res_image.content)

    print(f'{index}:{url}')