from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

BOARDS = []

WORDS = []

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)