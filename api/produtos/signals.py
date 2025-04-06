from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def criar_dados_iniciais(sender, **kwargs):
    if sender.name == "produtos":  # Garante que só roda para o app 'produtos'
        from .models import Categoria
        Categoria.objects.get_or_create(nome="Geral")
