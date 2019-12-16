from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'bonoelite/home.html')


def maestro_trabajador(request):
    listtrabajadores = maestrotrabajadores.objects.all()
    return render(request, 'bonoelite/maestro_trabajador.html', {'listtrabajadores':listtrabajadores})


def eliminarTrabajador(request, id):
    maestrotrabajadores.objects.get(id=id).delete()
    return redirect('maestro_trabajador')
