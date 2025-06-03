from selenium import webdriver

options = webdriver.ChromeOptions()

#브라우저 창 항상 유지
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

#브라우저 창 최대화
browser.maximize_window()

#네이버 항공권 페이지 이동
url = "https://flight.naver.com/"
browser.get(url)

browser.get_screenshot_as_file("data/fight.png")
print("프로그램종료")
browser.quit()