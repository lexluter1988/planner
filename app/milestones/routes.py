from datetime import datetime

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from flask_babel import _, lazy_gettext as _l

from app import db
from app.models import Milestone, Project
from app.milestones import bp
from app.milestones.forms import MilestoneForm
from app.projects.routes import create_default_project


@bp.route('/milestones', methods=['GET', 'POST'])
@login_required
def add():
    if not current_user.is_authenticated:
        flash(_('You must be logged in to create milestones'))
        return redirect(url_for('main.index'))
    form = MilestoneForm()
    milestones = Milestone.query.all()

    projects = Project.query.all()
    if not projects:
        projects = [create_default_project()]
    form.project.choices = [(p.id, p.name) for p in projects]

    if form.validate_on_submit():
        selected_project = Project.query.get(form.project.data)
        milestone = Milestone(
            name=form.name.data,
            description=form.description.data,
            project=selected_project,
            status=form.status.data,
            created=datetime.utcnow(),
            deadline=form.deadline.data,
            estimated=form.estimated.data,
        )
        db.session.add(milestone)
        db.session.commit()
        flash(_('Your milestone is saved'))
        return redirect(url_for('milestones.add'))
    return render_template('milestones/milestones.html', milestones=milestones, form=form)


# TODO: implement normal js delete method
@bp.route('/projects/<int:milestone_id>', methods=['GET'])
@login_required
def delete(milestone_id):
    project = Milestone.query.filter_by(id=milestone_id).first_or_404()
    if project:
        db.session.delete(project)
        db.session.commit()
        flash(_('Your milestone is deleted'))
    else:
        flash(_('No milestone with such id found'))
    return redirect(url_for('milestones.add'))


def create_default_milestone():
    milestone = Milestone(
        name=_('default'),
        description=_('Automatically generated default milestone '),
        project=None,
        status=None,
        created=datetime.utcnow(),
        deadline=None,
        estimated=None,
    )
    db.session.add(milestone)
    db.session.commit()
    return milestone
