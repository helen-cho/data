import requests

res = requests.get('http://nadocoding.tistory.com')
res.raise_for_status()

with open('data/nadocoding.html', 'w', encoding='utf-8') as f:  #구글에서 나도코딩 티스트리검색
    f.write(res.text)