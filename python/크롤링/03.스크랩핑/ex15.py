import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?sca_esv=1eda6e0add178775&q=송중기&udm=2&...&dpr=0.8'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
           'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3'}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
with open('song.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

images = soup.find_all('a', attrs={"class":"EZAeBe"})
print(len(images))

for idx, image in enumerate(images):
    title = image.find("div", attrs={"class":"toI8Rb OSrXXb"})
    print('-' * 100)
    print(idx+1, title.get_text())
    print(image['href'])