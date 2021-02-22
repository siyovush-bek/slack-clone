from functools import wraps
from flask import render_template, session, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from flack import app


class Channel:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []
    
    def __repr__(self):
        return self.name
    


channel = Channel('General')
channel.messages = ['aaa' for _ in range(20)]
channels = ['clubhouse', 'semiplanet']
users = set()


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get('USERNAME'):
            return redirect(url_for('login'))
        else:
            return f(*args, **kwargs)
    return wrapper


@app.route('/')
@login_required
def home():
    username = session.get("USERNAME")
    return render_template("home.html", username=username, channel=channel, channels=channels)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if session.get('USERNAME'):
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        if name in users:
            error = "Such username already exists, please pick another"
        else:
            users.add(name)
            session['USERNAME'] = name
            return redirect(url_for('home'))
    return render_template("signin.html", title='Login', error=error)


@app.route('/logout')
@login_required
def logout():
    users.remove(session['USERNAME'])
    del session['USERNAME']
    return redirect(url_for('login'))
