from django.contrib import admin
from django.urls import path

from TercerApp.views import *


urlpatterns = [
    path('pacientes', pacientes, name="TercerAppPacientes"),
    path('paciente/<nombre>/<apellido>', crear_paciente, name="TercerAppPaciente"),
    path('protocolo/<nombre_protocolo>', protocolo, name="TercerAppProtocolo"),
    path('site/<nombre_site>', site, name="TercerAppSite"),
]
