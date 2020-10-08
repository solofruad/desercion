from django.urls import path, include

from .views import HomePageView, AboutPageView, EstudiantesViewSet, JornadasViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudiantes', EstudiantesViewSet)
router.register('jornadas', JornadasViewSet)

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('home',HomePageView.as_view(), name='home'),
    path('about',AboutPageView.as_view(), name='about'),
    path('api/v1/',include(router.urls)),
]