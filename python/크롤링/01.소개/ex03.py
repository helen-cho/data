import requests

url='https://www.google.com/search?sca_esv=61c64a259e7d732d&sxsrf=AHTn8zq2ITAEkXXhAAaZiXxykYFfwnVnoQ:1738328085951&udm=2&fbs=ABzOT_CZsxZeNKUEEOfuRMhc2yCI6hbTw9MNVwGCzBkHjFwaK53DgNHTMxn53_XGiUHS2MuRVDP60KUbqm2OQomhT296Q8j4L9BFGBcQ0mIumXcz3BBM3q-d0sHsYe1ngZ2czGnYwgrFuuarr7CQPUFzsI-b-QWXiPkrm5A200zHsZfCRKUUzvIl3L1i9aXthG0ZYLCG2BHOT9vS_FgVrP8t4cL1xrMRIw&sa=X&ved=2ahUKEwi5vcPggKCLAxVT1jQHHRypEHoQtKgLegQIIRAB&biw=1280&bih=665&dpr=1.5'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}
param = {'q' : '조인성'}
res = requests.get(url, headers=headers, params=param)

with open('data/ex03.html', 'w', encoding='utf-8') as file:
    file.write(res.text)

