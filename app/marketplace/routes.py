from flask import render_template
from flask_login import login_required
from app.marketplace import bp
from app.marketplace.store import catalog


@bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    return render_template('marketplace/settings.html', catalog=catalog)
