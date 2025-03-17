from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

#1.기상청 홈페이지 이동
url = 'https://www.coffeebeankorea.com/store/store.asp'
browser.get(url)

#2. Store ID 구하기
store = browser.find_element(By.ID, 'storeListUL')
es = store.find_elements(By.TAG_NAME, 'li')

store_id = []
for e in es:
    id = e.get_attribute('data-no')
    store_id.append(id)
print(len(store_id))
