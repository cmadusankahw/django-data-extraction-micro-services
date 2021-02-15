"""
    mongo_db_data_extraction URL Configuration
"""
from django.urls import path

from mongodb_data_extraction.views import DataViewSet
from configs.constants import mongodb_prefix, list_prefix

urlpatterns = [
    path(f'{mongodb_prefix}/{list_prefix}', DataViewSet.as_view({
        'get': 'get_all_query_data',
    })),
]