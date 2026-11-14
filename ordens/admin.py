from django.contrib import admin

from .models import Cliente, Equipamento, OrdemServico

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nome", "telefone", "email", "criado_em"]
    search_fields = ["nome", "telefone", "email"]

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ["tipo", "marca", "modelo", "numero_de_serie", "cliente"]
    search_fields = ["marca", "modelo", "numero_de_serie", "cliente__nome"]
    list_filter = ["tipo"]

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ["id", "equipamento", "status", "valor_orcamento", "data_entrada"]
    search_fields = ["defeito_relatado", "equipamento__cliente__nome"]
    list_filter = ["status", "data_entrada"]

