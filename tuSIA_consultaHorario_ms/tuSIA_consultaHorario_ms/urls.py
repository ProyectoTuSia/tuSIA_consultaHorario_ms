"""tuSIA_consultaHorario_ms URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('consulta_horario/', include('schedule.urls'))
    # path('consulta_horario/<str:userId>', views.readSchedule, name ="readSchedule"),
    # path('crear_horario/<str:userId>', views.postSchedule, name ="postSchedule")

]
