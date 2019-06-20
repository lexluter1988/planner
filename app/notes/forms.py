from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_babel import _, lazy_gettext as _l
from wtforms.validators import DataRequired


class AddNoteForm(FlaskForm):
    content = StringField(_l('Text'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))
