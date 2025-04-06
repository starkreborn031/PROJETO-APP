from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    valor_base = models.DecimalField(max_digits=10, decimal_places=2)
    duracao_estimada = models.DurationField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
