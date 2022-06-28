from django.urls import path
from .views import *



urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', inicio, name="inicio"),
    
    path('vehiculos/', vehiculos, name="vehiculos"),
    path('ingresar_vehiculo/', ingresar_vehiculo, name="ingresar_vehiculo"),
    
    path('repuestos/', repuesto, name="repuestos"),
    path('ingresar_repuesto/', ingresar_repuesto, name="ingresar_repuesto"),
    
    path('accesorios/', accesorios, name="accesorios"),
    path('ingresar_accesorio/', ingresar_accesorio, name="ingresar_accesorio"),
    
    
    

    
    path('entregables/', entregables, name="entregables"),
    # path('base/', base),
]
