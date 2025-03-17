from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url='https://www.gmarket.co.kr/n/search?keyword=%ed%96%a5%ec%88%98&k=53&p=1'
browser.get(url)

prev_height = browser.execute_script('return document.body.scrollHeight')
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height: break
    prev_height = curr_height

from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(browser.page_source, 'lxml')
es = soup.find_all('div', attrs={'class':re.compile('^box__item-container')})

for index, e in enumerate(es):
    #상품 이름
    title = e.find('span', attrs={'class':'text__item'})
    if title:
        title = title.get_text()
    else:
        title = ''
    
    #상품 이미지 주소
    image = e.find('img')
    if image:
        image = 'https:' + image['src']

    #상품 가격
    price = e.find('strong', attrs={'class':'text text__value'})
    if price:
        price = price.get_text()
    else:
        price = ''

    #구매건수    
    pay_count = e.find('li', attrs={'class':re.compile('list-item__pay-count$')})
    if pay_count:
        pay_count = re.sub('구매|건', '', pay_count.get_text()).strip()
    else:
        pay_count = '0'

    #상품정보 출력
    print(f'{index+1}.{title}')
    print(f'이미지주소:{image}')
    print(f'상품가격:{price}')
    print(f'구매건수:{pay_count}')
    print('-' * 100)

browser.quit()