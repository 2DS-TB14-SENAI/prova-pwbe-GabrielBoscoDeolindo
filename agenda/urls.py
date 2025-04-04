from django.urls import path
from . import views

urlpatterns = [
    path('servicos/', views.listar_servicos),
    path('servicos/<int:pk>', views.servico_especifico),
    path('agendamentos/', views.listar_agendamento),
    path('agendamentos/<int:pk>', views.agendamento_especifico),
]