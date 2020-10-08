from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Estudiantes, Matriculas, Jornadas, Programas
from rest_framework import viewsets
from .serializers import EstudiantesSerializer, JornadasSerializer

# Create your views here.
# Controllers

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class EstudiantesViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer

class JornadasViewSet(viewsets.ModelViewSet):
    queryset = Jornadas.objects.all()
    serializer_class = JornadasSerializer