from http import client
import json
from bson import json_util, ObjectId
from bson.json_util import dumps
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


#  @api_view(['POST'])
# def postSchedule(request,userId):
#     print('hola mundo')
#     schedule = request.data
#     print(schedule)
#     return Response({'message':'OK'})
