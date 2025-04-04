from django.urls import path
from . import views

urlpatterns = [
    path('api/servicos/', views.criar_servico),
    path('api/servicos/', views.listar_servicos),
    path('api/servicos/<int:pk>', views.servico_especifico),
    path('api/agendamentos/', views.criar_agendamento),
    path('api/agendamentos/', views.listar_agendamento),
    path('api/agendamentos/<int:pk>', views.agendamento_especifico),
]