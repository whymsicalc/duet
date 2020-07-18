from flask import Flask, request, render_template, jsonify
from static.words import words
import random

app = Flask(__name__)

@app.route("/")
def homepage():
    """Show homepage."""
    return render_template("index.html")

@app.route("/create-game", methods=["POST"])
def create_game():
    """Create game for given user."""
    player1 = request.form.get("player1")
    game_words = random.sample(words, 25)
    return render_template("game_page.html", player1=player1, game_words=game_words)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)