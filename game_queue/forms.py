from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError


# Forms
class UsernameForm(Form):
    username = StringField('Username', validators=[DataRequired()])


# Validators
class Unique(object):
    def __init__(self, message: str) -> None:
        self.message = message

    def __call__(self, form, field) -> None:
        pass
