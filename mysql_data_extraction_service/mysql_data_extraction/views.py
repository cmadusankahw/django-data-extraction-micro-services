import sys
import time

from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
import logging

from mysql_data_extraction.serializers import GeneralSerializer
from configs.constants import *
from mysql_data_extraction.models import *

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


class DataViewSet(viewsets.ViewSet):
    # GET return all data for a given model(table) and a database
    # rac-data-extraction/v1/mysql/list/<str:database>/<str:table>
    def get_all(self, request, db=None, table=None):
        data_model = getattr(sys.modules[__name__], table)
        data = data_model.objects.using(db).all()
        GeneralSerializer.Meta.model = data_model
        serializer = GeneralSerializer(data, many=True)
        return Response(serializer.data)

    # GET with a raw SQL query
    # rac-data-extraction/v1/mysql/list
    def get_all_query_data(self, request):
        try:
            db_name = request.GET.get(req_db_name, None)
            table_name = request.GET.get(req_table_name, None)
            filed_names = request.GET.get(req_field_names, None)
            where_filter = request.GET.get(req_where_filter, None)
            order_by_filter = request.GET.get(req_order_by_filter, None)
            limit_filter = request.GET.get(req_limit_filter, None)

            if db_name is not None and table_name is not None:

                if filed_names is None:
                    filed_names = '*'

                query_statement = f'SELECT {filed_names} FROM {table_name}'

                if where_filter is not None:
                    query_statement = query_statement + f' WHERE {where_filter}'

                if order_by_filter is not None:
                    query_statement = query_statement + f' ORDER BY {order_by_filter}'

                if limit_filter is not None:
                    query_statement = query_statement + f' LIMIT {limit_filter}'

                logging.info(query_statement)
                data_model = getattr(sys.modules[__name__], table_name)
                data = data_model.objects.using(db_name).raw(query_statement)

                GeneralSerializer.Meta.model = data_model
                serializer = GeneralSerializer(data, many=True)
                return Response(serializer.data)
            else:
                return HttpResponse(status=404)
        except:
            return HttpResponse(status=500)
