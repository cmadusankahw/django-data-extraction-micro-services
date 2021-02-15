import urllib
import logging
from pyhive import hive
from configs.constants import connection_failure_exception,connection_success
from configs.keys import *
import thrift_sasl

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

connection = None

try:
    # Connect to HiveServer2
    connection = hive.connect(host = hive_host, port = hive_port).cursor()
    logging.info(connection_success)

except Exception as e:
    logging.error(e)
    logging.error(connection_failure_exception)
