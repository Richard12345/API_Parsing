import json

import omdb
import pandas as pd
import requests
from pprint import PrettyPrinter



pp = PrettyPrinter()

apiKey = '1d094a12'

#Fetch Movie Data
#Fetch Movie Data with Full Plot
data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
year = ''
movie = 'Thor'
params = {
    's':movie,
    'type':'movie',
    'y':year,
    'plot':'full'
}
response = requests.get(data_URL,params=params).json()
print (response)

responseText = requests.get(data_URL,params=params).raw

json_data= {r"Search":[{"Title":"Christine: Fast and Furious","Year":"2004","imdbID":"tt0456345","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BYWU0Y2E2MDMtMWU2YS00NDc1LTlmNjMtZjE3YTc4OGFiYTg5XkEyXkFqcGdeQXVyMTExODYyNA@@._V1_SX300.jpg"},{"Title":"The Fast and the Furious: Editing for the MPAA","Year":"2002","imdbID":"tt0781022","Type":"movie","Poster":"N/A"},{"Title":"Fast and Furious","Year":"1924","imdbID":"tt0799767","Type":"movie","Poster":"N/A"},{"Title":"Fast & Furious: Races and Chases","Year":"2009","imdbID":"tt5527618","Type":"movie","Poster":"N/A"},{"Title":"The Fast and the Furious: Visual Effects Montage","Year":"2002","imdbID":"tt0781023","Type":"movie","Poster":"N/A"},{"Title":"Fast and Furious","Year":"1931","imdbID":"tt0142284","Type":"movie","Poster":"N/A"},{"Title":"Fast and Furious: Fast Cars!","Year":"2015","imdbID":"tt5933142","Type":"movie","Poster":"N/A"},{"Title":"The Making of 'The Fast and the Furious'","Year":"2002","imdbID":"tt5267184","Type":"movie","Poster":"N/A"},{"Title":"Fast and Furious","Year":"1917","imdbID":"tt0146739","Type":"movie","Poster":"N/A"},{"Title":"Fast and Furious","Year":"1915","imdbID":"tt0447062","Type":"movie","Poster":"N/A"}],"totalResults":"36","Response":"True"}


import requests
response = requests.get("http://www.omdbapi.com/?i=&apikey=1d094a12&s=fast and furious*&page=2&type=movie")



json_data ={"Search":[{"Title":"Christine: Fast and Furious","Year":"2004","imdbID":"tt0456345","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BYWU0Y2E2MDMtMWU2YS00NDc1LTlmNjMtZjE3YTc4OGFiYTg5XkEyXkFqcGdeQXVyMTExODYyNA@@._V1_SX300.jpg"},{"Title":"The Fast and the Furious: Editing for the MPAA","Year":"2002","imdbID":"tt0781022","Type":"movie","Poster":"N/A"},{"Title":"Fast and Furious","Year":"1924","imdbID":"tt0799767","Type":"movie","Poster":"N/A"},{"Title":"Fast & Furious: Races and Chases","Year":"2009","imdbID":"tt5527618","Type":"movie","Poster":"N/A"},{"Title":"The Fast and the Furious: Visual Effects Montage","Year":"2002","imdbID":"tt0781023","Type":"movie","Poster":"N/A"},{"Title":"Fast and Furious","Year":"1931","imdbID":"tt0142284","Type":"movie","Poster":"N/A"},{"Title":"Fast and Furious: Fast Cars!","Year":"2015","imdbID":"tt5933142","Type":"movie","Poster":"N/A"},{"Title":"The Making of 'The Fast and the Furious'","Year":"2002","imdbID":"tt5267184","Type":"movie","Poster":"N/A"},{"Title":"Fast and Furious","Year":"1917","imdbID":"tt0146739","Type":"movie","Poster":"N/A"},{"Title":"Fast and Furious","Year":"1915","imdbID":"tt0447062","Type":"movie","Poster":"N/A"}],"totalResults":"36","Response":"True"}

json_string = json.dumps(json_data)
print('Equivalent json string of input dictionary:',
      json_string)

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(len(people))

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])



somejsondata= [{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}]

movie_dict = json.loads(json_data.items())