from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    ordering = ['nome']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'categoria', 'preco', 'estoque', 'ativo']
    list_filter = ['categoria', 'ativo']
    search_fields = ['nome', 'descricao']
    list_editable = ['preco', 'estoque', 'ativo']
    ordering = ['nome']




'''
#ORIGINAL
from django.contrib import admin
from .models import Produto

admin.site.register(Produto)
'''