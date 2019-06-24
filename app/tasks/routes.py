from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_babel import _, lazy_gettext as _l

from app import db
from app.models import Task
from app.tasks import bp


@bp.route('/tasks', methods=['GET'])
@login_required
def all():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)
