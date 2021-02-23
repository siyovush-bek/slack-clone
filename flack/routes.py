from functools import wraps
from datetime import datetime
from flask import render_template, session, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_socketio import emit
from flack import app, socketio
from flack.models import Channel, Message, users



channel = Channel('General')


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
    return render_template("home.html", username=username, channel=channel)


# socket stuff
@socketio.on('user connect')
def user_connect(data):
    new_member = data['user']
    if channel.add_member(new_member):
        emit('user connect', {'message': f'{new_member} joined the channel'}, broadcast=True)

@socketio.on("send message")
def send_message(data):
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    msg = data['content']
    sender = data['sender']
    if msg and not msg.isspace():
        message = Message(msg, now, sender)
        channel.add_message(message)
        emit("recieve message", {"content": msg, 'sender': sender }, broadcast=True)

# @socketio.on('connect')
# def user_connected(data):
#     emit('user connected', {'msg' : f"{data['user']} connected"})


# login logout functions, should be moved to seperate blueprint
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
    user = session.pop('USERNAME')
    users.remove(user)
    channel.remove_member(user)
    return redirect(url_for('login'))
