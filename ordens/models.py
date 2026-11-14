from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="equipamentos",
    )
    tipo = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)
    numero_de_serie = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.tipo} {self.marca} {self.modelo} ({self.cliente})"

class OrdemServico(models.Model):
    class Status(models.TextChoices):
        ABERTA = "aberta", "Aberta"
        EM_ANALISE = "em_analise", "Em análise"
        AGUARDANDO_PECA = "aguardando_peca", "Aguardando peça"
        CONCLUIDA = "concluida", "Concluída"
        ENTREGUE = "entregue", "Entregue"


    equipamento = models.ForeignKey(
        Equipamento,
        on_delete=models.PROTECT,
        related_name="ordens"
    )

    valor_orcamento = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    defeito_relatado = models.TextField()
    diagnostico = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ABERTA,
    )

    data_entrada = models.DateTimeField(auto_now_add=True)
    data_saida = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-data_entrada"]
        verbose_name = "ordem de serviço"
        verbose_name_plural = "ordens de serviço"

    def __str__(self):
        return f"OS #{self.pk} - {self.equipamento}"