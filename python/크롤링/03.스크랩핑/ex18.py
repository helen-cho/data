import requests
from bs4 import BeautifulSoup

query = '파이썬'
url=f'https://www.hanbit.co.kr/search/search_list.html?keyword={query}'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
           'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3'}
res = requests.get(url, headers=headers)

res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

ul = soup.find('div', attrs={'class':'ser_list_wrap'})
print(ul)
es = ul.find_all('li', attrs={'class', 'ser_bg'})

print(f'갯수:{len(es)}')
for index, e in enumerate(es):
    title = e.find('strong', attrs={'class':'ser_text_title'})
    print(title)