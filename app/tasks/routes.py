from datetime import datetime

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from flask_babel import _, lazy_gettext as _l

from app import db
from app.models import Task
from app.tasks import bp
from app.tasks.forms import TaskForm


@bp.route('/tasks', methods=['GET', 'POST'])
@login_required
def add():
    if not current_user.is_authenticated:
        flash(_('You must be logged in to create tasks'))
        return redirect(url_for('main.index'))
    form = TaskForm()
    tasks = Task.query.filter_by(author=current_user)
    if form.validate_on_submit():
        task = Task(
            name=form.name.data,
            author=current_user,
            description=form.name.data,
            # TODO: select projects from data here
            # project=form.project.data,
            # milestone=form.milestone.data,
            priority=form.priority.data,
            group=form.group.data,
            status=form.status.data,
            created=datetime.utcnow(),
            deadline=form.deadline.data,
            schedule=form.schedule.data,
            estimated=form.estimated.data,
            actions=form.actions.data
        )
        db.session.add(task)
        db.session.commit()
        flash(_('Your task is saved'))
        return redirect(url_for('tasks.add'))
    return render_template('tasks/tasks.html', tasks=tasks, form=form)


# TODO: implement normal js delete method
@bp.route('/tasks/<int:task_id>', methods=['GET'])
@login_required
def delete(task_id):
    project = Task.query.filter_by(id=task_id).first_or_404()
    if project:
        db.session.delete(project)
        db.session.commit()
        flash(_('Your task is deleted'))
    else:
        flash(_('No task with such id found'))
    return redirect(url_for('tasks.add'))
