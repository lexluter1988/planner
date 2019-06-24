from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_babel import _, lazy_gettext as _l

from app import db
from app.models import Note
from app.notes import bp
from app.notes.forms import AddNoteForm


@bp.route('/notes', methods=['GET'])
@login_required
def all():
    notes = Note.query.all()
    return render_template('notes/notes.html', notes=notes)


@bp.route('/notes/add', methods=['GET', 'POST'])
@login_required
def add():
    if not current_user.is_authenticated:
        flash(_('You must be logged in to write notes'))
        return redirect(url_for('main.index'))
    form = AddNoteForm()
    notes = Note.query.all()
    if form.validate_on_submit():
        note = Note(content=form.content.data, author=current_user)
        db.session.add(note)
        db.session.commit()
        flash(_('Your note is saved'))
        return redirect(url_for('notes.add'))
    return render_template('notes/notes.html', form=form, notes=notes)

