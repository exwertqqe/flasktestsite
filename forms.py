from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class site1(FlaskForm):
    site = StringField('site', validators=[DataRequired()])
    submit = SubmitField('Submit')

