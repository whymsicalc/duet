from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

BOARDS = []

WORDS = []

@app.route("/")
def homepage():
    """Show homepage."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)