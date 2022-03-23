import sqlite3
from enum import Enum
from flask_login import UserMixin

from .database import Database

class MessageType(str, Enum):
    CONFIRMATION = 1
    INFORMATION = 2
    WARNING = 3
    ERROR = 4
    SYSTEM = 5

class MessageAction(str, Enum):
    ENABLE = 1
    DISABLE = 2
    ALLOW = 3
    DENY = 4
    LOG = 5

class Homespace(UserMixin):
    def __init__(self, id, client_token, session_id):
        self.id = id
        self.client_token = client_token
        self.session_id = session_id

    def list_homespaces():
        homespaces = []
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM homespaces where session_id != 'NULL';''')
        for homespace in cursor.fetchall():
            client = Homespace(homespace[0], homespace[1], homespace[2])
            homespaces.append(client)
        return homespaces
    
    def list_homespace_by_token(client_token):
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM homespaces WHERE client_token=?''', [client_token])
        result = cursor.fetchone()
        homespace = Homespace(result[0], result[1], result[2])
        return homespace
    
    def update_homespace(homespace):
        conn = Database.create_connection()
        cursor = conn.cursor()
        home = (homespace.client_token, homespace.session_id, homespace.id)
        cursor.execute("UPDATE homespaces SET client_token=?, session_id = ? where id = ?", home)
        conn.commit()

class Notification:
    def __init__(self, action, type, protocol):
        self.action = action
        self.type = type
        self.protocol = protocol

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)