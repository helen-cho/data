import requests

url = 'http://google.com/user'
res = requests.get(url, timeout=0.001)
print(res)