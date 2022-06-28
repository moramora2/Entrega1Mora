from django import forms
    
    
class NuevoVehiculo(forms.Form):

    marca = forms.CharField(max_length=30,label="Marca")
    modelo = forms.CharField(max_length=30,label="Modelo")
    anio = forms.IntegerField(min_value=1900,label="Año")
    
    
class NuevoRepuesto(forms.Form):

    marca = forms.CharField(max_length=30,label="Marca")
    modelo = forms.CharField(max_length=30,label="Modelo")
    
class NuevoAccesorio(forms.Form):

    marca = forms.CharField(max_length=30,label="Marca")
    modelo = forms.CharField(max_length=30,label="Modelo")
    precio = forms.IntegerField(min_value=1,label="Precio")