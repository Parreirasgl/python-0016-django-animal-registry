from django.urls import path
from . import views

urlpatterns = [
    path("", views.editar_registro, name='editar_registro'),
    path('/success', views.confirmacao, name='registro_editado_sucesso'),
    ]
