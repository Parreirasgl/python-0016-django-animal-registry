from django.urls import path
from . import views

urlpatterns = [
    path("busca", views.buscar, name='path_buscar'),
    path("<nome_animal>/edicao", views.editar_registro, name='path_editar_registro'),
    path("confirma", views.confirmar, name='path_confirmar'),
    # path("<nome>/confirma", views.confirmar1, name='path_confirmar1'),
    ]
