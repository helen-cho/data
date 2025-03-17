import requests

url = 'http://google.com/user'
res = requests.get(url)
print(res)

#만약 에러가 있다면 멈춰주고 에러를 알려준다
res.raise_for_status()

url = 'http://google.com'
res = requests.get(url)
print(res)
