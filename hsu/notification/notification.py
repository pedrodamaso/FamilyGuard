import socketio
import threading
from flask import Flask, request, abort

class Notification():

    app = Flask(__name__)
    app.config["DEBUG"] = False

    sio = socketio.Client(logger=True, engineio_logger=True)
 
    @sio.event
    def connect():
        print('connection established')

    @sio.event
    def disconnect():
        print('disconnected from server')

    def __init__(self, number):
        self.number = number
        threading.Thread.__init__(self)
    
    def run(self):
        token = {'client_token': '71A30QTXHkJTltd0ahEzJp3VFEmX-ifYIqBnL6TCgdE'}
        Notification.sio.connect('http://127.0.0.1:8001/', token)