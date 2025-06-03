from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

#1.기상청 홈페이지 이동
url = "https://www.weather.go.kr"
browser.get(url)

#2.전국 클릭
xpath = '//*[@id="content-body"]/div[4]/h2/a'
e = browser.find_element(By.XPATH, xpath)
e.click()
time.sleep(1)

#3.예보 클릭
xpath = '//*[@id="content-body"]/div[4]/div/div/div[1]/ul/li[3]'
e = browser.find_element(By.XPATH, xpath)
e.click()
time.sleep(1)

#4.요일선택
for i in range(1, 8):
   xpath = f'//*[@id="local-weather"]/div/div[{i}]/h3/a'
   e = browser.find_element(By.XPATH, xpath)
   print(f'---------- {e.text.replace('\n', '')} ----------')
   e.click()
   time.sleep(1)

   #5.스크랩핑
   soup = BeautifulSoup(browser.page_source, 'lxml')

   local = soup.find('div', attrs={'id':'weather'})
   es = local.find_all('dl', attrs={'class':re.compile('^po')})
   for index, e in enumerate(es):
       title = e.find('dt').get_text()
       temp = e.find('span').get_text()
       weather = e.find('i').get_text()
       print(f'{title}:{temp}도({weather})')