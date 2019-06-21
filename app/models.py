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
    notes = db.relationship('Note', backref='author', lazy='dynamic')

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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    description = db.Column(db.Text)

    # TODO: this is reference to Milestones, and to Project but could be none.
    project = db.Column(db.Integer, nullable=True)
    milestone = db.Column(db.Integer, nullable=True)
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


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



