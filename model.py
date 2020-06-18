from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Instantiate a SQLAlchemy object to create db.Model classes
db = SQLAlchemy()

class Game(db.Model):
    """Game model for a game."""

    __tablename__ = "game"

    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player1 = db.Column(db.String(50), nullable=False)
    player2 = db.Column(db.String(50), nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    game_card = db.Column(db.String(100), nullable=False)
    words = db.Column(db.Text, nullable=False)
    game_status = db.Column(db.String(100), nullable=False)