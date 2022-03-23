from flask import Blueprint
from flask import Flask
from flask_socketio import SocketIO
from flask_login import LoginManager
from repository import Homespace

socketio = SocketIO()
login = LoginManager()

main = Blueprint('main', __name__)

from . import routes, events

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug = debug
    app.config['SECRET_KEY'] = 'secret!'

    app.register_blueprint(main)

    login.init_app(app)
    socketio.init_app(app, manage_session=False,  DEBUG=True)
    return app