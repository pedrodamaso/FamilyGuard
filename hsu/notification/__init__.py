from flask import Flask
import socketio
from .notification import Notification

#socketio = socketio.AsyncClient(logger=True, engineio_logger=True, ssl_verify=False)
socketio = socketio.AsyncClient(logger=True, engineio_logger=True)

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'top secret!'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app, manage_session=False,  DEBUG = True)
    return app