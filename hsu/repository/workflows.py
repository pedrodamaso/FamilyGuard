import sqlite3
from .database import Database

class Workflows:

    def __init__(self, id, name, active, collector_id):
        self.id = id
        self.name = name
        self.active = active
        self.collector_id = collector_id

    def list_active_workflows(collector_id):
        workflows = []

        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute('select * from workflows where collector_id=? and active=1', [collector_id])

        for workflow_temp in cursor.fetchall():
            workflow = Workflows(workflow_temp[0], workflow_temp[1], workflow_temp[2], workflow_temp[3])
            workflows.append(workflow)

        conn.close()
        
        return workflows