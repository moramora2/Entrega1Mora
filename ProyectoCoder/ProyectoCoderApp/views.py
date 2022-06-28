import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Accesorio, Vehiculo, Repuesto, Accesorio
from .forms import NuevoRepuesto, NuevoVehiculo, NuevoAccesorio
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy

# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})


    
    
    
    

def vehiculos(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            vehiculos = Vehiculo.objects.filter( Q(marca__icontains=search) | Q(modelo__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/vehiculos.html",{"vehiculos":vehiculos, "search":True, "busqueda":search})

    vehiculos = Vehiculo.objects.all()

    return render(request,"ProyectoCoderApp/vehiculos.html",{"vehiculos":vehiculos, "search":False})


def ingresar_vehiculo(request):
    
    # post
    if request.method == "POST":
        
        formulario = NuevoVehiculo(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            vehiculo = Vehiculo(marca=info["marca"],modelo=info["modelo"],anio=info["anio"])
            vehiculo.save()

            return redirect("vehiculos")

        return render(request,"ProyectoCoderApp/vehiculos_form.html",{"form":formulario,"accion":"Ingresar"})
    
       # get
    formulario = NuevoVehiculo()
    return render(request,"ProyectoCoderApp/vehiculos_form.html",{"form":formulario,"accion":"Ingresar"})
 
    
    
    
    
def repuesto(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            repuestos = Repuesto.objects.filter( Q(marca__icontains=search) | Q(modelo__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/repuestos.html",{"repuestos":repuestos, "search":True, "busqueda":search})

    repuestos = Repuesto.objects.all()

    return render(request,"ProyectoCoderApp/repuestos.html",{"repuestos":repuestos, "search":False})


def ingresar_repuesto(request):
    
    # post
    if request.method == "POST":
        
        formulario = NuevoRepuesto(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            repuesto = Repuesto(marca=info["marca"],modelo=info["modelo"])
            repuesto.save()

            return redirect("repuestos")

        return render(request,"ProyectoCoderApp/repuestos_form.html",{"form":formulario,"accion":"Ingresar"})
    
    
           # get
    formulario = NuevoRepuesto()
    return render(request,"ProyectoCoderApp/repuestos_form.html",{"form":formulario,"accion":"Ingresar"})
    
    
    
    
def accesorios(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            acceosrios = Accesorio.objects.filter( Q(marca__icontains=search) | Q(modelo__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/accesorios.html",{"accesorios":accesorios, "search":True, "busqueda":search})

    accesorios = Accesorio.objects.all()

    return render(request,"ProyectoCoderApp/accesorios.html",{"accesorios":accesorios, "search":False})


def ingresar_accesorio(request):
    
    # post
    if request.method == "POST":
        
        formulario = NuevoAccesorio(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            accesorio = Accesorio(marca=info["marca"],modelo=info["modelo"],precio=info["precio"])
            accesorio.save()

            return redirect("accesorios")

        return render(request,"ProyectoCoderApp/accesorios_form.html",{"form":accesorio,"accion":"Ingresar"})
    
    
           # get
    formulario = NuevoAccesorio()
    return render(request,"ProyectoCoderApp/accesorios_form.html",{"form":formulario,"accion":"Ingresar"})
    
    











def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):
    return HttpResponse("Vista de entregables")