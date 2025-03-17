from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def browser_execute():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=options)
    url = "https://land.naver.com/"
    browser.get(url)

    e = browser.find_element(By.ID, "queryInputHeader")
    e.send_keys("루원시티")
    e.send_keys(Keys.ENTER)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(browser.page_source, "lxml")

    es = soup.find_all("a", attrs={"class":"item_link"})
    for index, e in enumerate(es):
        print(f'=================== 정보{index+1} ===================')
        title = e.find("div", attrs={"class":"title"})
        address = e.find("div", attrs={"class":"address"})
        type = e.find("strong", attrs={"class":"type"})
        info = e.find("div", attrs={"class":"info_area"})
        specs = info.find_all("span", attrs={"class":"spec"})
        print(f'{index}:{title.get_text()}')
        print(address.get_text())
        print(type.get_text())
        for spec in specs:
            print(spec.get_text() + "|", end="")
        print('')
    browser.quit()
#함수 실행
browser_execute()