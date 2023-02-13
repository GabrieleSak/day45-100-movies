from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movie_list_web_page = response.text

soup = BeautifulSoup(movie_list_web_page, "html.parser")


movies = soup.find_all(name="h3", class_='title')

movie_list = []

for movie in movies:
    movie_title = movie.getText()
    movie_list.insert(0, movie_title)

print(movie_list)

with open('movies.txt', 'w', encoding="utf-8") as f:
    for movie in movie_list:
        f.write(movie)
        f.write('\n')

