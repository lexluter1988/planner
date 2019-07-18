from datetime import datetime

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from flask_babel import _, lazy_gettext as _l

from app import db
from app.milestones.routes import create_default_milestone
from app.models import Task, Milestone, Project
from app.projects.routes import create_default_project
from app.tasks import bp
from app.tasks.forms import TaskForm


@bp.route('/all', methods=['GET'])
@login_required
def all():
    if not current_user.is_authenticated:
        flash(_('You must be logged in to create tasks'))
        return redirect(url_for('main.index'))
    tasks = Task.query.filter_by(author=current_user)
    return render_template('tasks/tasks.html', tasks=tasks)


@bp.route('/priority', methods=['GET'])
@login_required
def priority():
    tasks = Task.query.filter_by(author=current_user)
    return render_template('tasks/tasks_kovi.html', tasks=tasks)


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = TaskForm()
    milestones = Milestone.query.all()
    if not milestones:
        milestones = [create_default_milestone()]

    projects = Project.query.all()
    if not projects:
        projects = [create_default_project()]

    form.milestone.choices = [(m.id, m.name) for m in milestones]
    form.project.choices = [(p.id, p.name) for p in projects]

    if form.validate_on_submit():

        selected_milestone = Milestone.query.get(form.milestone.data)
        selected_project = Project.query.get(form.project.data)

        task = Task(
            name=form.name.data,
            author=current_user,
            description=form.name.data,
            project=selected_project,
            milestone=selected_milestone,
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
        return redirect(url_for('tasks.all'))
    return render_template('tasks/tasks.html', form=form)


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
