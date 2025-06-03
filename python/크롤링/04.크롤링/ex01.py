from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://naver.com")

#로그인 버튼의 클래스명
e = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
e.click()

browser.back()
browser.forward()
browser.refresh()
browser.back()

#검색어 입력 상자에 '나도코딩'을 입력 후 엔터
e = browser.find_element(By.ID, "query")
e.send_keys("나도코딩")
e.send_keys(Keys.ENTER)

#태그명이 'a'인 모든 태그 검색
es = browser.find_elements(By.TAG_NAME, "a")
for idx, e in enumerate(es):
    link = e.get_attribute("href")
    print(idx+1, link)

#다음 페이지로 이동
browser.get("http://daum.net")

#검색어 상자를 찾아 '나도코딩' 입력
e = browser.find_element(By.NAME, "q")
e.send_keys("나도코딩")

#검색 버튼을 찾아 클릭
e = browser.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]')
e.click()

time.sleep(10)