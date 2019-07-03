from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_babel import _, lazy_gettext as _l

from app import db
from app.models import Note
from app.notes import bp
from app.notes.forms import AddNoteForm


@bp.route('/notes/add', methods=['GET', 'POST'])
@login_required
def add():
    if not current_user.is_authenticated:
        flash(_('You must be logged in to write notes'))
        return redirect(url_for('main.index'))
    form = AddNoteForm()
    notes = Note.query.filter_by(author=current_user)
    if form.validate_on_submit():
        note = Note(content=form.content.data, author=current_user)
        db.session.add(note)
        db.session.commit()
        flash(_('Your note is saved'))
        return redirect(url_for('notes.add'))
    return render_template('notes/notes.html', form=form, notes=notes)


# TODO: implement normal js delete method
@bp.route('/notes/<int:note_id>', methods=['GET'])
@login_required
def delete(note_id):
    note = Note.query.filter_by(id=note_id).first_or_404()
    if note:
        db.session.delete(note)
        db.session.commit()
        flash(_('Your note is deleted'))
    else:
        flash(_('No note with such id found'))
    return redirect(url_for('notes.add'))
