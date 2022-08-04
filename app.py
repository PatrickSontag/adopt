from flask import Flask, request, redirect, render_template, flash, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)


########### ROUTES ##########


@app.route('/')
def home_page():
    """Shows pets list"""

    pets = Pet.query.all()
    
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Shows new pet form"""

    form = AddPetForm()

    if form.validate_on_submit():
        # data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        # new_pet = Pet(**data)
        name = form.name.data
        species = form.species.data
        photo = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet= Pet(name=name, species=species, photo_url=photo, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name} the {species}!")
        return redirect("/")

    else:
        return render_template('add_pet.html', form=form)

@app.route('/pet/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet_form(pet_id):
    """Shows pets list"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    print("PHOTO_URL: ", pet.photo_url)

    if form.validate_on_submit():
        print("PHOTO_URL post: ", pet.photo_url)

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name}: profile updated")
        return redirect("/")
    else:
        return render_template('edit_pet.html', form=form)