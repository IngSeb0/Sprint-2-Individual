from django.urls import path
from . import views

urlpatterns = [
    path('visualizar_paciente/<int:paciente_id>/', views.visualizar_imagenes_paciente, name='visualizar_imagenes_paciente'),
    path('seleccionar_paciente/', views.seleccionar_paciente, name='seleccionar_paciente'),
]