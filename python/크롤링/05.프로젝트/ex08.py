from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

#1.기상청 홈페이지 이동
url = "https://www.weather.go.kr"
browser.get(url)

def wait_until(xpath):
   WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

#2.전국 클릭
xpath = '//*[@id="content-body"]/div[4]/h2/a'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

#3.어제 클릭
xpath = '//*[@id="content-body"]/div[4]/div/div/div[1]/ul/li[1]/a'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

#4.전국 날씨정보 영역 찾기
xpath = '//*[@id="minmax"]'
wait_until(xpath)

#5.스크랩핑
soup = BeautifulSoup(browser.page_source, 'lxml')

local = soup.find('div', attrs={'id':'minmax'})
es = local.find_all('dl', attrs={'class':re.compile('^po')})
for index, e in enumerate(es):
    title = e.find('dt').get_text()
    red = e.find('span', attrs={'class', 'red'}).get_text()
    blue = e.find('span', attrs={'class', 'blue'}).get_text()
    print(f'{title}:최저({blue})/최고({red})')
