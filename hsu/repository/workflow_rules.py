import sqlite3
from .database import Database

class WorkflowRules:

    def __init__(self, id, workflow_id, condition, model_id_value, stop_conditions):
        self.id = id
        self.workflow_id = workflow_id
        self.condition = condition
        self.model_id_value = model_id_value
        self.stop_conditions = stop_conditions

    def list_workflow_rules(workflow_id):
        rules = []

        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute('select * from workflow_rules where workflow_id=?', [workflow_id])

        for workflow_temp in cursor.fetchall():
            workflow_rules = WorkflowRules(workflow_temp[0], workflow_temp[1], workflow_temp[2], workflow_temp[3], workflow_temp[4])
            rules.append(workflow_rules)

        conn.close()
        
        return rules