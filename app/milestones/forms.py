from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField, TextAreaField, IntegerField
from flask_babel import _, lazy_gettext as _l
from wtforms.validators import DataRequired


class MilestoneForm(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired()])
    description = TextAreaField(_l('Description'))

    project = SelectField(_l('Project'), coerce=int)

    status = SelectField(_l('Status'),
                         choices=[
                             ('new', 'New'),
                             ('in progress', 'In Progress'),
                             ('done', 'Done')],
                         validators=[DataRequired()])

    deadline = DateTimeField(_l('Deadline'), format='%m/%d/%y %H:%M', default=datetime.now())
    estimated = IntegerField(_l('Estimated'))
    submit = SubmitField(_l('Submit'))
