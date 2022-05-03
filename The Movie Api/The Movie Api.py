# themovied.org => film ve dizi arşivi
# themoviedb'nin sunduğu api
# anaktar kelimeye göre arama
# en popüler film liste
# vizyondaki film listesi

import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "3dd523dae9ed6e440785e0dcbe80667a"

    def getPopulerMovie(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movieApi = theMovieDb()

while True:
    secim = input("1-Popular Movies\n2-Search Movies\n3-Exit\nSeçiminiz: ")

    if secim == "3":
        break
    else:
        if secim == "1":
            i = 1
            movies = movieApi.getPopulerMovie()
            for movie in movies['results']:
                print(i)
                i = i + 1
                print(movie['title'])
        
        if secim == "2":
            keyword = input("Keyword: ")
            movies = movieApi.getSearchResults(keyword)
            for movie in movies['results']:
                print(movie['name'])


 