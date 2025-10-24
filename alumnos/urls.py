from django.urls import path
from . import views
from .views import Alumno

urlpatterns = [
    path('', views.lista_alumnos, name='lista'),              # Listado principal
    path('crear/', views.crear_alumno, name='crear'),         # Crear alumno
    path('editar/<int:pk>/', views.editar_alumno, name='editar'),  # Editar alumno
    path('eliminar/<int:pk>/', views.eliminar_alumno, name='eliminar'),  # Eliminar alumno
    path('detalle/<int:pk>/', views.detalle_alumno, name='detalle'),     # Detalle alumno
]
