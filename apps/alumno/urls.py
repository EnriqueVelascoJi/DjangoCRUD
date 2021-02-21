from django.urls import path

#Importar las vistas
from . import views
#Nombre de la aplicación para hacer referencia a las URL's
app_name = "alumno_app"

urlpatterns = [
    
    #Rutas de la aplicación 'alumno'
    path('', views.Inicio.as_view(), name="inicio"),
    path('registrar_alumno/', views.registrar_alumno, name="registrar_alumno"),
    path('listar_alumnos/', views.listar_alumnos, name="listar_alumnos"),
    path('eliminar_alumno/<int:id_alumno>', views.borrar_alumno, name="borrar_alumno"),
    path('editar_alumno/<int:id_alumno>', views.editar_alumno, name = "editar_alumno"),
    path('ver_alumno/<int:id_alumno>', views.ver_alumno, name = "ver_alumno")

]