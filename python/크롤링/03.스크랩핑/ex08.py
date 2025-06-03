import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

items = soup.find('tbody', attrs={'id':'_topItems1'})

rank1 = items.find('tr')
print(rank1.a.get_text())

# next_sibling 다음 엘리먼트로 넘기는 메소드는 개행이 존재하기 때문에 두 번 넘겨야한다.
rank2 = rank1.next_sibling.next_sibling
print(rank2.a.get_text())

#find_next_sibling() 함수를 이용하면 개행문자가 있는지 확인할 필요가없다.
rank3 = rank2.find_next_sibling('tr')
print(rank3.a.get_text())

rank2 = rank3.find_previous_sibling('tr')
print(rank2.a.get_text())

#parent 메서드는 rank1의 부모 관련 요소를 가져온다. 
print('-' * 100)
parent = rank1.parent
rank1 = parent.find('tr')
print(rank1.a.get_text())

#find_next_siblings() 함수는 rank1의 형제 요소들을 가져온다.
print('-' * 100)
siblings = rank1.find_next_siblings('tr')
print(len(siblings))
rank2 = siblings[0]
print(rank2.find('a').get_text())