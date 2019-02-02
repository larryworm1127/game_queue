from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError

from game_queue.app import game


# Validators
class Unique(object):
    def __init__(self, message: str) -> None:
        self.message = message

    def __call__(self, form, field) -> None:
        for queue in game.queues:
            if field.data in queue.players:
                raise ValidationError(self.message)


# Forms
class UsernameForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Unique("Can't queue up twice.")]
    )
