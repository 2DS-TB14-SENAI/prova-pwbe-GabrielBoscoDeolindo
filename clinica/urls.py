from django.urls import path
from . import views

urlpatterns = [
    path('/medicos/', views.listar_medicos),
    path('/consultas/nova/', views.criar_consulta),
    # path('/consultas/<int:id>/', views.detalhes_consulta),
]