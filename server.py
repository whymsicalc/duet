from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

BOARDS = []

WORDS = []

@app.route("/")
def homepage():
    """Show homepage."""
    return render_template("index.html")

@app.route("/create-game", methods=["POST"])
def create_game():
    """Create game for given user."""
    player1 = request.form.get("player1")
    return render_template("game_page.html", player1=player1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)