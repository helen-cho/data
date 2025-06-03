from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import os

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://www.hanbit.co.kr/'
browser.get(url)

search = browser.find_element(By.CSS_SELECTOR, '#top_search > a')
search.click()
time.sleep(2)

query = '자바'
text = browser.find_element(By.CSS_SELECTOR, '#keyword_str')
text.send_keys(query)
text.send_keys(Keys.ENTER)
time.sleep(2)

from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, "lxml")

div = soup.find('div', attrs={'class':'ser_list_wrap'})
es = div.find_all('li', attrs={'class':'ser_bg'})

#'books' 폴더가 없으면 새로 생성
if not os.path.exists('books'):
    os.mkdir('books')

for index, e in enumerate(es):
    title = e.find('strong', attrs={'class':'ser_text_title'})
    title = title.get_text()
    authors = e.find('span', attrs={'class':'ser_text_sub2'})
    authors = authors.get_text().split('/')[0].strip()
    price = e.find('span', attrs={'class':'ser_text_point'})
    image = e.find('img')['src']
    image = 'https://www.hanbit.co.kr/' + image

    #이미지를 로컬에 저장
    res_image = requests.get(image)
    res_image.raise_for_status()
    
    with open(f'books/image{index}.jpg', 'wb') as file:
        file.write(res_image.content)

    price = price.get_text()
    print(f'제목:{index}.{title}')
    print(f'저자:{authors}')
    print(f'가격:{price}')
    print('-' * 100)