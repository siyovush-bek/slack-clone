from flask import render_template, session
from flask.helpers import url_for
from werkzeug.utils import redirect
from flack import app

def login_required(f, *args, **kwargs):
    def wrapper():
        if not session.get('USERNAME'):
            return redirect(url_for('login'))
        f(*args, **kwargs)
    return wrapper


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template("login.html", title='Login')