import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/registrarse', methods=('GET', 'POST'))
def registrarse():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        idcard   = request.form['idcard'  ]
        idtype   = request.form['idtype'  ]
        db = get_db()
        error = None

        if not username:
            error = 'Nombre de usuario requerido.'
        elif not password:
            error = 'Contraseña requerida.'
        elif not idcard:
            error = 'Numero de identificación requerido.'
        elif not idtype:
            error = 'Tipo de identificación requerido.'
        elif db.execute(
            'SELECT id FROM user WHERE id = ?', (idcard,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (id, username, password) VALUES (?, ?, ?)',
                (idcard, username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        idcard   = request.form['idcard'  ]
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE id = ?', (idcard,)
        ).fetchone()

        if user is None:
            error = 'Numero de identificacion incorrecto.'
        elif not check_password_hash(user['password'], password):
            error = 'Contraseña incorrecta.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# LOGIN REQUERIDO
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view