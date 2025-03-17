import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def scrap_news(url):
    soup = create_soup(url)
    news_list = soup.find('ul', attrs={'class':'sa_list'}).find_all('li', limit=3)
    for index, news in enumerate(news_list):
        title = news.find('strong', attrs={'class':'sa_text_strong'}).get_text()
        link = news.find('a')['href']
        print(f'{index+1}. {title}')
        print(f'  (링크: {link})')

if __name__ == '__main__':
    print('[IT/과학] 뉴스')
    url ='https://news.naver.com/section/105'
    scrap_news(url)

    print()
    print('[경제] 뉴스')
    url = 'https://news.naver.com/section/101'
    scrap_news(url)

    print('[생활/문화화] 뉴스')
    url = 'https://news.naver.com/section/103'
    scrap_news(url)