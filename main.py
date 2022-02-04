from bs4 import BeautifulSoup
import requests

url ="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
# print(all_movies)

movies_title = [movie.getText() for movie in all_movies]
movies = movies_title[::-1]
# for n in range(len(movies_title)-1,-1,-1):
#     print(movies_title[n])

with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
