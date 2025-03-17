import requests

res = requests.get('https://www.google.com/search?sca_esv=61c64a259e7d732d&sxsrf=AHTn8zq2ITAEkXXhAAaZiXxykYFfwnVnoQ:1738328085951&q=%EC%86%A1%EC%A4%91%EA%B8%B0&udm=2&fbs=ABzOT_CZsxZeNKUEEOfuRMhc2yCI6hbTw9MNVwGCzBkHjFwaK53DgNHTMxn53_XGiUHS2MuRVDP60KUbqm2OQomhT296Q8j4L9BFGBcQ0mIumXcz3BBM3q-d0sHsYe1ngZ2czGnYwgrFuuarr7CQPUFzsI-b-QWXiPkrm5A200zHsZfCRKUUzvIl3L1i9aXthG0ZYLCG2BHOT9vS_FgVrP8t4cL1xrMRIw&sa=X&ved=2ahUKEwi5vcPggKCLAxVT1jQHHRypEHoQtKgLegQIIRAB&biw=1280&bih=665&dpr=1.5')
print(res)

with open('data/ex01.html', 'w', encoding='utf-8') as file:
    file.write(res.text)