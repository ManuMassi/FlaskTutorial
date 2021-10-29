from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    rate_the_dog = SelectField('rate', choices=["Good boy", "Sad Dog"])
    submit = SubmitField('Submit')

