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

cnt = 0
for index, item in enumerate(items):
    name=item.find("div", attrs={"class":"name"}).get_text()
    
    if '삼성' in name:  #애플 제품 제외
       print("<삼성성상품 제외합니다>")
       print("-" * 100)
       continue
    price=item.find("strong", attrs={"class", "price-value"}).get_text()
    
    rate = item.find("em", attrs={"class":"rating"})  #상품평평점
    if rate:
        rate = rate.get_text()
    else:
        print("<평점 없는 상품 제외합니다>")
        print("-" * 100)
        continue
    
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})  #평점수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
    else:
        print("<평점 수 없는 상품 제외합니다>")
        print("-" * 100)
        continue

    #평점 4.5 이상, 리뷰 100개 이상만 조회
    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        cnt += 1
        print(index+1, name.strip(), price, rate, rate_cnt)
        print("-" * 100)
        link = item.find('a', attrs={"class":"search-product-link"})['href']

        print(f'상품이름:{index}.{name}')
        print(f'상품가격:{price}원')
        print(f'상품품평점:{rate}점({rate_cnt}개)')
        print("바로가기:{}".format("https://www.coupang.com" + link))
        print("-" * 100)
print(f'조건을 만족하는 상품수:{cnt}개')