from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#Vistas genericas de Django
from django.views.generic import TemplateView

#Importar el formulario
from .forms import AlumnoForm

#Registro de fecha
from django.utils import timezone

#Importar el modelo
from .models import Alumno

#CRSF
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.


#Vista de inicio de los Alumnos
class Inicio(TemplateView):
    template_name = "inicio.html"

#Vista para registrar a los alumnos
@csrf_exempt
def registrar_alumno(request):

    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST)
            post = form.save()
            
            return HttpResponseRedirect('/listar_alumnos')
        else:
            errores = form.errors
            print(errores)
            return render(request, 'alumno/agregar_alumno.html', {
                'formulario': form,
                'errores': errores
            })
            
            
    else:
        
        form = AlumnoForm()
    return render(request, 'alumno/agregar_alumno.html', {
        'formulario': form
    })

#Listar alumnos
def listar_alumnos(request):

    alumnos = Alumno.objects.all()
    return render(request, 'alumno/listar_alumnos.html', {
        'alumnos': alumnos
    })

#Eliminar
@csrf_exempt
def borrar_alumno(request, id_alumno):

    alumno = Alumno.objects.get(id = id_alumno)
    alumno.delete()
    
    return HttpResponseRedirect('/listar_alumnos')

    


@csrf_exempt
def editar_alumno(request, id_alumno):
    alumno = Alumno.objects.get( id = id_alumno )

    
    if request.method == "GET":
        print(alumno.avatar)
        form = AlumnoForm({
            'nombre': alumno.nombre,
            'apellidos': alumno.apellidos,
            'boleta': alumno.boleta,
            'escuela': alumno.escuela,
            'carrera': alumno.carrera,
            'sexo': alumno.sexo,
            'descripcion': alumno.descripcion,
            'avatar': alumno.avatar,

        })
        return render(request, 'alumno/editar_alumno.html', {
            'formulario': form,
            'alumno': alumno,
            'metodo': 0
        })

    elif request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES, instance = alumno)
        if form.is_valid():
            
            alumno = form.save(commit =  False)
            alumno.save()

            return HttpResponseRedirect('/listar_alumnos')
        else:
            return render(request, 'alumno/editar_alumno.html', {
                'formulario': form,
                'alumno': alumno
            })
            
            
    else:
        
        
        form = AlumnoForm()
    return render(request, 'alumno/editar_alumno.html', {
        'formulario': form
    })

    return HttpResponseRedirect('/listar_alumnos')


#Visualizar la información del alumno
def ver_alumno(request, id_alumno):

    alumno = Alumno.objects.get( id = id_alumno )
    

    return render(request, 'alumno/ver_alumno.html', {
        'alumno': alumno,
    })