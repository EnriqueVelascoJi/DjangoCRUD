from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.

class Alumno(models.Model):
    """Model definition for Alumno."""
    
    #Opciones de género
    genero = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('O', 'Otro'),
    ]


    # TODO: Define fields here
    nombre = models.CharField("Nombre", max_length = 100)
    apellidos = models.CharField("Apellidos", max_length = 100)
    sexo = models.CharField('Género', max_length=1, choices = genero)
    boleta =  models.CharField("Boleta", max_length = 10, unique=True)
    escuela = models.CharField("Escuela", max_length = 50)
    carrera = models.CharField("Carrera", max_length = 50)
    descripcion = RichTextField(default="Ninguna")
    fecha_registro = models.DateTimeField("Fecha de registro", auto_now=True)
    avatar = models.ImageField("Fotografía", upload_to='alumno', blank=True, null=True)

    class Meta:
        """Meta definition for Alumno."""

        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

        

    def __str__(self):
        """Unicode representation of Alumno."""
        return str(self.id) + ".- " + str(self.nombre) + " " + str(self.apellidos) + " -- " + str(self.boleta)
    

    @property
    def nombre_completo(self):
        """Regresa el nombre completo del alumno"""
        return '%s %s' % (self.nombre, self.apellidos)