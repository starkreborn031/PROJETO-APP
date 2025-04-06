from django.db import models
from clientes.models import Cliente, Dispositivo
from servicos.models import Servico
from produtos.models import Produto

class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servico, blank=True)
    produtos = models.ManyToManyField(Produto, through='ProdutoOrdem', blank=True)
    descricao = models.TextField(blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"OS #{self.id} - {self.cliente.nome}"


class ProdutoOrdem(models.Model):
    ordem = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} na OS #{self.ordem.id}"
