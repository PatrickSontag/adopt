from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Image", validators=[Optional()])
    age = FloatField("Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available", validators=[InputRequired()])