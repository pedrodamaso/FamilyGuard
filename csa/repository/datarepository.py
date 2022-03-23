import sqlite3
from sqlite3 import Error
from database import Database

class DataRepository:

    def create_table_homespaces(conn):

        try:
            if conn is not None:
                
                c = conn.cursor() 

                c.execute('''CREATE TABLE homespaces
                            ([id] INTEGER PRIMARY KEY,[client_token] text, [session_id] text)''')

        except Error as e:
            print(e)

    def create_homespace(conn, homespace):

        sql = ''' INSERT INTO homespaces(client_token, session_id)
              VALUES(?, ?) '''
        cur = conn.cursor()
        cur.execute(sql, homespace)
        conn.commit()
    
    def initial_data_homespace(conn):

        with conn:
            homespace1 = ('71A30QTXHkJTltd0ahEzJp3VFEmX-ifYIqBnL6TCgdE', 'NULL')
            homespace2 = ('2qHkLhcnh1b3TSaAM5Y6JWwubksgp38Sy03AsfVBmKw', 'NULL')
            homespace3 = ('fTginwknHutokNI3iFSXuBF8QMp5ERA4YjIDTQv1Ik', 'NULL')

            DataRepository.create_homespace(conn, homespace1)
            DataRepository.create_homespace(conn, homespace2)
            DataRepository.create_homespace(conn, homespace3)

    def create_table_notifications(conn):
        
        try:
            if conn is not None:
                
                c = conn.cursor() 

                c.execute('''CREATE TABLE IF NOT EXISTS notifications (
                                    id integer PRIMARY KEY,
                                    type integer,
                                    action integer,
                                    protocol text,
                                    homespace_id integer NOT NULL,
                                    create_at text NOT NULL,
                                    FOREIGN KEY (homespace_id) REFERENCES homespaces (id)
                                );''')

        except Error as e:
            print(e)

    def create_notification(conn, notification):

        sql = ''' INSERT INTO notifications(type, action, protocol, homespace_id, create_at)
              VALUES(?, ?, ?, ?, ?) '''
        cur = conn.cursor()
        cur.execute(sql, notification)
        conn.commit()

    def initial_data_notification(conn):

        with conn:
            notification = (3, 5, 'tcp', 1, '27-04-2021')
            DataRepository.create_notification(conn, notification)
     
if __name__ == '__main__':
    conn =  Database.create_connection()
    DataRepository.create_table_homespaces(conn)
    DataRepository.initial_data_homespace(conn)
    DataRepository.create_table_notifications(conn)
    DataRepository.initial_data_notification(conn)
    conn.close()