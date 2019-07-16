from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField, TextAreaField, IntegerField
from flask_babel import _, lazy_gettext as _l
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired()])
    description = TextAreaField(_l('Description'))

    project = SelectField(_l('Project'), coerce=int)

    milestone = SelectField(_l('Milestone'), coerce=int)

    priority = SelectField(_l('Priority'),
                           choices=[('1', 'Urgent'),
                                    ('2', 'High'),
                                    ('3', 'Normal'),
                                    ('4', 'Low')])
    group = SelectField(_l('Group'),
                        choices=[('1', 'Urgent/Important'),
                                 ('2', 'Urgent/UnImportant'),
                                 ('3', 'Normal/Important'),
                                 ('4', 'Normal/UnImportant')])

    status = SelectField(_l('Status'),
                         choices=[
                             ('1', 'Backlog'),
                             ('2', 'New'),
                             ('3', 'In Progress'),
                             ('4', 'Done')],
                         validators=[DataRequired()])

    deadline = DateTimeField(_l('Deadline'), format='%m/%d/%y %H:%M', default=datetime.now())
    schedule = DateTimeField(_l('Schedule'), format='%m/%d/%y %H:%M', default=datetime.now())
    estimated = IntegerField(_l('Estimated'))

    actions = StringField(_l('Actions'))
    submit = SubmitField(_l('Submit'))
