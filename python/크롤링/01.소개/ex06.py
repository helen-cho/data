import requests

url='https://ssl.pstatic.net/melona/libs/1524/1524564/386e95af7ed41e37832b_20250103143458551.jpg'
res = requests.get(url)

with open('data/naver.jpg', "wb") as file:
    file.write(res.content)