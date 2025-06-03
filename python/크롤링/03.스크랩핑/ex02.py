import requests
url = 'http://nadocoding.tistory.com'

#구글에서 'What is user Agent String' 검색 (접속 브라우저마다 다르다)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

res = requests.get(url, headers=headers)
res.raise_for_status()

with open('data/nadocoding.html', 'w', encoding='utf-8') as f:
    f.write(res.text)