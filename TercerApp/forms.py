from django import forms


class PacienteForm(forms.Form):

    nombre = forms.CharField(max_length=40) #nombre
    apellido = forms.CharField(max_length=40) #apellido
    numero_paciente = forms.IntegerField() #numero que identifca al paciente dentro del protocolo
    ojo_estudio = forms.CharField(max_length=2)



class ProtocoloForm(forms.Form):
    nombre_protocolo = forms.CharField(max_length=50)  # nombre
    numero_protocolo = forms.IntegerField()


class SiteForm(forms.Form):
    nombre_site = forms.CharField(max_length=50)  # nombre del centro medico
    numero_site = forms.IntegerField()