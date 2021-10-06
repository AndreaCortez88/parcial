from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# -------------------------------------
class ResourceEmpleado(resources.ModelResource):
    class Meta:
        model = Empleado

class AdminEmpleado(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['pk_empleado', 'nombre', 'telefono', 'usuario', 'contraseña']
    resource_class = ResourceEmpleado

admin.site.register(Empleado, AdminEmpleado)

class Resourceordenador(resources.ModelResource):
    class Meta:
        model = ordenador

class Adminordenador(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre_ordenador']
    list_display = ['pk_ordenador', 'nombre_ordenador', 'num_ordenador']
    resource_class = Resourceordenador

admin.site.register(ordenador, Adminordenador)