from django.contrib import admin
from django.urls import path

from TercerApp.views import *


urlpatterns = [
    path('paciente', paciente, name="TercerAppPacientes"),
    path('paciente/<nombre>/<apellido>', paciente, name="TercerAppPacientes"),
    #path('protocolo/<nombre_protocolo>', protocolo, name="TercerAppProtocolo"),
]
