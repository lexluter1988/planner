import jwt
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from time import time
from app import db
from app import login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # relationships
    notes = db.relationship('Note', backref='author', lazy='dynamic')
    tasks = db.relationship('Task', backref='author', lazy='dynamic')
    projects = db.relationship('Project', backref='author', lazy='dynamic')
    pipelines = db.relationship('Pipeline', backref='author', lazy='dynamic')
    pipeline_tasks = db.relationship('PipelineTask', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

    # dependencies
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    description = db.Column(db.Text)

    # dependencies
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    milestone_id = db.Column(db.Integer, db.ForeignKey('milestone.id'))

    # TODO: implement choices
    priority = db.Column(db.String(64))
    # TODO: this is reference to Kovi type of view
    group = db.Column(db.String(64))

    # TODO: implement choices, also used for factory view and kanban view
    status = db.Column(db.String(64))
    created = db.Column(db.DateTime)
    ended = db.Column(db.DateTime)
    deadline = db.Column(db.DateTime)

    schedule = db.Column(db.DateTime)
    estimated = db.Column(db.Integer)
    duration = db.Column(db.Integer)

    actions = db.Column(db.String(120))


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    # relationships
    milestones = db.relationship('Milestone', backref='project', lazy='dynamic')
    tasks = db.relationship('Task', backref='project', lazy='dynamic')

    # dependencies
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    description = db.Column(db.Text)
    status = db.Column(db.String(64))
    created = db.Column(db.DateTime)
    ended = db.Column(db.DateTime)
    deadline = db.Column(db.DateTime)
    estimated = db.Column(db.Integer)
    duration = db.Column(db.Integer)


class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    # dependencies
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    # relationships
    tasks = db.relationship('Task', backref='milestone', lazy='dynamic')

    description = db.Column(db.Text)
    status = db.Column(db.String(64))
    created = db.Column(db.DateTime)
    ended = db.Column(db.DateTime)
    deadline = db.Column(db.DateTime)
    estimated = db.Column(db.Integer)
    duration = db.Column(db.Integer)


class Pipeline(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # relationships
    tasks = db.relationship('PipelineTask', backref='pipeline', lazy='dynamic')

    # dependencies
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    name = db.Column(db.Text)
    description = db.Column(db.Text)
    status = db.Column(db.String(64))
    created = db.Column(db.DateTime)
    ended = db.Column(db.DateTime)
    duration = db.Column(db.Integer)


class PipelineTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)

    # dependencies
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pipeline_id = db.Column(db.Integer, db.ForeignKey('pipeline.id'))

    position = db.Column(db.Integer)
    status = db.Column(db.String(64))
    created = db.Column(db.DateTime)
    ended = db.Column(db.DateTime)


class ApplicationStore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    # TODO: implement installed/uninstalled statuses
    status = db.Column(db.String(64))
    settings = db.relationship('Setting', backref='application', lazy='dynamic')


class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # dependencies
    app_id = db.Column(db.Integer, db.ForeignKey('application_store.id'))

    parameter = db.Column(db.Text)
    description = db.Column(db.Text)
    value = db.Column(db.Text)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



