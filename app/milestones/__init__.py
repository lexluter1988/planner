from flask import Blueprint

bp = Blueprint('milestones', __name__)

from app.milestones import routes