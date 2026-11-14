from django.shortcuts import render

from .models import Cliente

def cliente_lista(request):
    clientes = Cliente.objects.all()
    return render(request, "ordens/cliente_lista.html", {"clientes": clientes})
