from django.shortcuts import render
from TercerApp.models import Paciente
from TercerApp.forms import PacienteForm, ProtocoloForm, SiteForm, BusquedaPacienteForm



def pacientes(request):
    all_pacientes = Paciente.objects.all()
    context = {
        "pacientes": all_pacientes
    }
    return render(request, "TercerApp/paciente.html", context=context)

def crear_paciente(request):
    if request.method == "POST":
        mi_formulario = PacienteForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            paciente_save = Curso(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                numero_paciente = ['numero_paciente'],
                ojo_estudio = ['ojo_estudio'],
            )
            paciente_save.save()
    all_paciente = Paciente.objects.all()
    context = {
        "paciente": all_paciente,
        "form": PacienteForm(),
        "form_busqueda": BusquedaPacienteForm(),
    }
    return render(request, "TercerApp/paciente.html", context=context)
#
#
#
#
# def busqueda_protocolo(request):
#     #mostar datos filtrados
#     mi_formulario = PacienteForm(request.GET)
#     if mi_formulario.is_valid():
#         informacion = mi_formulario.cleaned_data
#         pacientes_filtrados = Paciente.objects.filter(nombre__icontains=informacion['nombre_protocolo'])
#         context = {
#             "Protocolo": ProtocoloForm()
#         }
#     return render(request, "TercerApp/busqueda_protocolo.html", context=context)
#
#
# def busqueda_site(request):
#     #mostar datos filtrados
#     mi_formulario = PacienteForm(request.GET)
#     if mi_formulario.is_valid():
#         informacion = mi_formulario.cleaned_data
#         pacientes_filtrados = Paciente.objects.filter(nombre__icontains=informacion['nombre_site'])
#         context = {
#             "Site": SiteForm()
#         }
#     return render(request, "TercerApp/busqueda_site.html", context=context)


def protocolo(request):
    return render(reequest, base.html)

def site(request):
    return render(request, base.html)






# from django.http import HttpResponse
#
# # def saludo(request):
# #
# #     return HttpResponse("Hola Django - Coder")

