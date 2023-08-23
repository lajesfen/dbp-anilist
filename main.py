from flask import Flask
from flask import request

app = Flask(__name__)

anilist = [
    { "id": 0, "title": "Anime 0", "score": 1.0, "type": "Serie", "season": "1", "genres": [ "Accion", "Aventura", "Pelea" ] },
    { "id": 1, "title": "Anime 1", "score": 1.0, "type": "Serie", "season": "3", "genres": [ "Accion", "Aventura", "Pelea" ] },
    { "id": 2, "title": "Anime 2", "score": 1.0, "type": "Serie", "season": "Final", "genres": [ "Accion", "Aventura", "Pelea" ] },
    { "id": 3, "title": "Anime 3", "score": 1.0, "type": "Serie", "season": "5", "genres": [ "Accion", "Aventura", "Pelea" ] },
    { "id": 4, "title": "Anime 4", "score": 1.0, "type": "Serie", "season": "GT", "genres": [ "Accion", "Aventura", "Pelea" ] },
    { "id": 5, "title": "Anime 5", "score": 1.0, "type": "Serie", "season": "0", "genres": [ "Accion", "Aventura", "Pelea" ] },
    { "id": 6, "title": "Anime 6", "score": 1.0, "type": "Serie", "season": "Plus", "genres": [ "Accion", "Aventura", "Pelea" ] },
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

    for _ani in anilist:
        if anime['id'] == _ani['id']:
            anilist.remove(_ani)
    return anilist