from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

#Instantiate a SQLAlchemy object to create db.Model classes
db = SQLAlchemy()