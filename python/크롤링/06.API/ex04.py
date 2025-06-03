import requests
from bs4 import BeautifulSoup
import re
import pprint #dictionary 형을 보기 좋게 출력한다.

#주소, 업체명, 전화번호 수집
def getInfo():
    url = 'https://www.wikitree.co.kr/articles/217101'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    #업체명을 저장할 리스트
    name_list = []
    for e in soup.select('strong'):
        if '회' in e.text: #e요소에 '회'가 있으면
            name = e.text.split('회 ')[-1] #'회 '를 기준으로 나누어 배열에 저장 후 마지만 요소를 수집한다.
            name_list.append(name)

    #모든 p 태그들을 수집한다.
    p =soup.select('p')
    #전화번호를 저장할 list
    tel_list = []
    #주소를 저장할 list
    add_list = []

    for i in range(len(p)):
        #정규식 {2,} 숫자 2자리이상, {3,} 숫자 3자리이상, {4} 숫자 4자리
        if re.match('[0-9]{2,}-[0-9]{3,}-[0-9]{4}', p[i].text):
            tel = p[i].text
            tel_list.append(tel)
            #주소를 수집하여 공백을 제거한다.
            add = p[i+1].text.strip()
            add_list.append(add)

    #zip 두개의 list를 묶어준다.
    add_tel = list(zip(add_list, tel_list))
    name_add_tel = list(zip(name_list, add_tel))
    #dictionary로 변경한다.
    info = dict(name_add_tel)
    return info, name_list, tel_list, add_list

if __name__ == '__main__':
    info = getInfo()
    pprint.pprint(info)