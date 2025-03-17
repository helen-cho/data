from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#브라우저 창 항상 유지
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

#브라우저 창 최대화
browser.maximize_window()

#1.네이버 항공권 페이지 이동
url = "https://flight.naver.com/"
browser.get(url)

#잠시 기다리는 시간 지정(초)
wait = 2

#2.가는 날 선택
e = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
e.click()
time.sleep(wait)

#3.이번달 25일 선택
es = browser.find_elements(By.XPATH, '//b[text()="25"]')
es[0].click()
time.sleep(1)

#4.이번달 26일 선택
es = browser.find_elements(By.XPATH, '//b[text()="26"]')
es[0].click()
time.sleep(wait)

#5.도착지 선택
e = browser.find_element(By.XPATH, '//b[text()="도착"]')
e.click()
time.sleep(wait)

#6.제주 선택
e = browser.find_element(By.XPATH, '//button[contains(text(), "제주")]')
e.click()

#첫 번째 결과를 출력할 때까지 최대 10초 기다린다.
first = '//*[@id="__next"]/div/main/section/div/div/div/div/a[1]/div/button[1]'
try: 
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, first)))

    #첫 번째 결과 출력
    e = browser.find_element(By.XPATH, first)
    print(e.text)
finally:
    browser.quit()