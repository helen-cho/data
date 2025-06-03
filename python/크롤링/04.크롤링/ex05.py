from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("window-size=1920x1080")
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')

browser = webdriver.Chrome(options=options)

#구글에서 user agent string 검색 후 what is my user agent 클릭
url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

detected_value = browser.find_element(By.ID, "detected_value")
print(detected_value.text)

browser.quit()