
API_prefix = 'rac-data-extraction/v1/'

fnb_prefix = 'fnb'
recs_prefix = 'recs'
returns_prefix = 'returns'

mysql_prefix = 'mysql'

query_prefix = 'query'
filter_prefix = 'filter'
list_prefix = 'list'

service_host = '0.0.0.0'
service_port = '8000'

day_view = 'Day'
month_view = 'Month'
week_view = 'Week'

mysql_offer_table = 'MySQLOfferTable'
rac_fnb_aggregated_sales_table = 'rac_fnb_aggregated_sales'
rac_fnb_customer_insights_table = 'rac_fnb_customer_insights'
rac_fnb_customer_insights_dummy_table = 'rac_fnb_customer_insights_dummy'
rac_fnb_dummy_insights_table = 'rac_fnb_dummy_insights'
rac_fnb_dummy_insights_daily_table = 'rac_fnb_dummy_insights_daily'
rac_fnb_dummy_insights_monthly_table = 'rac_fnb_dummy_insights_monthly'
rac_fnb_dummy_insights_view_mapping_table = 'rac_fnb_dummy_insights_view_mapping'
rac_fnb_dummy_insights_weekl_table = 'rac_fnb_dummy_insights_weekly'
rac_fnb_offer_catalog_table = 'rac_fnb_offer_catalog'
rac_fnb_product_catlog_table = 'rac_fnb_product_catlog'
row_tbl_001_truncated_table = 'row_tbl_001_truncated'
w_lut_tbl_view_mapping_table = 'w_lut_tbl_view_mapping'
w_lut_tbl_ret_store_table = 'w_lut_tbl_ret_store'
w_lut_tbl_department_table = 'w_lut_tbl_department'
w_lut_tbl_prod_type_table = 'w_lut_tbl_prod_type'
w_lut_tbl_brand_table = 'w_lut_tbl_brand'

# request parameters
req_where_filter = 'where-filter'
req_limit_filter = 'limit'
req_order_by_filter = 'order-by-filter'
req_table_name = 'table-name'
req_db_name = 'data-source'
req_field_names = 'field-names'

#  exceptions
no_results_found_dict = {
    "message": "No results Found"
}

connection_failure_exception = {
    "message": "MySQL Connection Failed! Please retry"
}

get_exception = {
    "message": "An exception occurred while retrieving data"
}