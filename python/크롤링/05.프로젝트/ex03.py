import requests
from bs4 import BeautifulSoup
import re

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

#[네이버]-[해커스]-[해커스토익]-[기초영어/회화][매일영어회화학습]
def scrap_english():
    print('[오늘의 영어 회화]')
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=...&logger_kw=...'
    soup = create_soup(url)

    sentences = soup.find_all('div', attrs={'id':re.compile('^conv_kor_t')})

    print('(영어지문)')
    #8문장이 있다고 가정할 때 index 기준 4~7까지 잘라서 출력
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print()

    print('(한글지문)')
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())

if __name__ == '__main__':
    scrap_english()