"""Pet adoption agency"""
from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///pets"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretkey"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
connect_db(app)

@app.route("/")
def home_page():
    """home page"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def show_add_pet_form():
    """show form to add a pet"""

    form = AddPetForm()

    if form.validate_on_submit():

        data = {k: v for k, v in form.data.items() if k != "csrf_token"}

        if not data.get('photo_url'):
            data.pop('photo_url', None) #removes this so that the default photo is used if user does not upload one
        
        new_pet = Pet(**data)

        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")
    
    else:
        return render_template("add_pet_form.html", form=form)
    
@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    """show details about a pet, and a form to edit the pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        
        db.session.commit()
        return redirect(f'/{pet_id}')
    
    else:
        return render_template("pet_details.html", pet=pet, form=form)
