from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "https://www.coupang.com/np/search?component=&q=노트북&channel=user"
browser.get(url)

interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)

    #이전 스크롤높이와 현재 스크롤높이가 같으면 break
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    else:
        prev_height = curr_height
print("스크롤 완료")