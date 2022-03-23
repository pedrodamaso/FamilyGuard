import sqlite3
from sqlite3 import Error

class Database(object):
    
    DB_LOCATION = "/home/pedro/Documentos/family-guard/code/csa/repository/csa.db"
     
    def create_connection():
        conn = None
        try:
            conn = sqlite3.connect(Database.DB_LOCATION)
            return conn
        except Error as e:
            print(e)
                
        return conn
    
    def close(self):
        self.conn.close()
        