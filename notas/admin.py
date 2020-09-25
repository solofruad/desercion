from django.contrib import admin
from .models import Estudiantes, Jornadas, Matriculas, Programas 

class EstudiantesAdmin(admin.ModelAdmin):    
    search_fields = ['nombre','documento']
    list_display = ('documento','nombre','sexo','telefono')

class ProgramasAdmin(admin.ModelAdmin):
    list_display = ('nombre','snies')

class MatriculasAdmin(admin.ModelAdmin):
    list_filter = ['programa','jornada']
    search_fields = ['anio']
    list_display = ('estudiante','programa','jornada','anio','periodo','semestre')

admin.site.register(Matriculas, MatriculasAdmin)
admin.site.register(Estudiantes, EstudiantesAdmin)
admin.site.register(Programas)
admin.site.register(Jornadas)
