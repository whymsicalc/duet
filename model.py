from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Instantiate a SQLAlchemy object to create db.Model classes
db = SQLAlchemy()

class Game(db.Model):
    """Game model for a game."""

    __tablename__ = "games"

    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player1 = db.Column(db.String(50), nullable=False)
    player2 = db.Column(db.String(50), nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    game_card = db.Column(db.String(100), nullable=False)
    words = db.Column(db.Text, nullable=False)
    game_status = db.Column(db.String(100), nullable=False)

class Board(db.Model):
    """Board model for board status of a game."""

    __tablename__ = "boards"

    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.game_id"), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    games = db.relationship("Game", backref="boards")


def connect_to_db(app, database='postgres:///codenames'):
    """Connect the database to our Flask app."""

    # Configure to use our database
    # Database URI that should be used for the connection: kitchens
    app.config["SQLALCHEMY_DATABASE_URI"] = database
    # SQLAlchemy will NOT log all the statements issued to stderr when set to False
    app.config["SQLALCHEMY_ECHO"] = False
    # SQLAlchemy will NOT track modifications of objects
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # Connect app with db
    db.app = app
    # Initialize app
    db.init_app(app)


if __name__ == "__main__":
    # If we run file interactively, we can work with database directly.

    from server import app
    connect_to_db(app)