from rest_framework import serializers
from .models import Estudiantes, Matriculas, Jornadas, Programas


class EstudiantesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudiantes
        fields = ['nombre','documento','sexo','telefono']


class JornadasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jornadas
        fields = ['nombre']


