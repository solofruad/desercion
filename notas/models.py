from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

SEXO = (
    ("f","Femenino"),
    ("m","Masculino")
)

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=200)
    documento = models.CharField(max_length=100, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO, default='m') #m f
    telefono = models.CharField(max_length=70,default="")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = _('Estudiantes')

class Programas(models.Model):
    snies = models.CharField(max_length=200, unique=True)
    nombre = models.CharField(max_length=400)

    def __str__(self):
        return self.nombre   
         
    class Meta:
        verbose_name_plural = _('Programas')

class Jornadas(models.Model):    
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = _('Jornadas')

class Matriculas(models.Model):
    programa = models.ForeignKey(Programas, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    jornada = models.ForeignKey(Jornadas, on_delete=models.CASCADE)
    periodo = models.IntegerField()
    anio = models.IntegerField()
    semestre = models.IntegerField()

    def __str__(self):
        return str({self.estudiante, self.programa, self.jornada})
    
    class Meta():
        verbose_name_plural = _("Matriculas")
