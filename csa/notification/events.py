from flask import request, session, abort
from flask_socketio import emit
from repository import Homespace
from flask_login import LoginManager, login_user, current_user, UserMixin

from . import socketio

@socketio.on('connect', namespace='/')
def connect():
    client_token = request.headers['client_token']
    homespace = Homespace.list_homespace_by_token(client_token)

    print(homespace)
    if(homespace != None):
        homespace = Homespace(homespace.id, homespace.client_token, request.sid)
        login_user(homespace, remember=True)
        Homespace.update_homespace(homespace)
    else: 
        abort(401)

    emit('status', {'msg': ' connected'})

@socketio.on("disconnect", namespace="/")
def disconnect():
    print("desconectou")
 

@socketio.on("hsu_notification", namespace="/")
def notification(data):
    print(data)

def send_notification_hsu(data):
    socketio.emit("hsu_notification", data, namespace="/")