import json

from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
import sys

from configs.constants import *
from configs.db_connection import connection, logging


class DataViewSet(viewsets.ViewSet):
    # GET with a HBase query
    # rac-data-extraction/v1/hbase/list
    def get_all_query_data(self, request):
        try:
            if connection is not None:
                body = json.loads(request.body)

                table_name = body[req_table_name]
                data = None

                if table_name in body:
                    if req_field_names in body:
                        field_names = body[req_field_names]
                    else:
                        field_names = '*'

                    if req_hive_filters in body:
                        query = f'WHERE {body[req_hbase_filters]}'
                    else:
                        query = ''

                    # ToDo HBASE Query

                if data is not None:
                    return json.dumps(data)
                else:
                    return HttpResponse(status=404)
            else:
                return HttpResponse(status=401)
        except:
            return HttpResponse(status=500)