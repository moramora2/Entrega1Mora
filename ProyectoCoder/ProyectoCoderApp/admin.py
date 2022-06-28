from django.contrib import admin

from .models import *

# Register your models here.
    

class VehiculoAdmin(admin.ModelAdmin):

    list_display = ('marca', 'modelo', 'anio')
    
   
    
class RepuestoAdmin(admin.ModelAdmin):

    list_display = ('marca', 'modelo')



class AccesorioAdmin(admin.ModelAdmin):

    list_display = ('marca', 'modelo', 'precio')






admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Repuesto, RepuestoAdmin)
admin.site.register(Accesorio, AccesorioAdmin)

# nacho, admin -> python manage.py createsuperuser