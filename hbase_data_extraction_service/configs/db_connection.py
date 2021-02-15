import urllib
import logging

import pybase
# from configs.constants import connection_failure_exception, connection_success
# from configs.keys import *
# from kazoo.client import KazooClient


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

connection = None

try:
    # Connect to HBase Thrift server
    # zk = KazooClient(hosts='***:2181')
    # zk.start()
    # zk.get('***')
    connection = pybase.connect('***', 9090)
    # logging.info(connection.tables())
    # logging.info(connection['***'].get('***'))  # test
    logging.info('con success')
except Exception as e:
    logging.error(e)
    logging.error('con failed')
