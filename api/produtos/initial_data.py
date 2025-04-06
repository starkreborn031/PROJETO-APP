def criar_dados_iniciais():
    from produtos.models import Categoria

    # Criar categoria padrão
    Categoria.objects.get_or_create(nome="Geral")
