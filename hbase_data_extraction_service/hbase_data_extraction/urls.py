"""
    hbase_data_extraction URL Configuration
"""
from django.urls import path

from hbase_data_extraction.views import DataViewSet
from configs.constants import hbase_prefix, list_prefix

urlpatterns = [
    path(f'{hbase_prefix}/{list_prefix}/<str:collection>', DataViewSet.as_view({
        'get': 'get_all',
    })),
    path(f'{hbase_prefix}/{list_prefix}', DataViewSet.as_view({
        'get': 'get_all_query_data',
    })),
]