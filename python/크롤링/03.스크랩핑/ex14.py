import requests
from bs4 import BeautifulSoup
import os

url="http://www.cgv.co.kr/movies/?lt=1&ft=0"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

chart = soup.find("div", attrs={"class":"sect-movie-chart"})
movies = chart.find_all("div", attrs={"class":"box-image"})

if not os.path.exists("movies"):
    os.mkdir("movies")

for index, item in enumerate(movies):
    image = item.find('img')["src"]
    res_image = requests.get(image)
    res_image.raise_for_status()
    with open("movies/movie{}.jpg".format(index + 1), "wb") as f:
        f.write(res_image.content)