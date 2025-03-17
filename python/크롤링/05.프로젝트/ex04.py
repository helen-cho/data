import ex01, ex02, ex03

if __name__ == '__main__':
    ex01.scrap_weather()

    print('[IT/과학] 뉴스')
    url ='https://news.naver.com/section/105'
    ex02.scrap_news(url)

    ex03.scrap_english()
