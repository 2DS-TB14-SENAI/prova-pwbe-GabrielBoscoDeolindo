from django.urls import path
from . import views

urlpatterns = [
    path('auth/registro/', view=views.create_user),
    path('auth/login/', view=views.login),
]