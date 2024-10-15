"""Models for pets"""

default_img = "https://media.istockphoto.com/id/924005884/vector/animal-paw-vector-icon.jpg?s=612x612&w=0&k=20&c=oIN8cVbRTaFZDDfNTFZQPoB7NOILE0n3LiKALGPt9mI="

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """pet"""
    __tablename__ = "pets"

    id = db.Column(db.Integer, 
                   primary_key= True, 
                   autoincrement=True)
    
    name = db.Column(db.String, 
                     nullable=False)
    
    species = db.Column(db.String, 
                     nullable=False)
    
    photo_url = db.Column(db.String,
                          default=default_img)

    age = db.Column(db.Integer)

    notes = db.Column(db.String)

    available = db.Column(db.Boolean, default=True, nullable=False)
