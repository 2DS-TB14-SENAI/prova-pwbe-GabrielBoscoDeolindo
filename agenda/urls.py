from django.urls import path
from . import views

urlpatterns = [
    path('api/servicos/', views.criar_servico),
    path('api/servicos/', views.listar_servicos),
    path('api/servicos/<int:pk>', views.servico_especifico),
]