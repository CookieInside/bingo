from flask import Flask, render_template, jsonify, request, redirect, url_for
import json

class Game:
    player_list = []
    id = ""
    word_list = []
    suggestion_list = []

    def __init__(self, pId):
        self.id = pId

    def start(self):
        return ""
    
    def add_word(self, idx):
        if self.suggestion_list[idx] not in self.word_list:
            self.word_list.append(self.suggestion_list[idx])
        self.suggestion_list.remove(self.suggestion_list[idx])
    
    def suggest_word(self, word):
        if word not in self.suggestion_list:
            self.suggestion_list.append(word)
            
    def get_words(self):
        return self.word_list

    def get_suggestions(self):
        return self.suggestion_list

    def get_players(self):
        return self.player_list

    def join(self, name):
        self.player_list.append(name)

    def get_id(self):
        return self.id

app = Flask(__name__)
game_list = []

def get_game(id):
        for game in game_list:
          if game.get_id() == id:
            return game

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/create")
def create_game():
    return render_template("admin.html")

@app.route("/init-game", methods=["POST"])
def init_game():
    id = request.form["value"]
    game_list.append(Game(id))
    return jsonify({"result" : "game was initialized"})

@app.route("/suggest-word/<id>", methods=["POST"])
def suggest(id):
    get_game(id).suggest_word(request.form["value"])
    return jsonify({"result" : "added word to suggestion list"})

@app.route("/join/<id>/<name>")
def join(id, name):
    for game in game_list:
        if game.get_id() == id:
            game.join(name)
            return render_template('lobby.html', data=[name, id])
    return jsonify({"result" : "game not found"})

@app.route("/get-words/<id>")
def get_words(id):
    print(get_game(id).get_words())
    return jsonify(get_game(id).get_words())

@app.route("/get-suggestions/<id>")
def get_suggestions(id):
    print(get_game(id).get_suggestions())
    return jsonify(get_game(id).get_suggestions())

@app.route("/get-players/<id>")
def get_players(id):
    print(get_game(id).get_players())
    return json.dumps(get_game(id).get_players())

@app.route("/use-suggestion/<id>/<index>")
def use_suggestion(id, index):
    get_game(id).add_word(int(index))
    return jsonify({"result" : "word added"})

if __name__ == "__main__":
    app.run(host="0.0.0.0")
