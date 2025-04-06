from django.apps import AppConfig

class ProdutosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtos'

    def ready(self):
        import produtos.signals  # Isso registra os signals corretamente




'''
v1.2
from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class ProdutosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtos'

    def ready(self):
        try:
            from .initial_data import criar_dados_iniciais
            criar_dados_iniciais()
        except (OperationalError, ProgrammingError):
            # Ignora erro de banco ainda não migrado
            pass
'''



'''
#v1.1
from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class ProdutosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtos'

    def ready(self):
        try:
            from produtos.models import Categoria
            Categoria.objects.get_or_create(nome="Geral")
        except (OperationalError, ProgrammingError):
            # Isso impede que erros apareçam durante migrações
            pass
'''



'''
#ORIGINAL
from django.apps import AppConfig


class ProdutosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtos'
'''