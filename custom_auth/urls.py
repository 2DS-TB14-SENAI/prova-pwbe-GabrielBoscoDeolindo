from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', view=views.create_user),
    path('auth/login/', view=views.login),
    path('auth/profile/', view=views.profile)
]