from pymongo import MongoClient
import json
from bson import json_util, ObjectId
from bson.json_util import dumps
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer

from . import utils



@api_view(['GET','PUT'])
def CRUDschedule(request,userId):
    #local connection
    # client = MongoClient()
    # schedule_collecion = client["tuSIA_consultaHorario_db"]["schedule"]

    # remote connection
    utils_data = utils.get_db_handle()
    schedule_collection = utils_data[1]
    client = utils_data[2]

    schedule_data = schedule_collection.find_one({'userId' : userId})

    if request.method == 'PUT':

        if not(schedule_data):
            try:
                schedule_collection.insert_one(request.data)
                # return Response({"message": "Schedule added into the DB!")
            except :
                return Response({"message": "Something went wrong insterting data", "status": Response.status_code})

            return Response({"message": "Schedule added into the DB!"})
        
        else:
            try:
                print(request.data)
                currentSchedule = json.loads(json_util.dumps(schedule_data))
                schedule_collection.replace_one({'userId':userId},request.data)

            except Exception as inst:

                return Response({"message": inst, "status": Response.status_code})

            return Response({"message": "Schedule replaced into the DB!"})

    if request.method == 'GET':

        # schedule_serializer = ScheduleSerializer(schedule_data)
        schedule_json = json.loads(json_util.dumps(schedule_data))
        return Response({'data':schedule_json})
