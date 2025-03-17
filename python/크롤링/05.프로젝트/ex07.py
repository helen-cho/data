from selenium import webdriver
from bs4 import BeautifulSoup
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

#[기상청]-[전국]
url='https://www.weather.go.kr/w/index.do'
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')

local = soup.find('div', attrs={'id':'weather2'})
es = local.find_all('dl', attrs={'class':re.compile('^po')})
for index, e in enumerate(es):
    title = e.find('dt').get_text()
    temp = e.find('span').get_text()
    weather = e.find('i').get_text()
    print(title, temp, weather)