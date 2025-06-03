from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

#1.기상청 홈페이지 이동
url = 'https://www.coffeebeankorea.com/store/store.asp'
browser.get(url)

#2.storePop2() 함수 실행
browser.execute_script('storePop2(31)')
time.sleep(1)

#3.스크랩핑
soup = BeautifulSoup(browser.page_source, 'html.parser')

store_name_h2 = soup.select('div.store_txt > h2')
store_name = store_name_h2[0].string

store_info = soup.select('div.store_txt > table.store_table > tbody > tr > td')
store_address = list(store_info[2])[0]

store_phone = store_info[3].string
print(f'{store_name} | {store_address} | {store_phone}')