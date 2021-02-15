import urllib
import pymongo
from pymongo import MongoClient
import logging
from configs.constants import connection_failure_exception,connection_success
from configs.keys import *

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

connection = None

try:
    # MONGO_DATABASE_HOST = f'mongodb+srv://{mongo_user}:{mongo_pass}@{mongo_host}/{mongo_db}'
    # connection = mongoengine.connect(mongo_db, host=f"{mongo_host}:{mongo_port}").cursor()
    connection = MongoClient(mongo_host, mongo_port)
    logging.info(connection_success)
except:
    logging.error(connection_failure_exception)