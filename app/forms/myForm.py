from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    rate_the_dog = SelectField('rate', choices=["Good boy", "Sad Dog"], validators=[DataRequired()])
    dog_name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Submit')

