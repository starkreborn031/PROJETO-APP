from django.db import models

# Representa um cliente da empresa
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# Representa um dispositivo que pertence a um cliente
class Dispositivo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='dispositivos')
    tipo = models.CharField(max_length=50)  # Ex: notebook, desktop, gamer
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.marca} ({self.cliente.nome})"


# Representa um defeito relatado em um dispositivo
class Defeito(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='defeitos')
    descricao = models.TextField()
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Defeito em {self.dispositivo} - {self.descricao[:30]}"


# Representa um serviço realizado em um dispositivo de um cliente
class Servico(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='servicos')
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_execucao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Serviço em {self.dispositivo} - R$ {self.valor}"




'''
#ORIGINAL
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Dispositivo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='dispositivos')
    tipo = models.CharField(max_length=50)  # Ex: Notebook, PC Gamer
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.marca} {self.modelo}"
'''