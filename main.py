from flask import Flask
from flask import request

app = Flask(__name__)

anilist = [
    { "id": 0, "title": "Gintama", "score": 9.1, "type": "Movie", "season": "THE FINAL", "genres": [ "action", "comedy", "drama", "sci-fi" ] },
    { "id": 1, "title": "Gintama", "score": 9.0, "type": "TV Show", "season": "1", "genres": [ "action", "comedy", "drama", "sci-fi" ] },
    { "id": 2, "title": "Fruits Basket", "score": 9.0, "type": "TV Show", "season": "The Final", "genres": [ "comedy", "drama", "psychological", "romance", "slice of life" ] },
    { "id": 3, "title": "Hagane no Renkinjutsushi", "score": 9.0, "type": "TV Show", "season": "1", "genres": [ "action", "adventure", "drama", "fantasy" ] },
    { "id": 4, "title": "Kaguya-sama wa Kokurasetai", "score": 9.0, "type": "TV Show", "season": "Ultra Romantic", "genres": [ "comedy", "psychological", "romance", "slice of life" ] },
    { "id": 5, "title": "Shingeki no Kyojin", "score": 9.0, "type": "TV Show", "season": "3 Part 2", "genres": [ "action", "drama", "fantasy", "mystery" ] },
    { "id": 6, "title": "3-gatsu no Lion", "score": 8.9, "type": "TV Show", "season": "2", "genres": [ "drama", "slice of life" ] },
    { "id": 7, "title": "HUNTERxHUNTER", "score": 8.9, "type": "TV Show", "season": "2011", "genres": [ "action", "adventure", "fantasy" ] },
    { "id": 8, "title": "Owarimonogatari", "score": 8.9, "type": "TV Show", "season": "3", "genres": [ "comedy", "mystery", "psychological", "romance", "supernatural" ] },
    { "id": 9, "title": "Steins;Gate", "score": 8.9, "type": "TV Show", "season": "1", "genres": [ "drama", "psychological", "sci-fi", "thriller" ] }
]

@app.route("/anime", methods = [ "GET" ])
def get_animes():
    return anilist

@app.route("/anime", methods = [ "POST" ])
def add_anime():
    new_anime = {
        "id": request.json.get('id'),
        "title": request.json.get('title'),
        "score": request.json.get('score'),
        "type": request.json.get('type'),
        "season": request.json.get('season'),
        "genres": request.json.get('genres'),
    }
    anilist.append(new_anime)
    return new_anime

@app.route("/anime/<int:id>", methods=[ "GET" ])
def get_anime(id):
    anime = {}
    for _anime in anilist:
        if _anime['id'] == id:
            anime = _anime
    
    return anime

@app.route("/anime/<int:id>", methods=[ "PUT", "PATCH" ])
def set_anime(id):
    anime = {}
    for _anime in anilist:
        if _anime['id'] == id:
            anime = _anime
    
    if anime:
        params = request.get_json()
        for key, value in params.items():
            _anime[key] = value
    return _anime

@app.route("/anime/<int:id>", methods=[ "DELETE" ])
def delete_anime(id):
    anime = {}
    for _anime in anilist:
        if _anime['id'] == id:
            anime = _anime
    
    if anime:
        for _ani in anilist:
            if anime['id'] == _ani['id']:
                anilist.remove(_ani)
    return anilist