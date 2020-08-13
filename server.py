from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from constants.words import WORDS
from constants.boards import BOARDS
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
    game_words = random.sample(WORDS, 25)
    # save into database
    game_board = random.choice(BOARDS)
    # save board index instead of the entire board and index into board
    # save into database
    # game link - game PK
    return render_template("game_page.html", player1=player1, game_words=game_words, game_board=game_board)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)