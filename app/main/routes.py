from flask import render_template
from flask_login import login_required
from app.main import bp


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    services = {'settings': True, 'notes': False}
    return render_template('index.html', context=services)
