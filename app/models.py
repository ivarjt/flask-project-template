from app import db
from datetime import datetime

# This is just a sample model, you can delete it and create your own
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    date_joined = db.Column(db.Date, default=datetime.utcnow)
    # Add the rest of the columns here
    
    # Constructor method to initialize the object's attributes
    def __init__(self, username, email):
        self.username = username
        self.email = email
        # Add the rest of the columns here
        
    # Dunder method that returns a string representation of the object
    def __repr__(self):
        return f"<User: id={self.id}, username={self.username}, email={self.email}, date_joined={self.date_joined}>"