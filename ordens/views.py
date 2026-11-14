from django.shortcuts import get_object_or_404, render

from .models import Cliente


def cliente_lista(request):
    clientes = Cliente.objects.all()
    return render(request, "ordens/cliente_lista.html", {"clientes": clientes})


def cliente_detalhe(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, "ordens/cliente_detalhe.html", {"cliente": cliente})
