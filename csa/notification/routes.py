import json
from flask import session, redirect, url_for, render_template, request
from . import main
from repository import Homespace
from flask import jsonify, make_response, render_template
from flask_login import LoginManager, login_user, current_user, UserMixin
import jsonpickle

from . import login

@login.user_loader
def load_user(user_id):
    return UserMixin.get(user_id)

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/homespaces', methods=['GET'])
def homespaces():
    list_homespace = Homespace.list_homespaces()
    return render_template('homespaces.html', homespaces=list_homespace)

@main.route('/test', methods=['GET'])
def test():
    pass
    #homespaces = Homespace.list_homespaces()
    #return make_response(jsonpickle.encode(homespaces, unpicklable=False), 200)