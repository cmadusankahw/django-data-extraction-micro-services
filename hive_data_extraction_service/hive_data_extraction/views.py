import time
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from configs.constants import *
from configs.db_connection import connection, logging


class DataViewSet(viewsets.ViewSet):
    # GET with a HQL query
    # rac-data-extraction/v1/hive/list
    def get_all_query_data(self, request):
            if connection is not None:
                db_name = request.GET.get(req_db_name, None)
                table_name = request.GET.get(req_table_name, None)
                filed_names = request.GET.get(req_field_names, None)
                where_filter = request.GET.get(req_where_filter, None)
                order_by_filter = request.GET.get(req_order_by_filter, None)
                limit_filter = request.GET.get(req_limit_filter, None)

                try:
                    if db_name is not None and table_name is not None:

                        if filed_names is None:
                            filed_names = '*'

                        query_statement = f'SELECT {filed_names} FROM {db_name}.{table_name}'

                        if where_filter is not None:
                            query_statement = query_statement + f' WHERE {where_filter}'

                        if order_by_filter is not None:
                            query_statement = query_statement + f' ORDER BY {order_by_filter}'

                        if limit_filter is not None:
                            query_statement = query_statement + f' LIMIT {limit_filter}'

                        connection.execute(query_statement)
                        col_names = [i[0].split('.')[1] for i in connection.description]
                        data = connection.fetchall()

                        if data is not None and col_names is not None:
                            response_data = self.map_resultset(data, col_names)
                            return Response(response_data)
                        else:
                            return HttpResponse(status=404)
                    else:
                        return HttpResponse(status=404)
                except:
                    return HttpResponse(status=500)

    def map_resultset(self, data, col_names):
        try:
            final_list = []
            for d in data:
                dict = {}
                i = 0
                for row in d:
                    dict[col_names[i]] = row
                    i = i+1
                final_list.append(dict)
            return final_list
        except:
            return None