from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import json

def create_soup(query):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    url=f'https://www.daangn.com/kr/buy-sell/?in=서구&search={query}'
    browser.get(url)

    prev_height = browser.execute_script('return document.body.scrollHeight')
    while True:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)
        curr_height = browser.execute_script('return document.body.scrollHeight')
        if prev_height == curr_height:
            print('스크롤완료!')
            break
        prev_height = curr_height

    soup = BeautifulSoup(browser.page_source, 'lxml')
    browser.quit()
    return soup

def search(query):
    soup=create_soup(query)
    es = soup.find_all('a', attrs={'class':re.compile('^_13tpfox6')})
    items = []
    for index, e in enumerate(es):
        title = e.find('h2', attrs={'class':re.compile('^_1b153uwh')}).get_text()
        address= e.find('div', attrs={'class':re.compile('^_1b153uwk')}).get_text().strip()
        price= e.find('div', attrs={'class':re.compile('^_1b153uwi')}).get_text().strip()
        image = e.find('img')['src']
        data = {'no':index+1, 'title':title, 'address':address, 'price':price, 'image':image}
        items.append(data)
    return items

json_data = search('노트북')

#딕션너리 자료형을 문자열로 변환
json_str = json.dumps(json_data, indent=4, ensure_ascii=False)
print(json_str)

#JSON 자료형으로 파일에 저장
with open('data/당근.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False)