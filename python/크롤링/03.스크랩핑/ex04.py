import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')


chart = soup.find('div', attrs={'class':'sect-movie-chart'})
rank1 = chart.find('strong', attrs={'class':'rank'})
print('1:', rank1.getText())

rank1_sibling = rank1.find_next_sibling('a')
print('2:', 'http://cgv.co.kr' + rank1_sibling['href'])

rank1_grand=rank1.parent.parent
title1 = rank1_grand.find('strong', attrs={'class':'title'} )
print('3:', title1.getText())