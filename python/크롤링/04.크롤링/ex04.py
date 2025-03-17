from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)

url = "https://flight.naver.com/"
browser.get(url)

browser.get_screenshot_as_file("data/google.png")
print("프로그램종료")