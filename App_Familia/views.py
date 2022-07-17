from django.shortcuts import render
from App_Familia.models import Familiar
from django.http import HttpResponse

# Create your views here.
def familia(self, nombre, apellido, dni, fecha_de_nacimiento):
    familia = Familiar(nombre=nombre, apellido=apellido, dni=dni, fecha_de_nacimiento=fecha_de_nacimiento)
    familia.save()
    documento = f'Se ha ingresado a {nombre} {apellido} a la lista de familiares.'
    return HttpResponse(documento)

def vista_familia(self):
    lista = Familiar.objects.all()
    return render(self, "lista_familiares.html",{"lista_familiares": lista})


