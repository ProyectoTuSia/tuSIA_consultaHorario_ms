"""schedule URL Configuration"""

from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:userId>', views.CRUDschedule, name ="CRUDschedule")
    # # path('crear_horario/<str:userId>', views.postSchedule, name ="postSchedule")
]