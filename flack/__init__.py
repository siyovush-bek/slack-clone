from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you will never guess'
socketio = SocketIO(app)

from flack import routes