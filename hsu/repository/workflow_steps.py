import sqlite3
from .database import Database

class WorkflowSteps:

    def __init__(self, id, name, sequence_number, type, workflow_id, model_id, location_id):
        self.id = id
        self.name = name
        self.sequence_number = sequence_number
        self.type = type
        self.workflow_id = workflow_id
        self.model_id = model_id
        self.location_id = location_id

    def list_steps_workflow(workflow_id):
        workflows = []

        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute('select * from workflow_steps where workflow_id=? order by sequence_number', [workflow_id])

        for workflow_temp in cursor.fetchall():
            workflow = WorkflowSteps(workflow_temp[0], workflow_temp[1], workflow_temp[2], workflow_temp[3], workflow_temp[4], workflow_temp[5], workflow_temp[6])
            workflows.append(workflow)

        conn.close()
        
        return workflows
