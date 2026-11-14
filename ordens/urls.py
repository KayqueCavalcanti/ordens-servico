from django.urls import path

from . import views

app_name = "ordens"

urlpatterns = [
    path("clientes/", views.cliente_lista, name="cliente_lista"),
    path("clientes/novo/", views.cliente_novo, name="cliente_novo"),
    path("clientes/<int:pk>/", views.cliente_detalhe, name="cliente_detalhe"),
]
