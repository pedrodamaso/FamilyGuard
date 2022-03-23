import sqlite3
from sqlite3 import Error
from database import Database

class DataRepository:

    def create_table_message_type(coon):
        try:
            if conn is not None:

                c = conn.cursor() 

                c.execute('''CREATE TABLE IF NOT EXISTS message_type (
                                    id integer PRIMARY KEY,
                                    description text
                                );''')
        except Error as e:
            print(e)

    def create_table_message_action(coon):
        try:
            if conn is not None:

                c = conn.cursor() 

                c.execute('''CREATE TABLE IF NOT EXISTS message_action (
                                    id integer PRIMARY KEY,
                                    description text
                                );''')
        except Error as e:
            print(e)

    def create_table_device_type(coon):
        try:
            if conn is not None:

                c = conn.cursor() 

                c.execute('''CREATE TABLE IF NOT EXISTS device_type (
                                    id integer PRIMARY KEY,
                                    description text
                                );''')
        except Error as e:
            print(e)
    
    def create_table_devices(coon):
        try:
            if conn is not None:

                c = conn.cursor() 

                c.execute('''CREATE TABLE IF NOT EXISTS devices (
                                    id integer PRIMARY KEY,
                                    name text,
                                    device_type_id integer,
                                    FOREIGN KEY (device_type_id) REFERENCES device_type(id)
                                );''')
        except Error as e:
            print(e)

    def create_table_collectors(coon):
        try:
            if conn is not None:

                c = conn.cursor() 

                c.execute('''CREATE TABLE IF NOT EXISTS collectors (
                                    id integer PRIMARY KEY,
                                    description text
                                );''')

        except Error as e:
            print(e)

    def create_table_models(coon):
        try:
            if conn is not None:

                c = conn.cursor() 

                c.execute('''CREATE TABLE IF NOT EXISTS models (
                                    id integer PRIMARY KEY,
                                    name text,
                                    collector_id integer,
                                    FOREIGN KEY (collector_id) REFERENCES collectors(id)

                                );''')
        except Error as e:
            print(e)

    def create_table_models_active(conn):
        try:
            if conn is not None:

                c = conn.cursor() 

                c.execute('''CREATE TABLE IF NOT EXISTS models_active (
                                    location_id integer,
                                    model_id integer,
                                    FOREIGN KEY (model_id) REFERENCES models(id),
                                    PRIMARY KEY(location_id, model_id)
                                );''')
        except Error as e:
            print(e)


    def create_table_workflows(coon):
        try:
            if conn is not None:

                c = conn.cursor() 

                c.execute('''CREATE TABLE IF NOT EXISTS workflows (
                                    id integer PRIMARY KEY,
                                    name text,
                                    active text,
                                    collector_id integer,
                                    FOREIGN KEY (collector_id) REFERENCES collectors(id)
                                );''')

        except Error as e:
            print(e)

    def create_table_workflow_steps(coon):
        try:
            if conn is not None:

                c = conn.cursor() 

                c.execute('''CREATE TABLE IF NOT EXISTS workflow_steps (
                                    id integer PRIMARY KEY,
                                    name text,
                                    sequence_number integer,
                                    type integer,
                                    workflow_id integer,
                                    model_id integer,
                                    location_id integer,
                                    FOREIGN KEY (workflow_id) REFERENCES workflows(id),
                                    FOREIGN KEY (model_id) REFERENCES models(id)
                                    FOREIGN KEY (location_id) REFERENCES models_active(location_id)
                                );''')

        except Error as e:
            print(e)

    def create_table_messages(conn):
        
        try:
            if conn is not None:
                
                c = conn.cursor() 

                c.execute('''CREATE TABLE IF NOT EXISTS messages (
                                    id integer PRIMARY KEY,
                                    homespace_id integer,
                                    message_type_id integer,
                                    message_action_id integer,
                                    create_at text NOT NULL,
                                    FOREIGN KEY (message_type_id) REFERENCES message_type(id),
                                    FOREIGN KEY (message_action_id) REFERENCES message_action(id)
                                );''')

        except Error as e:
            print(e)

    def create_table_workflow_rules(conn):
        
        try:
            if conn is not None:
                
                c = conn.cursor() 

                c.execute('''CREATE TABLE IF NOT EXISTS workflow_rules (
                                    id integer PRIMARY KEY,
                                    workflow_id integer,
                                    condition text,
                                    model_id_value integer,
                                    stop_conditions,
                                    FOREIGN KEY (workflow_id) REFERENCES workflows(id),
                                    FOREIGN KEY (model_id_value) REFERENCES models(id)
                                );''')

        except Error as e:
            print(e)

    def populate_table_message_type(conn):

        try:
            if conn is not None:
                
                c = conn.cursor() 
                cur = conn.cursor()

                sql1 = ''' INSERT INTO message_type(description) VALUES('confirmation') '''
                sql2 = ''' INSERT INTO message_type(description) VALUES('information') '''
                sql3 = ''' INSERT INTO message_type(description) VALUES('warning') '''
                sql4 = ''' INSERT INTO message_type(description) VALUES('error') '''
                sql5 = ''' INSERT INTO message_type(description) VALUES('system') '''
                
                cur.execute(sql1)
                cur.execute(sql2)
                cur.execute(sql3)
                cur.execute(sql4)
                cur.execute(sql5)
               
                conn.commit()
        except Error as e:
            print(e)       

    def populate_table_message_action(conn):

        try:
            if conn is not None:
                
                c = conn.cursor() 
                cur = conn.cursor()

                sql1 = ''' INSERT INTO message_action(description) VALUES('enable') '''
                sql2 = ''' INSERT INTO message_action(description) VALUES('disable') '''
                sql3 = ''' INSERT INTO message_action(description) VALUES('allow') '''
                sql4 = ''' INSERT INTO message_action(description) VALUES('deny') '''
                sql5 = ''' INSERT INTO message_action(description) VALUES('log') '''
                
                cur.execute(sql1)
                cur.execute(sql2)
                cur.execute(sql3)
                cur.execute(sql4)
                cur.execute(sql5)
               
                conn.commit()
        except Error as e:
            print(e)  

    def populate_table_device_type(conn):

        try:
            if conn is not None:
                
                c = conn.cursor() 
                cur = conn.cursor()

                sql1 = ''' INSERT INTO device_type(description) VALUES('traditional') '''
                sql2 = ''' INSERT INTO device_type(description) VALUES('mobile') '''
                sql3 = ''' INSERT INTO device_type(description) VALUES('iot') '''
                
                cur.execute(sql1)
                cur.execute(sql2)
                cur.execute(sql3)
               
                conn.commit()
        except Error as e:
            print(e)  

    def populate_table_devices(conn):

        try:
            if conn is not None:
                
                c = conn.cursor() 
                cur = conn.cursor()

                sql1 = ''' INSERT INTO devices(name, device_type_id) VALUES('PD-Desktop', 1) '''
                
                cur.execute(sql1)
               
                conn.commit()
        except Error as e:
            print(e)  


    def populate_table_collectors(conn):

        try:
            if conn is not None:
                
                c = conn.cursor() 
                cur = conn.cursor()

                sql1 = ''' INSERT INTO collectors(description) VALUES('CICFlowMeter') '''
                
                cur.execute(sql1)
               
                conn.commit()
        except Error as e:
            print(e)  

    def populate_table_models(conn):

        try:
            if conn is not None:
                
                c = conn.cursor() 
                cur = conn.cursor()

                sql1 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_1_TC_1_StandardScaler.fg', 1) '''
                sql2 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_1_TC_1_PCA.fg', 1) '''
                sql3 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_1_TC_1_LOF.fg', 1) '''

                sql4 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_1_TC_2_PCA.fg', 1) '''
                sql5 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_1_TC_2_StandardScaler.fg', 1) '''
                sql6 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_1_TC_2_LOF.fg', 1) '''

                sql7 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_1_TC_3_StandardScaler.fg', 1) '''
                sql8 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_1_TC_3_PCA.fg', 1) '''
                sql9 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_1_TC_3_LOF.fg', 1) '''

                sql10 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_2_TC_1_StandardScaler.fg', 1) '''
                sql11 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_2_TC_1_PCA.fg', 1) '''
                sql12 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_2_TC_1_kNN.fg', 1) '''

                sql13 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_2_TC_2_StandardScaler.fg', 1) '''
                sql14 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_2_TC_2_PCA.fg', 1) '''
                sql15 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_2_TC_2_kNN.fg', 1) '''

                sql16 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_2_TC_3_StandardScaler.fg', 1) '''
                sql17 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_2_TC_3_PCA.fg', 1) '''
                sql18 = ''' INSERT INTO models(name, collector_id) VALUES('WORK_2_TC_3_kNN.fg', 1) '''


                cur.execute(sql1)
                cur.execute(sql2)
                cur.execute(sql3)
                cur.execute(sql4)
                cur.execute(sql5)
                cur.execute(sql6)
                cur.execute(sql7)
                cur.execute(sql8)
                cur.execute(sql9)
                cur.execute(sql10)
                cur.execute(sql11)
                cur.execute(sql12)
                cur.execute(sql13)
                cur.execute(sql14)
                cur.execute(sql15)
                cur.execute(sql16)
                cur.execute(sql17)
                cur.execute(sql18)
               
                conn.commit()
        except Error as e:
            print(e) 

    def populate_table_models_active(conn):

        try:
            if conn is not None:
                
                c = conn.cursor() 
                cur = conn.cursor()

                sql1 = ''' INSERT INTO models_active(location_id, model_id) VALUES(1, 1) '''
                sql2 = ''' INSERT INTO models_active(location_id, model_id) VALUES(2, 2) '''
                sql3 = ''' INSERT INTO models_active(location_id, model_id) VALUES(3, 3) '''
                sql4 = ''' INSERT INTO models_active(location_id, model_id) VALUES(4, 15) '''
                
                #sql1 = ''' INSERT INTO models_active(location_id, model_id) VALUES(1, 4) '''
                #sql2 = ''' INSERT INTO models_active(location_id, model_id) VALUES(2, 5) '''
                #sql3 = ''' INSERT INTO models_active(location_id, model_id) VALUES(3, 6) '''
                #sql4 = ''' INSERT INTO models_active(location_id, model_id) VALUES(4, 13) '''
                #sql5 = ''' INSERT INTO models_active(location_id, model_id) VALUES(5, 14) '''
                #sql6 = ''' INSERT INTO models_active(location_id, model_id) VALUES(6, 15) '''

                #sql1 = ''' INSERT INTO models_active(location_id, model_id) VALUES(1, 7) '''
                #sql2 = ''' INSERT INTO models_active(location_id, model_id) VALUES(2, 8) '''
                #sql3 = ''' INSERT INTO models_active(location_id, model_id) VALUES(3, 9) '''
                #sql4 = ''' INSERT INTO models_active(location_id, model_id) VALUES(4, 16) '''
                #sql5 = ''' INSERT INTO models_active(location_id, model_id) VALUES(5, 17) '''
                #sql6 = ''' INSERT INTO models_active(location_id, model_id) VALUES(6, 18) '''

                cur.execute(sql1)
                cur.execute(sql2)
                cur.execute(sql3)
                cur.execute(sql4)
               
                conn.commit()
        except Error as e:
            print(e)  

    def populate_table_workflows(conn):

        try:
            if conn is not None:
                
                c = conn.cursor() 
                cur = conn.cursor()

                sql1 = ''' INSERT INTO workflows(name, active, collector_id) VALUES('WORKFLOW_1', 1, 1) '''
                sql2 = ''' INSERT INTO workflows(name, active, collector_id) VALUES('WORKFLOW_2', 1, 1) '''
                
                cur.execute(sql1)
                cur.execute(sql2)
               
                conn.commit()
        except Error as e:
            print(e)  

    def populate_table_workflow_steps(conn):

        try:
            if conn is not None:
                
                c = conn.cursor() 
                cur = conn.cursor()

                sql1 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                           VALUES('WORKFLOW_1_STEP_1', 1, 1, 1, 1, 1) '''

                sql2 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                           VALUES('WORKFLOW_1_STEP_2', 2, 1, 1, 2, 2) '''

                sql3 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                           VALUES('WORKFLOW_1_STEP_3', 3, 2, 1, 3, 3) '''

                sql4 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                           VALUES('WORKFLOW_2_STEP_1', 1, 1, 2, 1, 1) '''

                sql5 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                           VALUES('WORKFLOW_2_STEP_2', 2, 1, 2, 2, 2) '''

                sql6 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                           VALUES('WORKFLOW_2_STEP_3', 3, 2, 2, 3, 3) '''
                
                sql7 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                           VALUES('WORKFLOW_2_STEP_4', 4, 2, 2, 4, 15) '''


                #sql1 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                #           VALUES('WORKFLOW_1_STEP_1', 1, 1, 1, 1, 4) '''

                #sql2 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                #           VALUES('WORKFLOW_1_STEP_2', 2, 1, 1, 2, 5) '''

                #sql3 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                #           VALUES('WORKFLOW_1_STEP_3', 3, 2, 1, 3, 6) '''

                #sql4 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                #           VALUES('WORKFLOW_2_STEP_1', 1, 1, 2, 4, 13) '''
                
                #sql5 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                #           VALUES('WORKFLOW_2_STEP_2', 2, 1, 2, 5, 14) '''

                #sql6 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                #           VALUES('WORKFLOW_2_STEP_3', 3, 2, 2, 6, 15) '''


                #sql1 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                #           VALUES('WORKFLOW_1_STEP_1', 1, 1, 1, 1, 7) '''

                #sql2 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                #           VALUES('WORKFLOW_1_STEP_2', 2, 1, 1, 2, 8) '''

                #sql3 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                #           VALUES('WORKFLOW_1_STEP_3', 3, 2, 1, 3, 9) '''

                #sql4 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                #           VALUES('WORKFLOW_2_STEP_1', 1, 1, 2, 4, 16) '''
                
                #sql5 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                #           VALUES('WORKFLOW_2_STEP_2', 2, 1, 2, 5, 17) '''

                #sql6 = ''' INSERT INTO workflow_steps(name, sequence_number, type, workflow_id, location_id, model_id)
                #           VALUES('WORKFLOW_2_STEP_3', 3, 2, 2, 6, 18) '''
                
                cur.execute(sql1)
                cur.execute(sql2)
                cur.execute(sql3)
                cur.execute(sql4)
                cur.execute(sql5)
                cur.execute(sql6)
                cur.execute(sql7)

                conn.commit()
        except Error as e:
            print(e)

  
    def populate_table_workflow_rules(conn):

        try:
            if conn is not None:
                
                c = conn.cursor() 
                cur = conn.cursor()
                
                sql1 = ''' INSERT INTO workflow_rules(workflow_id, condition, model_id_value, stop_conditions) VALUES(1, '1', 'predicted_temp[3]', 1) '''
                sql2 = ''' INSERT INTO workflow_rules(workflow_id, condition, model_id_value, stop_conditions) VALUES(2, 'predicted_temp[3] == 0', 'predicted_temp[3]', 1) '''
                sql3 = ''' INSERT INTO workflow_rules(workflow_id, condition, model_id_value, stop_conditions) VALUES(2, '1', 'predicted_temp[15]', 0) '''
                #sql1 = ''' INSERT INTO workflow_rules(workflow_id, condition, model_id_value, stop_conditions) VALUES(1, 'predicted_temp[6] == 0', 'predicted_temp[6]', 1) '''

                #sql1 = ''' INSERT INTO workflow_rules(workflow_id, condition, model_id_value, stop_conditions) VALUES(1, 'predicted_temp[9] == 0', 'predicted_temp[9]', 1) '''


                #sql2 = ''' INSERT INTO workflow_rules(workflow_id, condition, model_id_value, stop_conditions) VALUES(2, 'predicted_temp[3] == predicted_temp[4]', 'predicted_temp[3]', 1) '''
                #sql3 = ''' INSERT INTO workflow_rules(workflow_id, condition, model_id_value, stop_conditions) VALUES(2, '(predicted_temp[3] == 0) and (predicted_temp[4] == 1)', 'predicted_temp[3]', 0) '''
                #sql4 = ''' INSERT INTO workflow_rules(workflow_id, condition, model_id_value, stop_conditions) VALUES(2, '(predicted_temp[3] == 1) and (predicted_temp[4] == 0)', 'predicted_temp[4]', 0) '''
                
                cur.execute(sql1)
                cur.execute(sql2)
                cur.execute(sql3)
                #cur.execute(sql3)
                #cur.execute(sql4)
               
                conn.commit()
        except Error as e:
            print(e)  



if __name__ == '__main__':
    conn =  Database.create_connection()

    DataRepository.create_table_device_type(conn)
    DataRepository.create_table_devices(conn)
    DataRepository.create_table_message_type(conn)
    DataRepository.create_table_message_action(conn)
    DataRepository.create_table_collectors(conn)
    DataRepository.create_table_models(conn)
    DataRepository.create_table_models_active(conn)
    DataRepository.create_table_workflows(conn)
    DataRepository.create_table_workflow_steps(conn)
    DataRepository.create_table_messages(conn)
    DataRepository.create_table_workflow_rules(conn)


    DataRepository.populate_table_device_type(conn)
    DataRepository.populate_table_message_type(conn)
    DataRepository.populate_table_message_action(conn)
    DataRepository.populate_table_devices(conn)
    DataRepository.populate_table_collectors(conn)
    DataRepository.populate_table_models(conn)
    DataRepository.populate_table_models_active(conn)
    DataRepository.populate_table_workflows(conn)
    DataRepository.populate_table_workflow_steps(conn)
    DataRepository.populate_table_workflow_rules(conn)

    conn.close()