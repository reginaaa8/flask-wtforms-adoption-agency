from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField

class AddPetForm(FlaskForm):
    name = StringField("Pet Name")

    species = SelectField("Species",
                          choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    
    photo_url = StringField("Photo Url")

    age = IntegerField("Age")

    notes = TextAreaField("Notes")