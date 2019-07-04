from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField, TextAreaField, IntegerField
from flask_babel import _, lazy_gettext as _l
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired()])
    description = TextAreaField(_l('Description'))

    # TODO: pass projects or default from data here
    project = SelectField(_l('Project'), coerce=int)

    # TODO: pass milestones or default from data here
    milestone = SelectField(_l('Milestone'), coerce=int)

    priority = SelectField(_l('Priority'),
                           choices=[('3', 'Normal'),
                                    ('1', 'Urgent')])
    group = SelectField(_l('Group'),
                        choices=[('3', '3'),
                                 ('1', '1')])

    status = SelectField(_l('Status'),
                         choices=[
                             ('new', 'New'),
                             ('in progress', 'In Progress'),
                             ('done', 'Done')],
                         validators=[DataRequired()])

    deadline = DateTimeField(_l('Deadline'), format='%m/%d/%y %H:%M', default=datetime.now())
    schedule = DateTimeField(_l('Schedule'), format='%m/%d/%y %H:%M', default=datetime.now())
    estimated = IntegerField(_l('Estimated'))

    actions = StringField(_l('Actions'))
    submit = SubmitField(_l('Submit'))
