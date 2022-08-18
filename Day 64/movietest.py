import requests
from pprint import pprint

API_KEY = "598b3abafb89e98aabc3bcde425d6353"

def get_movie():
    # params = {
    #     "query": "Bambi",
    #     "api_key": API_KEY
    # }
    headers = {
        'Authorization': "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1OThiM2FiYWZiODllOThhYWJjM2JjZGU0MjVkNjM1MyIsInN1YiI6IjYyZTRhNDgwNWIxMjQwMDA2MTlhNDc0YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bXIxDjrJHbQV43wpiv0f8uj03-7ZlzEtty3lgoI2yuI",
        "Content-Type": "application/json;charset=utf-8"
    }
    # request = requests.get(url="https://api.themoviedb.org/3/movie/550?api_key=598b3abafb89e98aabc3bcde425d6353")
    # print(request)
    # REQUEST_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1OThiM2FiYWZiODllOThhYWJjM2JjZGU0MjVkNjM1MyIsInN1YiI6IjYyZTRhNDgwNWIxMjQwMDA2MTlhNDc0YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bXIxDjrJHbQV43wpiv0f8uj03-7ZlzEtty3lgoI2yuI"
    # request = requests.get(f'https://www.themoviedb.org/authenticate/{REQUEST_TOKEN}?redirect_to=http://www.yourapp.com/approved')
    # request = requests.get("https://api.themoviedb.org/3/authentication/token/new?api_key=598b3abafb89e98aabc3bcde425d6353")
    #
    # print(request.text)
    MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
    movie_id = 1362
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US")
    data = response.json()
    print(data)
    # for film in data["results"]:
    #     print(film["original_title"])
    #     print(film["release_date"])
    # data = response.json()["results"]
get_movie()