from django.urls import path
from .views import registro, home, perfil_usuario

urlpatterns = [
    path('', home, name='home'),
    path('registro/', registro, name='registro'),
    path('perfil/', perfil_usuario, name='perfil'),
]