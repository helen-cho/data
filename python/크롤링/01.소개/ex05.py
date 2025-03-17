import requests

url = 'http://google.com'
res = requests.get(url)
print(f'{url}:{res.status_code}')

url = 'http://google.com/user'
res = requests.get(url)
print(f'{url}:{res.status_code}')