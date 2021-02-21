from django.contrib import admin

#importar el modelo para regstrarlo en el administrador
from .models import Alumno

# Register your models here.
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    '''Admin View for Alumno'''

    list_display = (
        'id',
        'nombre_completo',
        'boleta',
        'escuela',
        'carrera',
        'sexo',
        'descripcion',
        'fecha_registro')
    list_filter = (
        'escuela',
        'carrera',
        'sexo',)
    
    search_fields = (
        'nombre',
        'apellidos'
        'sexo',)
    
    