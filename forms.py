from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('dg','dog'), ('ct','cat'), ('pc', 'porcupine')])
    photo_url = StringField("Image", validators=[Optional(), URL()])
    age = FloatField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])
    # available = BooleanField("Available", validators=[InputRequired()])

class EditPetForm(FlaskForm):
    """Form for adding snacks."""

    photo_url = StringField("Image", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")