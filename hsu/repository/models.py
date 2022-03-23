import sqlite3
from .database import Database

class Models:

    def __init__(self, location_id, model_id, name, collector_id):
        self.location_id = location_id
        self.model_id = model_id
        self.name = name
        self.collector_id = collector_id

    def list_active_models():
        models = []

        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute('select location_id, model_id, name, collector_id from models_active as ma inner join models as m on m.id == ma.model_id;')
        
        for model_temp in cursor.fetchall():
            model = Models(model_temp[0], model_temp[1], model_temp[2], model_temp[3])
            models.append(model)

        conn.close()
        
        return models
