
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

#1. 네이버 이동
browser.get("http://naver.com")

#2. 로그인 버튼 클릭
e = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
e.click()

#3. 아이디, 비밀번호 입력
browser.find_element(By.ID, "id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("naver_pw!")

#4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()
time.sleep(3)

#5. 새로운 id를 입력
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("my_id")

#6. 현재 html 모든 정보 출력
print(browser.page_source)

#7. 브라우저 종료
browser.close() #현재 탭 종료
browser.quit() #브라우저 종료

time.sleep(10)
