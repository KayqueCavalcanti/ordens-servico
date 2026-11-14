from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClienteForm
from .models import Cliente

def cliente_lista(request):
    clientes = Cliente.objects.all()
    return render(request, "ordens/cliente_lista.html", {"clientes": clientes})


def cliente_detalhe(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, "ordens/cliente_detalhe.html", {"cliente": cliente})

def cliente_novo(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect("ordens:cliente_detalhe", pk=cliente.pk)
    else:
        form = ClienteForm()
    return render(request, "ordens/cliente_form.html", {"form": form})
