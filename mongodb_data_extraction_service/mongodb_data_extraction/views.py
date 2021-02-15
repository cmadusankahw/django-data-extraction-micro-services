import json
from bson import json_util
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
import sys
import time

from configs.constants import *
from configs.db_connection import connection, logging


class DataViewSet(viewsets.ViewSet):
    # GET with a mongoDB query
    # rac-data-extraction/v1/mongodb/list
    def get_all_query_data(self, request):
        try:
            if connection is not None:
                collection_name = request.GET.get(req_collection_name, None)
                db_name = request.GET.get(req_db_name, None)
                field_names = request.GET.get(req_field_names, None)
                filters = request.GET.get(req_mongo_filters, None)
                limit_filter = request.GET.get(req_limit_filter, None)

                db = connection[db_name]
                collection = db[collection_name]

                if limit_filter is not None:
                    data = list(collection.find({}).limit(int(limit_filter)))
                else:
                    data = list(collection.find({}))
                serialized_data = json.loads(json_util.dumps(data))

                return Response(serialized_data)  # json_utils required to serialize ObjectId
            else:
                return HttpResponse(status=404)
        except:
            return HttpResponse(status=500)
