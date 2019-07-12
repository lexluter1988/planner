from flask import Blueprint

bp = Blueprint('marketplace', __name__)

from app.marketplace import routes