import requests
import json


class Movie:
    def __init__(self):
        self.api_url="https://api.themoviedb.org/3/"
        self.api_key = "de0a65be21166238a02042a2dfa38a6f"
        self.page = 1

    def getPopulars(self):
        response = requests.get(f"{self.api_url}movie/popular?api_key={self.api_key}&page={self.page}")
        return response.json()
    def countPage(self):
        self.page+=1
    def nowPlaying(self):
        response = requests.get(f"{self.api_url}movie/now_playing?api_key={self.api_key}&page=2")
        return response.json()
    
    def getFilm(self,name):
        response = requests.get(f"{self.api_url}search/movie?api_key={self.api_key}&query={name}&page=1")
        return response.json()

film = Movie()

while True:
    ch = input("1- Popular Films\n2- Now Playing Films\n3- Get Film\n0- Exit\nChose: ")
    if ch=="1":
        print(f"{film.page}".center(50,"*"))
        result = film.getPopulars()
        for movie in result["results"]:
            print(movie["title"]+"--"+str(movie["vote_average"]))
        film.countPage()
    elif ch=="2":
        result = film.nowPlaying()
        for movie in result["results"]:
            print(movie["title"]+"--"+str(movie["vote_average"]))
    elif ch=="3":
        name = input("Enter name: ")
        print()
        result = film.getFilm(name)
        for movie in result["results"]:
            print(movie["title"]+"--"+str(movie["vote_average"]))

    elif ch=="0":
        break
