from selenium import webdriver
import re
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("window-size=1920x1080")
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)

url = "https://www.coupang.com/np/search?component=&q=노트북&channel=user"
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')
items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

for index, item in enumerate(items):
    #상품이름
    name=item.find("div", attrs={"class": "name"}).get_text()
    
    #상품가격
    price=item.find("strong", attrs={"class", "price-value"}).get_text()
    
    #상품평점
    rate = item.find("em", attrs={"class": "rating"})
    if rate: 
        rate = rate.get_text()
    else: 
        rate = "평점없음"
    
    #상품평
    rate_cnt = item.find("span", attrs={"class": "rating-total-count"})
    if rate_cnt: 
        rate_cnt = rate_cnt.get_text()
    else: 
        rate_cnt = "상품평없음"
    
    print(f'{index+1}.{name.strip()}')
    print(f'상품가격:{price}원')
    print(f'상품평점:{rate}')
    print(f'상품평:{rate_cnt[1:-1]}개')
    print("-" * 100)