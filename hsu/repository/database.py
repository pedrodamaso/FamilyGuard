import sqlite3
import configparser
import os

class Database(object):
    
    def create_connection():
        conn = None
        try:
            config_path = os.path.dirname(os.path.abspath(__file__))
            config = configparser.ConfigParser()
            config.read(os.path.join(config_path, 'hsu.cfg'))

            conn = sqlite3.connect(config.get('DB','DB_LOCATION'))
            return conn

        except sqlite3.Error as e:
            print(e)
                
        return conn
    
    def close(self):
        self.conn.close()
        