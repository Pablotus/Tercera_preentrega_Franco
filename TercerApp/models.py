from django.db import models



class Paciente(models.Model):

    nombre = models.CharField(max_length=40) #nombre
    apellido = models.CharField(max_length=40) #apellido
    numero_paciente = models.IntegerField() #numero que identifca al paciente dentro del protocolo
    ojo_estudio = models.CharField(max_length=2) #Puede ser ojo derecho(OD) u ojo izquierdo (OI)

    def __str__(self):
        return f"paciente:{self.nombre}, apellido:{self.apellido}, numero_paciente:{self.numero_paciente}, ojo_estudio:{self.ojo_estudio}"


class Protocolo(models.Model):
    nombre_protocolo = models.CharField(max_length=50)  # nombre
    numero_protocolo = models.IntegerField() #codigo que identifica al protocolo

    def __str__(self):
        return f"protocolo:{self.nombre_protocolo}, numero_protocolo:{self.numero_protocolo}"


class Site(models.Model):
    nombre_site = models.CharField(max_length=50)  # nombre del centro medico
    numero_site = models.IntegerField() #codigo que identifica al centro medico

    def __str__(self):
        return f"site:{self.nombre_site}, numero_site:{self.numero_site}"

