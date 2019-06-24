from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField, TextAreaField, IntegerField
from flask_babel import _, lazy_gettext as _l
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired()])
    description = TextAreaField(_l('Description'))

    project = SelectField(_l('Project'),
                          choices=[('home', 'Home'),
                                   ('work', 'Work')])

    milestone = SelectField(_l('Milestone'),
                            choices=[('day', 'Day'),
                                     ('week', 'Week')])

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

    #deadline = DateTimeField(_l('Deadline'), format='%m/%d/%y %H:%M', id='deadline_datepicker')
    #schedule = DateTimeField(_l('Schedule'), format='%m/%d/%y %H:%M', id='schedule_datepicker')
    estimated = IntegerField(_l('Estimated'))

    actions = StringField(_l('Actions'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))
