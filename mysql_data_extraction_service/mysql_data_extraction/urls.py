"""
    mysql_data_extraction URL Configuration
"""
from django.urls import path

from mysql_data_extraction.views import DataViewSet
from configs.constants import mysql_prefix, query_prefix, filter_prefix, list_prefix

urlpatterns = [
    path(f'{mysql_prefix}/{list_prefix}/<str:db>/<str:table>', DataViewSet.as_view({
        'get': 'get_all',
    })),
    path(f'{mysql_prefix}/{list_prefix}', DataViewSet.as_view({
        'get': 'get_all_query_data',
    }))
]