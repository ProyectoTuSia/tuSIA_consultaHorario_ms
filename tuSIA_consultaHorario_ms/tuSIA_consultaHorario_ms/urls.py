"""tuSIA_consultaHorario_ms URL Configuration"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('consulta_horario/', views.index, name ="index")
]
