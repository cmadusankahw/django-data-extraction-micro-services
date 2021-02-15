
API_prefix = 'rac-data-extraction/v1/'

fnb_prefix = 'fnb'
recs_prefix = 'recs'
returns_prefix = 'returns'

hbase_prefix = 'hbase'

query_prefix = 'query'
filter_prefix = 'filter'
list_prefix = 'list'

service_host = '0.0.0.0'
service_port = '8003'

connection_success = 'Hbase Connection Successful'

# request parameters
req_table_name = 'table-name'
req_field_names = 'filed-names'
req_hbase_filters = 'hbase-filters'

#  exceptions
no_results_found_dict = {
    "message": "No results Found"
}

connection_failure_exception = {
    "message": "hbase Connection Failed! Please retry"
}

get_exception = {
    "message": "An exception occurred while retrieving data"
}
