import os
import configparser
from .database import Database

#   Arquivo de configuração
CONFIG_FILE = 'hsu.cfg'
CONFIG_PATH = ''.join([str(os.path.dirname(os.path.abspath(__file__))), '/', CONFIG_FILE])

if os.path.exists(CONFIG_PATH):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
else:
    print(f'Conf file not found: {CONFIG_FILE}')

