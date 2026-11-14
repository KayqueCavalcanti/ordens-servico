from django.urls import path

from . import views

app_name = "ordens"

urlpatterns = [
    path("clientes/", views.cliente_lista, name="cliente_lista"),
]
