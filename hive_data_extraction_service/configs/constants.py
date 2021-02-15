
API_prefix = 'rac-data-extraction/v1/'

fnb_prefix = 'fnb'
recs_prefix = 'recs'
returns_prefix = 'returns'

hive_prefix = 'hive'

query_prefix = 'query'
filter_prefix = 'filter'
list_prefix = 'list'

service_host = '0.0.0.0'
service_port = '8002'

get_exception = 'An exception occurred while retrieving data'

connection_success = 'hive Connection Successful'

# request parameters
req_db_name = 'data-source'
req_where_filter = 'where'
req_order_by_filter = 'order-by'
req_limit_filter = 'limit'
req_table_name = 'table-name'
req_field_names = 'field-names'
req_hive_filters = 'hive-filters'

#  exceptions
no_results_found_dict = {
    "message": "No results Found"
}

connection_failure_exception = {
    "message": "hive Connection Failed! Please retry"
}

get_exception = {
    "message": "An exception occurred while retrieving data"
}