from datetime import datetime

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from flask_babel import _, lazy_gettext as _l

from app import db
from app.models import Milestone
from app.milestones import bp
from app.milestones.forms import MilestoneForm


@bp.route('/milestones', methods=['GET', 'POST'])
@login_required
def add():
    if not current_user.is_authenticated:
        flash(_('You must be logged in to create milestones'))
        return redirect(url_for('main.index'))
    form = MilestoneForm()
    milestones = Milestone.query.all()
    if form.validate_on_submit():
        milestone = Milestone(
            name=form.name.data,
            description=form.description.data,
            projects=form.projects.data,
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
