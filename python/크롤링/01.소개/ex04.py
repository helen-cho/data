import requests

url = 'http://google.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}
param = {'q' : 'python'}
res = requests.get(url, headers=headers, params=param)

print(f'1.res.request.path_url:{res.request.path_url}')
print(f'2.res.request.method:{res.request.method}')
print(f'3.res.request.headers:{res.request.headers['User-Agent']}')
print(f'4.res.encoding:{res.encoding}')