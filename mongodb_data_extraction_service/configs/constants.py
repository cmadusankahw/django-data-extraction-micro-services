
API_prefix = 'rac-data-extraction/v1/'

fnb_prefix = 'fnb'
recs_prefix = 'recs'
returns_prefix = 'returns'

mongodb_prefix = 'mongodb'

query_prefix = 'query'
filter_prefix = 'filter'
list_prefix = 'list'

service_host = '0.0.0.0'
service_port = '8001'

connection_success = 'mongoDB Connection Successful'

# request parameters
req_collection_name = 'collection-name'
req_db_name = 'data-source'
req_field_names = 'field-names'
req_mongo_filters = 'mongo-filters'
req_limit_filter = 'limit'

#  exceptions
no_results_found_dict = {
    "message": "No results Found"
}

connection_failure_exception = {
    "message": "mongoDB Connection Failed! Please retry"
}

get_exception = {
    "message": "An exception occurred while retrieving data"
}