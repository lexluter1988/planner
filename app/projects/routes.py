from datetime import datetime

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from flask_babel import _, lazy_gettext as _l

from app import db
from app.models import Project
from app.projects import bp
from app.projects.forms import ProjectForm


@bp.route('/projects', methods=['GET', 'POST'])
@login_required
def add():
    # TODO: no need this, we already have decorator
    if not current_user.is_authenticated:
        flash(_('You must be logged in to create project'))
        return redirect(url_for('main.index'))
    form = ProjectForm()
    projects = Project.query.all()
    if form.validate_on_submit():
        project = Project(
            name=form.name.data,
            description=form.description.data,
            status=form.status.data,
            created=datetime.utcnow(),
            deadline=form.deadline.data,
            estimated=form.estimated.data,
        )
        db.session.add(project)
        db.session.commit()
        flash(_('Your project is saved'))
        return redirect(url_for('projects.add'))
    return render_template('projects/projects.html', projects=projects, form=form)


# TODO: implement normal js delete method
@bp.route('/projects/<int:project_id>', methods=['GET'])
@login_required
def delete(project_id):
    project = Project.query.filter_by(id=project_id).first_or_404()
    if project:
        db.session.delete(project)
        db.session.commit()
        flash(_('Your project is deleted'))
    else:
        flash(_('No project with such id found'))
    return redirect(url_for('projects.add'))
