from distutils.log import error
from pymongo import MongoClient
import json
from bson import json_util, ObjectId
from bson.json_util import dumps
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer

from . import utils

# Create your views here.

@api_view(['GET','PUT'])
def CRUDschedule(request,userId):
    client = MongoClient()
    schedule_collection = client["tuSIA_consultaHorario_db"]["schedule"]

    schedule_data = schedule_collection.objects.find_one({'userId' : userId})

    if request.method == 'PUT':

        if not(schedule_data):
            try:
                schedule_collection.objects.insert_one(request.data)
                # return Response({"message": "Schedule added into the DB!")
            except :
                return Response({"message": "Something went wrong insterting data", "status": Response.status_code})

            return Response({"message": "Schedule added into the DB!"})
        
        else:
            try:
                schedule_collection.objects.replace_one({'userId':userId},request.data)
            except:
                return Response({"message": "Something went wrong", "status": Response.status_code})

            return Response({"message": "Schedule replaced into the DB!"})

    if request.method == 'GET':

        # schedule_serializer = ScheduleSerializer(schedule_data)
        schedule_json = json.loads(json_util.dumps(schedule_data))
        return Response({'data':schedule_json})


        # dbResponse = utils.get_db_handle()

        # schedules = dbResponse[1]
        # client = dbResponse[2]

        # details = schedules.find_one({"userId":userId})
        #     # if details:
        #     #     pass
        # print(type(details))
        # d_js = json.loads(json_util.dumps(details))
        # client.close()

        # return Response({'data':d_js})
