from selenium import webdriver
import re
from bs4 import BeautifulSoup
import os
import requests

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("window-size=1920x1080")
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)

url = "https://www.coupang.com/np/search?component=&q=노트북&channel=user"
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')
items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

#'product' 폴더가 존재하지 않으면 새로운 'product'폴더를 생성
if not os.path.exists("product"):
    os.mkdir("product")

cnt = 0
for index, item in enumerate(items):
    #이미지 태그의 src 속성값을 저장한다.
    image=item.find("img", attrs={"class":"search-product-wrap-img"})["src"]

    #이미지 주사에 'thumbnail'이 포함된 경우
    if 'thumbnail' in image:
        cnt += 1
        image = "https:" + image

        #이미지를 요청
        res_image = requests.get(image)
        #응답 상태 코드를 확인하고, 오류가 발생하면 예외를 발생
        res_image.raise_for_status()

        #이미지를 파일로 저장장
        with open("product/product{}.jpg".format(index+1), "wb") as f:
            f.write(res_image.content)

print(f'이미지 다운로드 완료:{cnt}개')