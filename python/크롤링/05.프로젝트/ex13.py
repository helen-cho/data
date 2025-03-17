from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import csv

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

#커피빈 전국 매장의 Store ID를 구하는 함수
def store_id(url):
    #1.커피빈 매장찾기 페이지로 이동
    browser.get(url)
    #2. 커피매장 정보영역 찾기
    store = browser.find_element(By.ID, 'storeListUL')
    es = store.find_elements(By.TAG_NAME, 'li')
    #3. Store ID(data-no)를 구해 Return한다.
    store_id = []
    for e in es:
        id = e.get_attribute('data-no')
        store_id.append(id)
    return store_id

#전국 Store ID를 받아 매장 정보를 구하는 함수수
def store_info(store_id):
    f = open('data/커피빈.csv', "w", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)
    #Store ID 갯수만큼 반복복
    for index, id in enumerate(store_id):
        #1.커피빈 매장찾기 페이지로 이동
        browser.get(url)
        browser.execute_script(f'storePop2({id})')
        time.sleep(1)
        #2.스크랩핑
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        #매장이름
        store_name_h2 = soup.select('div.store_txt > h2')
        store_name = store_name_h2[0].string
        #매장정보
        store_info = soup.select('div.store_txt > table.store_table > tbody > tr > td')
        #매장이름
        store_address = list(store_info[2])[0]
        #매장전화
        store_phone = store_info[3].string
        #매장정보 출력, 파일에 저장장
        print(f'{index+1}.{store_name} | {store_address} | {store_phone}')
        data = [index+1, store_name, store_address, store_phone]
        writer.writerow(data)
    
if __name__ == '__main__':
    url = 'https://www.coffeebeankorea.com/store/store.asp'
    store_id = store_id(url)
    store_info(store_id)