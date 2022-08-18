import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

movie_list = soup.find_all(name="h3", class_="title")

movie_list = [movie.get_text() for movie in movie_list]
# print(len(movie_list))
# print(movie_list[len(movie_list):0:-1])
# print(movie_list)
# for i in movie_list[len(movie_list):0:-1]:
#     print(i)
#     print("\n")
# print(movie_list[0])

# movie_list = [for movie in movie_list]

with open("movies.txt", "w") as file:
    for i in movie_list[len(movie_list):0:-1]:
        file.write(i)
        file.write("\n")
    file.write(movie_list[0])



